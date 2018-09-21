# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class PublicDnsNamespace(pulumi.CustomResource):
    """
    Provides a Service Discovery Public DNS Namespace resource.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, name=None):
        """Create a PublicDnsNamespace resource with the given unique name, props, and options."""
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
        The description that you specify for the namespace when you create it.
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the namespace.
        """
        __props__['name'] = name

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN that Amazon Route 53 assigns to the namespace when you create it.
        """
        __self__.hosted_zone = pulumi.runtime.UNKNOWN
        """
        The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
        """

        super(PublicDnsNamespace, __self__).__init__(
            'aws:servicediscovery/publicDnsNamespace:PublicDnsNamespace',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'description' in outs:
            self.description = outs['description']
        if 'hostedZone' in outs:
            self.hosted_zone = outs['hostedZone']
        if 'name' in outs:
            self.name = outs['name']