# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Permission(pulumi.CustomResource):
    action: pulumi.Output[str]
    """
    The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
    """
    event_source_token: pulumi.Output[str]
    """
    The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
    """
    function: pulumi.Output[str]
    """
    Name of the Lambda function whose resource policy you are updating
    """
    principal: pulumi.Output[str]
    """
    The principal who is getting this permission.
    e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
    such as `events.amazonaws.com` or `sns.amazonaws.com`.
    """
    qualifier: pulumi.Output[str]
    """
    Query parameter to specify function version or alias name.
    The permission will then apply to the specific qualified ARN.
    e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
    """
    source_account: pulumi.Output[str]
    """
    This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
    """
    source_arn: pulumi.Output[str]
    """
    When granting Amazon S3 or CloudWatch Events permission to
    invoke your function, you should specify this field with the Amazon Resource Name (ARN)
    for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
    generated from the specified bucket or rule can invoke the function.
    API Gateway ARNs have a unique structure described
    [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
    """
    statement_id: pulumi.Output[str]
    """
    A unique statement identifier. By default generated by this provider.
    """
    statement_id_prefix: pulumi.Output[str]
    """
    A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statement_id`.
    """
    def __init__(__self__, resource_name, opts=None, action=None, event_source_token=None, function=None, principal=None, qualifier=None, source_account=None, source_arn=None, statement_id=None, statement_id_prefix=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates a Lambda permission to allow external sources invoking the Lambda function
        (e.g. CloudWatch Event Rule, SNS or S3).

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        iam_for_lambda = aws.iam.Role("iamForLambda", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        test_lambda = aws.lambda_.Function("testLambda",
            code=pulumi.FileArchive("lambdatest.zip"),
            handler="exports.handler",
            role=iam_for_lambda.arn,
            runtime="nodejs8.10")
        test_alias = aws.lambda_.Alias("testAlias",
            description="a sample description",
            function_name=test_lambda.name,
            function_version="$$LATEST")
        allow_cloudwatch = aws.lambda_.Permission("allowCloudwatch",
            action="lambda:InvokeFunction",
            function=test_lambda.name,
            principal="events.amazonaws.com",
            qualifier=test_alias.name,
            source_arn="arn:aws:events:eu-west-1:111122223333:rule/RunDaily")
        ```

        ## Usage with SNS

        ```python
        import pulumi
        import pulumi_aws as aws

        default_topic = aws.sns.Topic("defaultTopic")
        default_role = aws.iam.Role("defaultRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        func = aws.lambda_.Function("func",
            code=pulumi.FileArchive("lambdatest.zip"),
            handler="exports.handler",
            role=default_role.arn,
            runtime="python2.7")
        with_sns = aws.lambda_.Permission("withSns",
            action="lambda:InvokeFunction",
            function=func.name,
            principal="sns.amazonaws.com",
            source_arn=default_topic.arn)
        lambda_ = aws.sns.TopicSubscription("lambda",
            endpoint=func.arn,
            protocol="lambda",
            topic=default_topic.arn)
        ```

        ## Specify Lambda permissions for API Gateway REST API

        ```python
        import pulumi
        import pulumi_aws as aws

        my_demo_api = aws.apigateway.RestApi("myDemoAPI", description="This is my API for demonstration purposes")
        lambda_permission = aws.lambda_.Permission("lambdaPermission",
            action="lambda:InvokeFunction",
            function="MyDemoFunction",
            principal="apigateway.amazonaws.com",
            source_arn=my_demo_api.execution_arn.apply(lambda execution_arn: f"{execution_arn}/*/*/*"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
        :param pulumi.Input[str] event_source_token: The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
        :param pulumi.Input[dict] function: Name of the Lambda function whose resource policy you are updating
        :param pulumi.Input[str] principal: The principal who is getting this permission.
               e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
               such as `events.amazonaws.com` or `sns.amazonaws.com`.
        :param pulumi.Input[str] qualifier: Query parameter to specify function version or alias name.
               The permission will then apply to the specific qualified ARN.
               e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
        :param pulumi.Input[str] source_account: This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
        :param pulumi.Input[str] source_arn: When granting Amazon S3 or CloudWatch Events permission to
               invoke your function, you should specify this field with the Amazon Resource Name (ARN)
               for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
               generated from the specified bucket or rule can invoke the function.
               API Gateway ARNs have a unique structure described
               [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
        :param pulumi.Input[str] statement_id: A unique statement identifier. By default generated by this provider.
        :param pulumi.Input[str] statement_id_prefix: A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statement_id`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if action is None:
                raise TypeError("Missing required property 'action'")
            __props__['action'] = action
            __props__['event_source_token'] = event_source_token
            if function is None:
                raise TypeError("Missing required property 'function'")
            __props__['function'] = function
            if principal is None:
                raise TypeError("Missing required property 'principal'")
            __props__['principal'] = principal
            __props__['qualifier'] = qualifier
            __props__['source_account'] = source_account
            __props__['source_arn'] = source_arn
            __props__['statement_id'] = statement_id
            __props__['statement_id_prefix'] = statement_id_prefix
        super(Permission, __self__).__init__(
            'aws:lambda/permission:Permission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, action=None, event_source_token=None, function=None, principal=None, qualifier=None, source_account=None, source_arn=None, statement_id=None, statement_id_prefix=None):
        """
        Get an existing Permission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
        :param pulumi.Input[str] event_source_token: The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
        :param pulumi.Input[dict] function: Name of the Lambda function whose resource policy you are updating
        :param pulumi.Input[str] principal: The principal who is getting this permission.
               e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
               such as `events.amazonaws.com` or `sns.amazonaws.com`.
        :param pulumi.Input[str] qualifier: Query parameter to specify function version or alias name.
               The permission will then apply to the specific qualified ARN.
               e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
        :param pulumi.Input[str] source_account: This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
        :param pulumi.Input[str] source_arn: When granting Amazon S3 or CloudWatch Events permission to
               invoke your function, you should specify this field with the Amazon Resource Name (ARN)
               for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
               generated from the specified bucket or rule can invoke the function.
               API Gateway ARNs have a unique structure described
               [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
        :param pulumi.Input[str] statement_id: A unique statement identifier. By default generated by this provider.
        :param pulumi.Input[str] statement_id_prefix: A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statement_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action"] = action
        __props__["event_source_token"] = event_source_token
        __props__["function"] = function
        __props__["principal"] = principal
        __props__["qualifier"] = qualifier
        __props__["source_account"] = source_account
        __props__["source_arn"] = source_arn
        __props__["statement_id"] = statement_id
        __props__["statement_id_prefix"] = statement_id_prefix
        return Permission(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

