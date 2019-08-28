# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetPrefixListResult:
    """
    A collection of values returned by getPrefixList.
    """
    def __init__(__self__, cidr_blocks=None, name=None, prefix_list_id=None, id=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError("Expected argument 'cidr_blocks' to be a list")
        __self__.cidr_blocks = cidr_blocks
        """
        The list of CIDR blocks for the AWS service associated
        with the prefix list.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the selected prefix list.
        """
        if prefix_list_id and not isinstance(prefix_list_id, str):
            raise TypeError("Expected argument 'prefix_list_id' to be a str")
        __self__.prefix_list_id = prefix_list_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetPrefixListResult(GetPrefixListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrefixListResult(
            cidr_blocks=self.cidr_blocks,
            name=self.name,
            prefix_list_id=self.prefix_list_id,
            id=self.id)

def get_prefix_list(name=None,prefix_list_id=None,opts=None):
    """
    `.getPrefixList` provides details about a specific prefix list (PL)
    in the current region.
    
    This can be used both to validate a prefix list given in a variable
    and to obtain the CIDR blocks (IP address ranges) for the associated
    AWS service. The latter may be useful e.g. for adding network ACL
    rules.
    
    :param str name: The name of the prefix list to select.
    :param str prefix_list_id: The ID of the prefix list to select.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/prefix_list.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['prefixListId'] = prefix_list_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getPrefixList:getPrefixList', __args__, opts=opts).value

    return AwaitableGetPrefixListResult(
        cidr_blocks=__ret__.get('cidrBlocks'),
        name=__ret__.get('name'),
        prefix_list_id=__ret__.get('prefixListId'),
        id=__ret__.get('id'))
