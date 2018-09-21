# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class NetworkInterfaceSecurityGroupAttachment(pulumi.CustomResource):
    """
    This resource attaches a security group to an Elastic Network Interface (ENI).
    It can be used to attach a security group to any existing ENI, be it a
    secondary ENI or one attached as the primary interface on an instance.
    
    ~> **NOTE on instances, interfaces, and security groups:** Terraform currently
    provides the capability to assign security groups via the [`aws_instance`][1]
    and the [`aws_network_interface`][2] resources. Using this resource in
    conjunction with security groups provided in-line in those resources will cause
    conflicts, and will lead to spurious diffs and undefined behavior - please use
    one or the other.
    
    [1]: /docs/providers/aws/d/instance.html
    [2]: /docs/providers/aws/r/network_interface.html
    """
    def __init__(__self__, __name__, __opts__=None, network_interface_id=None, security_group_id=None):
        """Create a NetworkInterfaceSecurityGroupAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not network_interface_id:
            raise TypeError('Missing required property network_interface_id')
        elif not isinstance(network_interface_id, basestring):
            raise TypeError('Expected property network_interface_id to be a basestring')
        __self__.network_interface_id = network_interface_id
        """
        The ID of the network interface to attach to.
        """
        __props__['networkInterfaceId'] = network_interface_id

        if not security_group_id:
            raise TypeError('Missing required property security_group_id')
        elif not isinstance(security_group_id, basestring):
            raise TypeError('Expected property security_group_id to be a basestring')
        __self__.security_group_id = security_group_id
        """
        The ID of the security group.
        """
        __props__['securityGroupId'] = security_group_id

        super(NetworkInterfaceSecurityGroupAttachment, __self__).__init__(
            'aws:ec2/networkInterfaceSecurityGroupAttachment:NetworkInterfaceSecurityGroupAttachment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'networkInterfaceId' in outs:
            self.network_interface_id = outs['networkInterfaceId']
        if 'securityGroupId' in outs:
            self.security_group_id = outs['securityGroupId']