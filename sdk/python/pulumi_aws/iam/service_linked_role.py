# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ServiceLinkedRole(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) specifying the role.
    """
    aws_service_name: pulumi.Output[str]
    """
    The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
    """
    create_date: pulumi.Output[str]
    """
    The creation date of the IAM role.
    """
    custom_suffix: pulumi.Output[str]
    """
    Additional string appended to the role name. Not all AWS services support custom suffixes.
    """
    description: pulumi.Output[str]
    """
    The description of the role.
    """
    name: pulumi.Output[str]
    """
    The name of the role.
    """
    path: pulumi.Output[str]
    """
    The path of the role.
    """
    unique_id: pulumi.Output[str]
    """
    The stable and unique string identifying the role.
    """
    def __init__(__self__, resource_name, opts=None, aws_service_name=None, custom_suffix=None, description=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        elasticbeanstalk = aws.iam.ServiceLinkedRole("elasticbeanstalk", aws_service_name="elasticbeanstalk.amazonaws.com")
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_service_name: The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
        :param pulumi.Input[str] custom_suffix: Additional string appended to the role name. Not all AWS services support custom suffixes.
        :param pulumi.Input[str] description: The description of the role.
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

            if aws_service_name is None:
                raise TypeError("Missing required property 'aws_service_name'")
            __props__['aws_service_name'] = aws_service_name
            __props__['custom_suffix'] = custom_suffix
            __props__['description'] = description
            __props__['arn'] = None
            __props__['create_date'] = None
            __props__['name'] = None
            __props__['path'] = None
            __props__['unique_id'] = None
        super(ServiceLinkedRole, __self__).__init__(
            'aws:iam/serviceLinkedRole:ServiceLinkedRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, aws_service_name=None, create_date=None, custom_suffix=None, description=None, name=None, path=None, unique_id=None):
        """
        Get an existing ServiceLinkedRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) specifying the role.
        :param pulumi.Input[str] aws_service_name: The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
        :param pulumi.Input[str] create_date: The creation date of the IAM role.
        :param pulumi.Input[str] custom_suffix: Additional string appended to the role name. Not all AWS services support custom suffixes.
        :param pulumi.Input[str] description: The description of the role.
        :param pulumi.Input[str] name: The name of the role.
        :param pulumi.Input[str] path: The path of the role.
        :param pulumi.Input[str] unique_id: The stable and unique string identifying the role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["aws_service_name"] = aws_service_name
        __props__["create_date"] = create_date
        __props__["custom_suffix"] = custom_suffix
        __props__["description"] = description
        __props__["name"] = name
        __props__["path"] = path
        __props__["unique_id"] = unique_id
        return ServiceLinkedRole(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

