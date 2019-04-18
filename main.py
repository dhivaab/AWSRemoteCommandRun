import boto3
import config
from smart_open import smart_open
import time

def executecommandsonwindowsinstances(client, commands):
    resp = client.send_command(
        DocumentName= config.SSMDocumentName,
        Parameters={'commands': commands,"workingDirectory":config.workingdirectory,"executionTimeout":config.executiontimeout},
        InstanceIds=config.InstanceId,
        TimeoutSeconds=config.Querytimeoutseconds,
        OutputS3BucketName=config.OutputS3BucketName,
        OutputS3KeyPrefix=config.OutputS3KeyPrefix
    )
    return resp['Command']['CommandId']    


def reads3logsforstdout(commandid):
    bucketpath = 's3://' + config.OutputS3BucketName + "/" + config.OutputS3KeyPrefix + "/" + commandid + "/" + config.InstanceId[0] + "/" + "awsrunPowerShellScript" + "/" + "0.awsrunPowerShellScript" + "/" + "stdout"
    output = ''
    for line in smart_open(bucketpath, 'rb'):
        output = output + line.decode('utf8')
    return output
ssm_client = boto3.client('ssm',
    region_name= config.region_name,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
) 

commandid = executecommandsonwindowsinstances(ssm_client, ['dir'])
time.sleep(60)
output = reads3logsforstdout(commandid)
print(output)