// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a VPC Endpoint Service resource.
 * Service consumers can create an _Interface_ VPC Endpoint to connect to the service.
 * 
 * ~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
 * both a standalone VPC Endpoint Service Allowed Principal resource
 * and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
 * a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
 * and will overwrite the association.
 */
export class VpcEndpointService extends pulumi.CustomResource {
    /**
     * Get an existing VpcEndpointService resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointServiceState): VpcEndpointService {
        return new VpcEndpointService(name, <any>state, { id });
    }

    /**
     * Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.
     */
    public readonly acceptanceRequired: pulumi.Output<boolean>;
    /**
     * The ARNs of one or more principals allowed to discover the endpoint service.
     */
    public readonly allowedPrincipals: pulumi.Output<string[]>;
    /**
     * The Availability Zones in which the service is available.
     */
    public /*out*/ readonly availabilityZones: pulumi.Output<string[]>;
    /**
     * The DNS names for the service.
     */
    public /*out*/ readonly baseEndpointDnsNames: pulumi.Output<string[]>;
    /**
     * The ARNs of one or more Network Load Balancers for the endpoint service.
     */
    public readonly networkLoadBalancerArns: pulumi.Output<string[]>;
    /**
     * The private DNS name for the service.
     */
    public /*out*/ readonly privateDnsName: pulumi.Output<string>;
    /**
     * The service name.
     */
    public /*out*/ readonly serviceName: pulumi.Output<string>;
    /**
     * The service type, `Gateway` or `Interface`.
     */
    public /*out*/ readonly serviceType: pulumi.Output<string>;
    /**
     * The state of the VPC endpoint service.
     */
    public /*out*/ readonly state: pulumi.Output<string>;

    /**
     * Create a VpcEndpointService resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcEndpointServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VpcEndpointServiceArgs | VpcEndpointServiceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VpcEndpointServiceState = argsOrState as VpcEndpointServiceState | undefined;
            inputs["acceptanceRequired"] = state ? state.acceptanceRequired : undefined;
            inputs["allowedPrincipals"] = state ? state.allowedPrincipals : undefined;
            inputs["availabilityZones"] = state ? state.availabilityZones : undefined;
            inputs["baseEndpointDnsNames"] = state ? state.baseEndpointDnsNames : undefined;
            inputs["networkLoadBalancerArns"] = state ? state.networkLoadBalancerArns : undefined;
            inputs["privateDnsName"] = state ? state.privateDnsName : undefined;
            inputs["serviceName"] = state ? state.serviceName : undefined;
            inputs["serviceType"] = state ? state.serviceType : undefined;
            inputs["state"] = state ? state.state : undefined;
        } else {
            const args = argsOrState as VpcEndpointServiceArgs | undefined;
            if (!args || args.acceptanceRequired === undefined) {
                throw new Error("Missing required property 'acceptanceRequired'");
            }
            if (!args || args.networkLoadBalancerArns === undefined) {
                throw new Error("Missing required property 'networkLoadBalancerArns'");
            }
            inputs["acceptanceRequired"] = args ? args.acceptanceRequired : undefined;
            inputs["allowedPrincipals"] = args ? args.allowedPrincipals : undefined;
            inputs["networkLoadBalancerArns"] = args ? args.networkLoadBalancerArns : undefined;
            inputs["availabilityZones"] = undefined /*out*/;
            inputs["baseEndpointDnsNames"] = undefined /*out*/;
            inputs["privateDnsName"] = undefined /*out*/;
            inputs["serviceName"] = undefined /*out*/;
            inputs["serviceType"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
        }
        super("aws:ec2/vpcEndpointService:VpcEndpointService", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VpcEndpointService resources.
 */
export interface VpcEndpointServiceState {
    /**
     * Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.
     */
    readonly acceptanceRequired?: pulumi.Input<boolean>;
    /**
     * The ARNs of one or more principals allowed to discover the endpoint service.
     */
    readonly allowedPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The Availability Zones in which the service is available.
     */
    readonly availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The DNS names for the service.
     */
    readonly baseEndpointDnsNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ARNs of one or more Network Load Balancers for the endpoint service.
     */
    readonly networkLoadBalancerArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The private DNS name for the service.
     */
    readonly privateDnsName?: pulumi.Input<string>;
    /**
     * The service name.
     */
    readonly serviceName?: pulumi.Input<string>;
    /**
     * The service type, `Gateway` or `Interface`.
     */
    readonly serviceType?: pulumi.Input<string>;
    /**
     * The state of the VPC endpoint service.
     */
    readonly state?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VpcEndpointService resource.
 */
export interface VpcEndpointServiceArgs {
    /**
     * Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.
     */
    readonly acceptanceRequired: pulumi.Input<boolean>;
    /**
     * The ARNs of one or more principals allowed to discover the endpoint service.
     */
    readonly allowedPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ARNs of one or more Network Load Balancers for the endpoint service.
     */
    readonly networkLoadBalancerArns: pulumi.Input<pulumi.Input<string>[]>;
}