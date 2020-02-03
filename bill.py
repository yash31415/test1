import json
import boto3

def lambda_handler(event, context):

   #Resource calling for  Cost Explore
   client = boto3.client('ce')

   #Getting Response from cost expolre
   response = client.get_cost_and_usage(

   #Getting Time period to get the cost
       TimePeriod={
           'Start': '2020-01-01', #Change the start date as per requirement
           'End': '2020-01-31' #Change the End date as per requirement
           },

   #Get the billed amount within a certain period
           Granularity='MONTHLY',
           Metrics=[
           'NetAmortizedCost'
           ],
   )

   #Instilizing and Getting respose to get billed amount
   for amount in response['ResultsByTime']:

   #Storing the starting date and timeperiod
       start_date = amount['TimePeriod']['Start']

   #Storing the End date with time period
       end_date = amount['TimePeriod']['End']

   #Estimation of the total cost
       total_cost = "$"+amount['Total']['NetAmortizedCost']['Amount']
       return (total_cost+" of the date "+start_date+" to "+end_date)
lambda_handler("","")
