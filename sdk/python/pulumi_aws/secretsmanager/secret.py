# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Secret(pulumi.CustomResource):
    """
    Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html).
    """
    def __init__(__self__, __name__, __opts__=None, description=None, kms_key_id=None, name=None, policy=None, recovery_window_in_days=None, rotation_lambda_arn=None, rotation_rules=None, tags=None):
        """Create a Secret resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description of the secret.
        """
        __props__['description'] = description

        if kms_key_id and not isinstance(kms_key_id, basestring):
            raise TypeError('Expected property kms_key_id to be a basestring')
        __self__.kms_key_id = kms_key_id
        """
        Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
        """
        __props__['kmsKeyId'] = kms_key_id

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Spaces are not permitted.
        """
        __props__['name'] = name

        if policy and not isinstance(policy, basestring):
            raise TypeError('Expected property policy to be a basestring')
        __self__.policy = policy
        """
        A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
        """
        __props__['policy'] = policy

        if recovery_window_in_days and not isinstance(recovery_window_in_days, int):
            raise TypeError('Expected property recovery_window_in_days to be a int')
        __self__.recovery_window_in_days = recovery_window_in_days
        """
        Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can range from 7 to 30 days. The default value is 30.
        """
        __props__['recoveryWindowInDays'] = recovery_window_in_days

        if rotation_lambda_arn and not isinstance(rotation_lambda_arn, basestring):
            raise TypeError('Expected property rotation_lambda_arn to be a basestring')
        __self__.rotation_lambda_arn = rotation_lambda_arn
        """
        Specifies the ARN of the Lambda function that can rotate the secret.
        """
        __props__['rotationLambdaArn'] = rotation_lambda_arn

        if rotation_rules and not isinstance(rotation_rules, dict):
            raise TypeError('Expected property rotation_rules to be a dict')
        __self__.rotation_rules = rotation_rules
        """
        A structure that defines the rotation configuration for this secret. Defined below.
        """
        __props__['rotationRules'] = rotation_rules

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        Specifies a key-value map of user-defined tags that are attached to the secret.
        """
        __props__['tags'] = tags

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        Amazon Resource Name (ARN) of the secret.
        """
        __self__.rotation_enabled = pulumi.runtime.UNKNOWN
        """
        Specifies whether automatic rotation is enabled for this secret.
        """

        super(Secret, __self__).__init__(
            'aws:secretsmanager/secret:Secret',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'description' in outs:
            self.description = outs['description']
        if 'kmsKeyId' in outs:
            self.kms_key_id = outs['kmsKeyId']
        if 'name' in outs:
            self.name = outs['name']
        if 'policy' in outs:
            self.policy = outs['policy']
        if 'recoveryWindowInDays' in outs:
            self.recovery_window_in_days = outs['recoveryWindowInDays']
        if 'rotationEnabled' in outs:
            self.rotation_enabled = outs['rotationEnabled']
        if 'rotationLambdaArn' in outs:
            self.rotation_lambda_arn = outs['rotationLambdaArn']
        if 'rotationRules' in outs:
            self.rotation_rules = outs['rotationRules']
        if 'tags' in outs:
            self.tags = outs['tags']