import json

def my_handler(event, context):
  print('received event:', )
  print(event)
  
  response = {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda- 2!')
  }
  
  return response
  

'''  
def customer_handler(event, context):
  print(event)
  customerId = event['pathParameters']['customerId']  # API: /customers/123 => 123 becomes customerId
  customer = {'customerId': customerId, 'customerName': "Customer " + customerId}
  response = {
		'statusCode': 200,
		# Uncomment below to enable CORS requests
		'headers': {
		    'Access-Control-Allow-Origin': '*',
		    'Access-Control-Allow-Headers': '*'
		},
		'body': json.dumps(customer)
    }
  return response  
'''  
