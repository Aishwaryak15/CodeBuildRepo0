import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello there Aish from Lambda!....... (Modified v0.2')
    }
