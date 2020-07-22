from json import dumps, loads


def lambda_handler(event, context):
    data = loads(event.get('body', {}))

    return {
        'statusCode': 200,
        'body': dumps(data or {}),
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }
