# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class DeploymentConfig(pulumi.CustomResource):
    """
    Provides a CodeDeploy deployment config for an application
    """
    def __init__(__self__, __name__, __opts__=None, deployment_config_name=None, minimum_healthy_hosts=None):
        """Create a DeploymentConfig resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not deployment_config_name:
            raise TypeError('Missing required property deployment_config_name')
        elif not isinstance(deployment_config_name, basestring):
            raise TypeError('Expected property deployment_config_name to be a basestring')
        __self__.deployment_config_name = deployment_config_name
        """
        The name of the deployment config.
        """
        __props__['deploymentConfigName'] = deployment_config_name

        if not minimum_healthy_hosts:
            raise TypeError('Missing required property minimum_healthy_hosts')
        elif not isinstance(minimum_healthy_hosts, dict):
            raise TypeError('Expected property minimum_healthy_hosts to be a dict')
        __self__.minimum_healthy_hosts = minimum_healthy_hosts
        """
        A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.
        """
        __props__['minimumHealthyHosts'] = minimum_healthy_hosts

        __self__.deployment_config_id = pulumi.runtime.UNKNOWN
        """
        The AWS Assigned deployment config id
        """

        super(DeploymentConfig, __self__).__init__(
            'aws:codedeploy/deploymentConfig:DeploymentConfig',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'deploymentConfigId' in outs:
            self.deployment_config_id = outs['deploymentConfigId']
        if 'deploymentConfigName' in outs:
            self.deployment_config_name = outs['deploymentConfigName']
        if 'minimumHealthyHosts' in outs:
            self.minimum_healthy_hosts = outs['minimumHealthyHosts']