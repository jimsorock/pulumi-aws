# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Subnet(pulumi.CustomResource):
    """
    Provides an VPC subnet resource.
    """
    def __init__(__self__, __name__, __opts__=None, assign_ipv6_address_on_creation=None, availability_zone=None, cidr_block=None, ipv6_cidr_block=None, map_public_ip_on_launch=None, tags=None, vpc_id=None):
        """Create a Subnet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if assign_ipv6_address_on_creation and not isinstance(assign_ipv6_address_on_creation, bool):
            raise TypeError('Expected property assign_ipv6_address_on_creation to be a bool')
        __self__.assign_ipv6_address_on_creation = assign_ipv6_address_on_creation
        """
        Specify true to indicate
        that network interfaces created in the specified subnet should be
        assigned an IPv6 address. Default is `false`
        """
        __props__['assignIpv6AddressOnCreation'] = assign_ipv6_address_on_creation

        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        __props__['availabilityZone'] = availability_zone

        if not cidr_block:
            raise TypeError('Missing required property cidr_block')
        elif not isinstance(cidr_block, basestring):
            raise TypeError('Expected property cidr_block to be a basestring')
        __self__.cidr_block = cidr_block
        """
        The CIDR block for the subnet.
        """
        __props__['cidrBlock'] = cidr_block

        if ipv6_cidr_block and not isinstance(ipv6_cidr_block, basestring):
            raise TypeError('Expected property ipv6_cidr_block to be a basestring')
        __self__.ipv6_cidr_block = ipv6_cidr_block
        """
        The IPv6 network range for the subnet,
        in CIDR notation. The subnet size must use a /64 prefix length.
        """
        __props__['ipv6CidrBlock'] = ipv6_cidr_block

        if map_public_ip_on_launch and not isinstance(map_public_ip_on_launch, bool):
            raise TypeError('Expected property map_public_ip_on_launch to be a bool')
        __self__.map_public_ip_on_launch = map_public_ip_on_launch
        """
        Specify true to indicate
        that instances launched into the subnet should be assigned
        a public IP address. Default is `false`.
        """
        __props__['mapPublicIpOnLaunch'] = map_public_ip_on_launch

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if not vpc_id:
            raise TypeError('Missing required property vpc_id')
        elif not isinstance(vpc_id, basestring):
            raise TypeError('Expected property vpc_id to be a basestring')
        __self__.vpc_id = vpc_id
        """
        The VPC ID.
        """
        __props__['vpcId'] = vpc_id

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the subnet.
        * `availability_zone`- The AZ for the subnet.
        """
        __self__.ipv6_cidr_block_association_id = pulumi.runtime.UNKNOWN
        """
        The association ID for the IPv6 CIDR block.
        """

        super(Subnet, __self__).__init__(
            'aws:ec2/subnet:Subnet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'assignIpv6AddressOnCreation' in outs:
            self.assign_ipv6_address_on_creation = outs['assignIpv6AddressOnCreation']
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'cidrBlock' in outs:
            self.cidr_block = outs['cidrBlock']
        if 'ipv6CidrBlock' in outs:
            self.ipv6_cidr_block = outs['ipv6CidrBlock']
        if 'ipv6CidrBlockAssociationId' in outs:
            self.ipv6_cidr_block_association_id = outs['ipv6CidrBlockAssociationId']
        if 'mapPublicIpOnLaunch' in outs:
            self.map_public_ip_on_launch = outs['mapPublicIpOnLaunch']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']