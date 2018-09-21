# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ListenerRule(pulumi.CustomResource):
    """
    Provides a Load Balancer Listener Rule resource.
    
    ~> **Note:** `aws_alb_listener_rule` is known as `aws_lb_listener_rule`. The functionality is identical.
    """
    def __init__(__self__, __name__, __opts__=None, actions=None, conditions=None, listener_arn=None, priority=None):
        """Create a ListenerRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not actions:
            raise TypeError('Missing required property actions')
        elif not isinstance(actions, list):
            raise TypeError('Expected property actions to be a list')
        __self__.actions = actions
        """
        An Action block. Action blocks are documented below.
        """
        __props__['actions'] = actions

        if not conditions:
            raise TypeError('Missing required property conditions')
        elif not isinstance(conditions, list):
            raise TypeError('Expected property conditions to be a list')
        __self__.conditions = conditions
        """
        A Condition block. Condition blocks are documented below.
        """
        __props__['conditions'] = conditions

        if not listener_arn:
            raise TypeError('Missing required property listener_arn')
        elif not isinstance(listener_arn, basestring):
            raise TypeError('Expected property listener_arn to be a basestring')
        __self__.listener_arn = listener_arn
        """
        The ARN of the listener to which to attach the rule.
        """
        __props__['listenerArn'] = listener_arn

        if priority and not isinstance(priority, int):
            raise TypeError('Expected property priority to be a int')
        __self__.priority = priority
        """
        The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        """
        __props__['priority'] = priority

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the rule (matches `id`)
        """

        super(ListenerRule, __self__).__init__(
            'aws:elasticloadbalancingv2/listenerRule:ListenerRule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'actions' in outs:
            self.actions = outs['actions']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'conditions' in outs:
            self.conditions = outs['conditions']
        if 'listenerArn' in outs:
            self.listener_arn = outs['listenerArn']
        if 'priority' in outs:
            self.priority = outs['priority']