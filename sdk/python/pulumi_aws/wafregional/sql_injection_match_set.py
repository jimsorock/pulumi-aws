# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class SqlInjectionMatchSet(pulumi.CustomResource):
    """
    Provides a WAF Regional SQL Injection Match Set Resource for use with Application Load Balancer.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, sql_injection_match_tuples=None):
        """Create a SqlInjectionMatchSet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name or description of the SizeConstraintSet.
        """
        __props__['name'] = name

        if sql_injection_match_tuples and not isinstance(sql_injection_match_tuples, list):
            raise TypeError('Expected property sql_injection_match_tuples to be a list')
        __self__.sql_injection_match_tuples = sql_injection_match_tuples
        """
        The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
        """
        __props__['sqlInjectionMatchTuples'] = sql_injection_match_tuples

        super(SqlInjectionMatchSet, __self__).__init__(
            'aws:wafregional/sqlInjectionMatchSet:SqlInjectionMatchSet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'name' in outs:
            self.name = outs['name']
        if 'sqlInjectionMatchTuples' in outs:
            self.sql_injection_match_tuples = outs['sqlInjectionMatchTuples']