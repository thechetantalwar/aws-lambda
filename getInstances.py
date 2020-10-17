import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.resource('ec2')

    instances = ec2.instances.filter(
        Filters = [{'Name'   : 'instance-state-name',
                    'Values' : ['running']}])

    iids = [i.id for i in instances]
    
    return {
        'statusCode': 200,
        'body': json.dumps(iids)
    }
