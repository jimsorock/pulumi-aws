# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ScheduledAction(pulumi.CustomResource):
    """
    Provides an Application AutoScaling ScheduledAction resource.
    """
    def __init__(__self__, __name__, __opts__=None, end_time=None, name=None, resource_id=None, scalable_dimension=None, scalable_target_action=None, schedule=None, service_namespace=None, start_time=None):
        """Create a ScheduledAction resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if end_time and not isinstance(end_time, basestring):
            raise TypeError('Expected property end_time to be a basestring')
        __self__.end_time = end_time
        """
        The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z
        """
        __props__['endTime'] = end_time

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the scheduled action.
        """
        __props__['name'] = name

        if not resource_id:
            raise TypeError('Missing required property resource_id')
        elif not isinstance(resource_id, basestring):
            raise TypeError('Expected property resource_id to be a basestring')
        __self__.resource_id = resource_id
        """
        The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)
        """
        __props__['resourceId'] = resource_id

        if scalable_dimension and not isinstance(scalable_dimension, basestring):
            raise TypeError('Expected property scalable_dimension to be a basestring')
        __self__.scalable_dimension = scalable_dimension
        """
        The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount
        """
        __props__['scalableDimension'] = scalable_dimension

        if scalable_target_action and not isinstance(scalable_target_action, dict):
            raise TypeError('Expected property scalable_target_action to be a dict')
        __self__.scalable_target_action = scalable_target_action
        """
        The new minimum and maximum capacity. You can set both values or just one. See below
        """
        __props__['scalableTargetAction'] = scalable_target_action

        if schedule and not isinstance(schedule, basestring):
            raise TypeError('Expected property schedule to be a basestring')
        __self__.schedule = schedule
        """
        The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)
        """
        __props__['schedule'] = schedule

        if not service_namespace:
            raise TypeError('Missing required property service_namespace')
        elif not isinstance(service_namespace, basestring):
            raise TypeError('Expected property service_namespace to be a basestring')
        __self__.service_namespace = service_namespace
        """
        The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs
        """
        __props__['serviceNamespace'] = service_namespace

        if start_time and not isinstance(start_time, basestring):
            raise TypeError('Expected property start_time to be a basestring')
        __self__.start_time = start_time
        """
        The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z
        """
        __props__['startTime'] = start_time

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The Amazon Resource Name (ARN) of the scheduled action.
        """

        super(ScheduledAction, __self__).__init__(
            'aws:appautoscaling/scheduledAction:ScheduledAction',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'endTime' in outs:
            self.end_time = outs['endTime']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceId' in outs:
            self.resource_id = outs['resourceId']
        if 'scalableDimension' in outs:
            self.scalable_dimension = outs['scalableDimension']
        if 'scalableTargetAction' in outs:
            self.scalable_target_action = outs['scalableTargetAction']
        if 'schedule' in outs:
            self.schedule = outs['schedule']
        if 'serviceNamespace' in outs:
            self.service_namespace = outs['serviceNamespace']
        if 'startTime' in outs:
            self.start_time = outs['startTime']