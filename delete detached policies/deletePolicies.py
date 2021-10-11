import boto3

#create IAM class
client = boto3.client('iam')

#Get list of policies, scope is set to Local(customer managed)
policies = client.list_policies(
    Scope='Local | AWS',
    OnlyAttached= False,

)
#iternate policies dict{}
for v in policies.get('Policies'):
    policyarn = v.get('Arn')
    
    respone = client.delete_policy(
    PolicyArn= policyarn 
  )
    
