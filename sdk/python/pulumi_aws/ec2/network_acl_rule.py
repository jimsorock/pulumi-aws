# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NetworkAclRule(pulumi.CustomResource):
    cidr_block: pulumi.Output[str]
    """
    The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
    """
    egress: pulumi.Output[bool]
    """
    Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
    """
    from_port: pulumi.Output[float]
    """
    The from port to match.
    """
    icmp_code: pulumi.Output[str]
    """
    ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
    """
    icmp_type: pulumi.Output[str]
    """
    ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
    """
    ipv6_cidr_block: pulumi.Output[str]
    """
    The IPv6 CIDR block to allow or deny.
    """
    network_acl_id: pulumi.Output[str]
    """
    The ID of the network ACL.
    """
    protocol: pulumi.Output[str]
    """
    The protocol. A value of -1 means all protocols.
    """
    rule_action: pulumi.Output[str]
    """
    Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
    """
    rule_number: pulumi.Output[float]
    """
    The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
    """
    to_port: pulumi.Output[float]
    """
    The to port to match.
    """
    def __init__(__self__, resource_name, opts=None, cidr_block=None, egress=None, from_port=None, icmp_code=None, icmp_type=None, ipv6_cidr_block=None, network_acl_id=None, protocol=None, rule_action=None, rule_number=None, to_port=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        > **NOTE on Network ACLs and Network ACL Rules:** This provider currently
        provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
        defined in-line. At this time you cannot use a Network ACL with in-line rules
        in conjunction with any Network ACL Rule resources. Doing so will cause
        a conflict of rule settings and will overwrite rules.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        bar_network_acl = aws.ec2.NetworkAcl("barNetworkAcl", vpc_id=aws_vpc["foo"]["id"])
        bar_network_acl_rule = aws.ec2.NetworkAclRule("barNetworkAclRule",
            network_acl_id=bar_network_acl.id,
            rule_number=200,
            egress=False,
            protocol="tcp",
            rule_action="allow",
            cidr_block=aws_vpc["foo"]["cidr_block"],
            from_port=22,
            to_port=22)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_block: The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
        :param pulumi.Input[bool] egress: Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
        :param pulumi.Input[float] from_port: The from port to match.
        :param pulumi.Input[str] icmp_code: ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
        :param pulumi.Input[str] icmp_type: ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
        :param pulumi.Input[str] ipv6_cidr_block: The IPv6 CIDR block to allow or deny.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] protocol: The protocol. A value of -1 means all protocols.
        :param pulumi.Input[str] rule_action: Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
        :param pulumi.Input[float] rule_number: The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
        :param pulumi.Input[float] to_port: The to port to match.
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

            __props__['cidr_block'] = cidr_block
            __props__['egress'] = egress
            __props__['from_port'] = from_port
            __props__['icmp_code'] = icmp_code
            __props__['icmp_type'] = icmp_type
            __props__['ipv6_cidr_block'] = ipv6_cidr_block
            if network_acl_id is None:
                raise TypeError("Missing required property 'network_acl_id'")
            __props__['network_acl_id'] = network_acl_id
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            if rule_action is None:
                raise TypeError("Missing required property 'rule_action'")
            __props__['rule_action'] = rule_action
            if rule_number is None:
                raise TypeError("Missing required property 'rule_number'")
            __props__['rule_number'] = rule_number
            __props__['to_port'] = to_port
        super(NetworkAclRule, __self__).__init__(
            'aws:ec2/networkAclRule:NetworkAclRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cidr_block=None, egress=None, from_port=None, icmp_code=None, icmp_type=None, ipv6_cidr_block=None, network_acl_id=None, protocol=None, rule_action=None, rule_number=None, to_port=None):
        """
        Get an existing NetworkAclRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_block: The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
        :param pulumi.Input[bool] egress: Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
        :param pulumi.Input[float] from_port: The from port to match.
        :param pulumi.Input[str] icmp_code: ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
        :param pulumi.Input[str] icmp_type: ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
        :param pulumi.Input[str] ipv6_cidr_block: The IPv6 CIDR block to allow or deny.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] protocol: The protocol. A value of -1 means all protocols.
        :param pulumi.Input[str] rule_action: Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
        :param pulumi.Input[float] rule_number: The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
        :param pulumi.Input[float] to_port: The to port to match.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cidr_block"] = cidr_block
        __props__["egress"] = egress
        __props__["from_port"] = from_port
        __props__["icmp_code"] = icmp_code
        __props__["icmp_type"] = icmp_type
        __props__["ipv6_cidr_block"] = ipv6_cidr_block
        __props__["network_acl_id"] = network_acl_id
        __props__["protocol"] = protocol
        __props__["rule_action"] = rule_action
        __props__["rule_number"] = rule_number
        __props__["to_port"] = to_port
        return NetworkAclRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

