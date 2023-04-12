from celery import Celery
import os
import subprocess
import pika
import sys


# app = Celery('tasks',backend='rpc://', broker='pyamqp://guest@localhost//')

app = Celery('tasks',backend='redis://localhost', broker='pyamqp://guest@localhost//')
# backend='redis://localhost'


def publish(output, errors, function_id):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    message = output
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    # print("Function {} output: {}".format(function_id, output))
    connection.close()

@app.task
def invokeFunction(functionName,payload, pipeline_id, function_id):
    celery_task_id = app.current_task.request.id
    print("Worker received a request for invokeFunction({},{})".format(functionName,payload))
    print("taskId = {} , pipeline_id = {} , function_id = {} ".format(celery_task_id,pipeline_id,function_id))
    try:
       command_to_exec = ["faas-cli", "invoke",functionName]
       print(command_to_exec)
       funcCall = subprocess.Popen(command_to_exec, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
       output, errors = funcCall.communicate(input=payload)
       funcCall.wait()

        ## Just for testing
    #    output = functionName + " finished"
       publish(output,errors, function_id)

    except subprocess.CalledProcessError as e:
        print(e.output)
    return "execution Faild"
