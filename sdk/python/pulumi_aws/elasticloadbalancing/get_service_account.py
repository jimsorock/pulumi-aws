# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

warnings.warn("aws.elasticloadbalancing.getServiceAccount has been deprecated in favor of aws.elb.getServiceAccount", DeprecationWarning)
class GetServiceAccountResult:
    """
    A collection of values returned by getServiceAccount.
    """
    def __init__(__self__, arn=None, id=None, region=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The ARN of the AWS ELB service account in the selected region.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
class AwaitableGetServiceAccountResult(GetServiceAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceAccountResult(
            arn=self.arn,
            id=self.id,
            region=self.region)

def get_service_account(region=None,opts=None):
    """
    Use this data source to get the Account ID of the [AWS Elastic Load Balancing Service Account](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy)
    in a given region for the purpose of whitelisting in S3 bucket policy.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_aws as aws

    main = aws.elb.get_service_account()
    elb_logs = aws.s3.Bucket("elbLogs",
        acl="private",
        policy=f\"\"\"{{
      "Id": "Policy",
      "Version": "2012-10-17",
      "Statement": [
        {{
          "Action": [
            "s3:PutObject"
          ],
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::my-elb-tf-test-bucket/AWSLogs/*",
          "Principal": {{
            "AWS": [
              "{main.arn}"
            ]
          }}
        }}
      ]
    }}

    \"\"\")
    bar = aws.elb.LoadBalancer("bar",
        access_logs={
            "bucket": elb_logs.bucket,
            "interval": 5,
        },
        availability_zones=["us-west-2a"],
        listeners=[{
            "instancePort": 8000,
            "instanceProtocol": "http",
            "lbPort": 80,
            "lbProtocol": "http",
        }])
    ```



    :param str region: Name of the region whose AWS ELB account ID is desired.
           Defaults to the region from the AWS provider configuration.
    """
    pulumi.log.warn("get_service_account is deprecated: aws.elasticloadbalancing.getServiceAccount has been deprecated in favor of aws.elb.getServiceAccount")
    __args__ = dict()


    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elasticloadbalancing/getServiceAccount:getServiceAccount', __args__, opts=opts).value

    return AwaitableGetServiceAccountResult(
        arn=__ret__.get('arn'),
        id=__ret__.get('id'),
        region=__ret__.get('region'))
