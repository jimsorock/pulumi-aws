# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class DefaultVpcDhcpOptions(pulumi.CustomResource):
    """
    Provides a resource to manage the [default AWS DHCP Options Set](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#AmazonDNS)
    in the current region.
    
    Each AWS region comes with a default set of DHCP options.
    **This is an advanced resource**, and has special caveats to be aware of when
    using it. Please read this document in its entirety before using this resource.
    
    The `aws_default_vpc_dhcp_options` behaves differently from normal resources, in that
    Terraform does not _create_ this resource, but instead "adopts" it
    into management. 
    """
    def __init__(__self__, __name__, __opts__=None, netbios_name_servers=None, netbios_node_type=None, tags=None):
        """Create a DefaultVpcDhcpOptions resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if netbios_name_servers and not isinstance(netbios_name_servers, list):
            raise TypeError('Expected property netbios_name_servers to be a list')
        __self__.netbios_name_servers = netbios_name_servers
        """
        List of NETBIOS name servers.
        """
        __props__['netbiosNameServers'] = netbios_name_servers

        if netbios_node_type and not isinstance(netbios_node_type, basestring):
            raise TypeError('Expected property netbios_node_type to be a basestring')
        __self__.netbios_node_type = netbios_node_type
        """
        The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        """
        __props__['netbiosNodeType'] = netbios_node_type

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.domain_name = pulumi.runtime.UNKNOWN
        __self__.domain_name_servers = pulumi.runtime.UNKNOWN
        __self__.ntp_servers = pulumi.runtime.UNKNOWN

        super(DefaultVpcDhcpOptions, __self__).__init__(
            'aws:ec2/defaultVpcDhcpOptions:DefaultVpcDhcpOptions',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'domainName' in outs:
            self.domain_name = outs['domainName']
        if 'domainNameServers' in outs:
            self.domain_name_servers = outs['domainNameServers']
        if 'netbiosNameServers' in outs:
            self.netbios_name_servers = outs['netbiosNameServers']
        if 'netbiosNodeType' in outs:
            self.netbios_node_type = outs['netbiosNodeType']
        if 'ntpServers' in outs:
            self.ntp_servers = outs['ntpServers']
        if 'tags' in outs:
            self.tags = outs['tags']