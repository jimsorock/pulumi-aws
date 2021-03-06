# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RouteResponse(pulumi.CustomResource):
    api_id: pulumi.Output[str]
    """
    The API identifier.
    """
    model_selection_expression: pulumi.Output[str]
    """
    The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) for the route response.
    """
    response_models: pulumi.Output[dict]
    """
    The response models for the route response.
    """
    route_id: pulumi.Output[str]
    """
    The identifier of the [`apigatewayv2.Route`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html).
    """
    route_response_key: pulumi.Output[str]
    """
    The route response key.
    """
    def __init__(__self__, resource_name, opts=None, api_id=None, model_selection_expression=None, response_models=None, route_id=None, route_response_key=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 route response.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

        ## Example Usage

        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.RouteResponse("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            route_id=aws_apigatewayv2_route["example"]["id"],
            route_response_key="$$default")
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] model_selection_expression: The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) for the route response.
        :param pulumi.Input[dict] response_models: The response models for the route response.
        :param pulumi.Input[str] route_id: The identifier of the [`apigatewayv2.Route`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html).
        :param pulumi.Input[str] route_response_key: The route response key.
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

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['model_selection_expression'] = model_selection_expression
            __props__['response_models'] = response_models
            if route_id is None:
                raise TypeError("Missing required property 'route_id'")
            __props__['route_id'] = route_id
            if route_response_key is None:
                raise TypeError("Missing required property 'route_response_key'")
            __props__['route_response_key'] = route_response_key
        super(RouteResponse, __self__).__init__(
            'aws:apigatewayv2/routeResponse:RouteResponse',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_id=None, model_selection_expression=None, response_models=None, route_id=None, route_response_key=None):
        """
        Get an existing RouteResponse resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] model_selection_expression: The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) for the route response.
        :param pulumi.Input[dict] response_models: The response models for the route response.
        :param pulumi.Input[str] route_id: The identifier of the [`apigatewayv2.Route`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html).
        :param pulumi.Input[str] route_response_key: The route response key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["model_selection_expression"] = model_selection_expression
        __props__["response_models"] = response_models
        __props__["route_id"] = route_id
        __props__["route_response_key"] = route_response_key
        return RouteResponse(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

