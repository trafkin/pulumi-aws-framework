"""A Python Pulumi program"""

from pulumi_aws.apigateway.response import Response
from api_gateway import APIGatewayBuilder
import variables

account_id=variables.var_account_id
region=variables.var_region
api_name=variables.var_api_name
resource_name=variables.var_resource_name
function_name=variables.var_function_name
response_template=variables.var_response_template

api_gateway = APIGatewayBuilder(account_id, region, api_name, resource_name, function_name, response_template)
