# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Vpc(pulumi.CustomResource):
    """
    Provides an VPC resource.
    """
    def __init__(__self__, __name__, __opts__=None, assign_generated_ipv6_cidr_block=None, cidr_block=None, enable_classiclink=None, enable_classiclink_dns_support=None, enable_dns_hostnames=None, enable_dns_support=None, instance_tenancy=None, tags=None):
        """Create a Vpc resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['assign_generated_ipv6_cidr_block'] = assign_generated_ipv6_cidr_block

        if not cidr_block:
            raise TypeError('Missing required property cidr_block')
        __props__['cidr_block'] = cidr_block

        __props__['enable_classiclink'] = enable_classiclink

        __props__['enable_classiclink_dns_support'] = enable_classiclink_dns_support

        __props__['enable_dns_hostnames'] = enable_dns_hostnames

        __props__['enable_dns_support'] = enable_dns_support

        __props__['instance_tenancy'] = instance_tenancy

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['default_network_acl_id'] = None
        __props__['default_route_table_id'] = None
        __props__['default_security_group_id'] = None
        __props__['dhcp_options_id'] = None
        __props__['ipv6_association_id'] = None
        __props__['ipv6_cidr_block'] = None
        __props__['main_route_table_id'] = None
        __props__['owner_id'] = None

        super(Vpc, __self__).__init__(
            'aws:ec2/vpc:Vpc',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

