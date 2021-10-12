import pulumi_aws as aws
from pulumi_aws.lambda_.get_function import AwaitableGetFunctionResult
from pulumi_aws.lambda_.get_function import get_function

class APIGatewayBuilder:

    api: aws.apigateway.RestApi
    deploy_api: aws.apigateway.Deployment or None

    resource_alert: aws.apigateway.Resource
    method_alert: aws.apigateway.Method
    integration_alert: aws.apigateway.Integration
    method_response_200_alert: aws.apigateway.MethodResponse
    integration_response_alert: aws.apigateway.IntegrationResponse

    lambda_notificator: AwaitableGetFunctionResult
    lambda_notificator_permission: aws.lambda_.Permission

    def __init__(self, account_id: str, region: str, api_name: str, resource_name: str,
        f_name: str, response_templates) -> None:

        self.api = aws.apigateway.RestApi(api_name, name=api_name)
        self.resource_alert = aws.apigateway.Resource("resource_alert", 
            rest_api=self.api.id,
            parent_id=self.api.root_resource_id,
            path_part=resource_name
        )

        self.method_alert = aws.apigateway.Method("method_alert",
            rest_api=self.api,
            resource_id=self.resource_alert.id,
            http_method="POST",
            authorization="NONE"
        )

        self.lambda_notificator = get_function(
            function_name=f_name
        )

        self.lambda_notificator_permission = aws.lambda_.Permission("lambda_notificator_permission",
            action="lambda:InvokeFunction",
            function=self.lambda_notificator.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=self.api.id.apply(lambda id: f"arn:aws:execute-api:{region}:{account_id}:{id}/*")
        )

        self.integration_alert = aws.apigateway.Integration("integration_alert",
            rest_api=self.api,
            resource_id=self.resource_alert.id,
            http_method=self.method_alert.http_method,
            integration_http_method= "POST",
            type="AWS",
            uri=self.lambda_notificator.invoke_arn
        )

        self.method_response_200_alert = aws.apigateway.MethodResponse("method_response_200_alert",
            rest_api=self.api,
            resource_id=self.resource_alert.id,
            http_method=self.method_alert.http_method,
            status_code="200",
            response_models={
                "application/json": "Empty"
            }
        )

        self.integration_response_alert = aws.apigateway.IntegrationResponse("integration_response_alert",
            rest_api=self.api,
            resource_id=self.resource_alert.id,
            http_method=self.method_alert.http_method,
            status_code=self.method_response_200_alert.status_code,
            response_templates=response_templates
        )

