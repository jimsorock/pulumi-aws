# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Stack(pulumi.CustomResource):
    capabilities: pulumi.Output[list]
    """
    A list of capabilities.
    Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
    """
    disable_rollback: pulumi.Output[bool]
    """
    Set to true to disable rollback of the stack if stack creation failed.
    Conflicts with `on_failure`.
    """
    iam_role_arn: pulumi.Output[str]
    """
    The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
    """
    name: pulumi.Output[str]
    """
    Stack name.
    """
    notification_arns: pulumi.Output[list]
    """
    A list of SNS topic ARNs to publish stack related events.
    """
    on_failure: pulumi.Output[str]
    """
    Action to be taken if stack creation fails. This must be
    one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
    """
    outputs: pulumi.Output[dict]
    """
    A map of outputs from the stack.
    """
    parameters: pulumi.Output[dict]
    """
    A map of Parameter structures that specify input parameters for the stack.
    """
    policy_body: pulumi.Output[str]
    """
    Structure containing the stack policy body.
    Conflicts w/ `policy_url`.
    """
    policy_url: pulumi.Output[str]
    """
    Location of a file containing the stack policy.
    Conflicts w/ `policy_body`.
    """
    tags: pulumi.Output[dict]
    """
    A list of tags to associate with this stack.
    """
    template_body: pulumi.Output[str]
    """
    Structure containing the template body (max size: 51,200 bytes).
    """
    template_url: pulumi.Output[str]
    """
    Location of a file containing the template body (max size: 460,800 bytes).
    """
    timeout_in_minutes: pulumi.Output[float]
    """
    The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
    """
    def __init__(__self__, resource_name, opts=None, capabilities=None, disable_rollback=None, iam_role_arn=None, name=None, notification_arns=None, on_failure=None, parameters=None, policy_body=None, policy_url=None, tags=None, template_body=None, template_url=None, timeout_in_minutes=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a CloudFormation Stack resource.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        network = aws.cloudformation.Stack("network",
            parameters={
                "VPCCidr": "10.0.0.0/16",
            },
            template_body=\"\"\"{
          "Parameters" : {
            "VPCCidr" : {
              "Type" : "String",
              "Default" : "10.0.0.0/16",
              "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
            }
          },
          "Resources" : {
            "myVpc": {
              "Type" : "AWS::EC2::VPC",
              "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                  {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
              }
            }
          }
        }

        \"\"\")
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] capabilities: A list of capabilities.
               Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
        :param pulumi.Input[bool] disable_rollback: Set to true to disable rollback of the stack if stack creation failed.
               Conflicts with `on_failure`.
        :param pulumi.Input[str] iam_role_arn: The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        :param pulumi.Input[str] name: Stack name.
        :param pulumi.Input[list] notification_arns: A list of SNS topic ARNs to publish stack related events.
        :param pulumi.Input[str] on_failure: Action to be taken if stack creation fails. This must be
               one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
        :param pulumi.Input[dict] parameters: A map of Parameter structures that specify input parameters for the stack.
        :param pulumi.Input[str] policy_body: Structure containing the stack policy body.
               Conflicts w/ `policy_url`.
        :param pulumi.Input[str] policy_url: Location of a file containing the stack policy.
               Conflicts w/ `policy_body`.
        :param pulumi.Input[dict] tags: A list of tags to associate with this stack.
        :param pulumi.Input[str] template_body: Structure containing the template body (max size: 51,200 bytes).
        :param pulumi.Input[str] template_url: Location of a file containing the template body (max size: 460,800 bytes).
        :param pulumi.Input[float] timeout_in_minutes: The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
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

            __props__['capabilities'] = capabilities
            __props__['disable_rollback'] = disable_rollback
            __props__['iam_role_arn'] = iam_role_arn
            __props__['name'] = name
            __props__['notification_arns'] = notification_arns
            __props__['on_failure'] = on_failure
            __props__['parameters'] = parameters
            __props__['policy_body'] = policy_body
            __props__['policy_url'] = policy_url
            __props__['tags'] = tags
            __props__['template_body'] = template_body
            __props__['template_url'] = template_url
            __props__['timeout_in_minutes'] = timeout_in_minutes
            __props__['outputs'] = None
        super(Stack, __self__).__init__(
            'aws:cloudformation/stack:Stack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, capabilities=None, disable_rollback=None, iam_role_arn=None, name=None, notification_arns=None, on_failure=None, outputs=None, parameters=None, policy_body=None, policy_url=None, tags=None, template_body=None, template_url=None, timeout_in_minutes=None):
        """
        Get an existing Stack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] capabilities: A list of capabilities.
               Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
        :param pulumi.Input[bool] disable_rollback: Set to true to disable rollback of the stack if stack creation failed.
               Conflicts with `on_failure`.
        :param pulumi.Input[str] iam_role_arn: The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        :param pulumi.Input[str] name: Stack name.
        :param pulumi.Input[list] notification_arns: A list of SNS topic ARNs to publish stack related events.
        :param pulumi.Input[str] on_failure: Action to be taken if stack creation fails. This must be
               one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
        :param pulumi.Input[dict] outputs: A map of outputs from the stack.
        :param pulumi.Input[dict] parameters: A map of Parameter structures that specify input parameters for the stack.
        :param pulumi.Input[str] policy_body: Structure containing the stack policy body.
               Conflicts w/ `policy_url`.
        :param pulumi.Input[str] policy_url: Location of a file containing the stack policy.
               Conflicts w/ `policy_body`.
        :param pulumi.Input[dict] tags: A list of tags to associate with this stack.
        :param pulumi.Input[str] template_body: Structure containing the template body (max size: 51,200 bytes).
        :param pulumi.Input[str] template_url: Location of a file containing the template body (max size: 460,800 bytes).
        :param pulumi.Input[float] timeout_in_minutes: The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["capabilities"] = capabilities
        __props__["disable_rollback"] = disable_rollback
        __props__["iam_role_arn"] = iam_role_arn
        __props__["name"] = name
        __props__["notification_arns"] = notification_arns
        __props__["on_failure"] = on_failure
        __props__["outputs"] = outputs
        __props__["parameters"] = parameters
        __props__["policy_body"] = policy_body
        __props__["policy_url"] = policy_url
        __props__["tags"] = tags
        __props__["template_body"] = template_body
        __props__["template_url"] = template_url
        __props__["timeout_in_minutes"] = timeout_in_minutes
        return Stack(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

