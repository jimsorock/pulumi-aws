# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetPolicyResult:
    """
    A collection of values returned by getPolicy.
    """
    def __init__(__self__, arn=None, description=None, id=None, name=None, path=None, policy=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) specifying the policy.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the policy.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the IAM policy.
        """
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        """
        The path to the policy.
        """
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        __self__.policy = policy
        """
        The policy document of the policy.
        """
class AwaitableGetPolicyResult(GetPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyResult(
            arn=self.arn,
            description=self.description,
            id=self.id,
            name=self.name,
            path=self.path,
            policy=self.policy)

def get_policy(arn=None,opts=None):
    """
    This data source can be used to fetch information about a specific
    IAM policy.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_policy(arn="arn:aws:iam::123456789012:policy/UsersManageOwnCredentials")
    ```



    :param str arn: ARN of the IAM policy.
    """
    __args__ = dict()


    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getPolicy:getPolicy', __args__, opts=opts).value

    return AwaitableGetPolicyResult(
        arn=__ret__.get('arn'),
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        path=__ret__.get('path'),
        policy=__ret__.get('policy'))
