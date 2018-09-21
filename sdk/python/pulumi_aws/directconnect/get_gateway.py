# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetGatewayResult(object):
    """
    A collection of values returned by getGateway.
    """
    def __init__(__self__, amazon_side_asn=None, id=None):
        if amazon_side_asn and not isinstance(amazon_side_asn, basestring):
            raise TypeError('Expected argument amazon_side_asn to be a basestring')
        __self__.amazon_side_asn = amazon_side_asn
        """
        The ASN on the Amazon side of the connection.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_gateway(name=None):
    """
    Retrieve information about a Direct Connect Gateway.
    """
    __args__ = dict()

    __args__['name'] = name
    __ret__ = pulumi.runtime.invoke('aws:directconnect/getGateway:getGateway', __args__)

    return GetGatewayResult(
        amazon_side_asn=__ret__.get('amazonSideAsn'),
        id=__ret__.get('id'))