import json
import boto3 

def lambda_handler(event, context):
    # TODO implement
    
    client = boto3.client('logs')
    
    for i in event['metrics']:
        
        log_Group_Name = i['logGroupName']
        filter_Name = i['filterName']
        filter_Pattern = i['filterPattern']
        
        metric_Name = i['metricName']
        metric_Namespace = i['metricNamespace']
        metric_Value = i['metricValue']
        
        response = client.put_metric_filter(
        logGroupName=log_Group_Name,
        filterName=filter_Name,
        filterPattern=filter_Pattern,
        metricTransformations=[
            {
                'metricName': metric_Name,
                'metricNamespace': metric_Namespace,
                'metricValue': metric_Value
            }
        ]
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
