# awsutils

import boto3
import os
from pprintpp import pprint


def get_session(region):
    return boto3.session.Session(
        region_name="us-west-2",
        aws_access_key_id=os.environ['ACCESS_ID'],
        aws_secret_access_key=os.environ['ACCESS_KEY'])

session = get_session('us-east-1')
client = session.client('ec2')

# print("start")
# pprint(client.describe_instances())
# pprint(client.run_instances(ImageId='ami-07b9ecc5dd818b08c', MinCount=1, MaxCount=1, InstanceType='t2.micro'))
# demo = client.describe_instances()
# instance_id = demo['Reservations'][0]['Instances'][0]['InstanceId']
# print("finish")
# pprint(client.describe_instances())
# # pprint.pprint(client.terminate_instances(InstanceIds=[instance_id]))
# # res = client.terminate_instances(InstanceIds=[instance_id])


def any_running_instance(status):
    reservations = status['Reservations']
    for r in reservations:
        if r['Instances'][0]['State']['Name'] != "terminated":
            print(r['Instances'][0]['InstanceId'])
            return r['Instances'][0]['InstanceId']
    return False


def start_vm():
    print("Starting instance...")
    status = client.describe_instances()
    if any_running_instance(status):
        return "Instance already existed, exiting..."
    res = client.run_instances(ImageId='ami-07b9ecc5dd818b08c', MinCount=1, MaxCount=1, InstanceType='t2.micro')
    return res


def stop_vm():
    print("Stopping instance...")
    status = client.describe_instances()
    instance_id = any_running_instance(status)
    if not instance_id:
        return "No instance to stop, exiting..."
    res = client.terminate_instances(InstanceIds=[instance_id])
    return res