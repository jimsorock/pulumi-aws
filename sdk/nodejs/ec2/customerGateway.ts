// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Tags} from "../index";

/**
 * Provides a customer gateway inside a VPC. These objects can be connected to VPN gateways via VPN connections, and allow you to establish tunnels between your network and the VPC.
 */
export class CustomerGateway extends pulumi.CustomResource {
    /**
     * Get an existing CustomerGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomerGatewayState): CustomerGateway {
        return new CustomerGateway(name, <any>state, { id });
    }

    /**
     * The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
     */
    public readonly bgpAsn: pulumi.Output<number>;
    /**
     * The IP address of the gateway's Internet-routable external interface.
     */
    public readonly ipAddress: pulumi.Output<string>;
    /**
     * Tags to apply to the gateway.
     */
    public readonly tags: pulumi.Output<Tags | undefined>;
    /**
     * The type of customer gateway. The only type AWS
     * supports at this time is "ipsec.1".
     */
    public readonly type: pulumi.Output<string>;

    /**
     * Create a CustomerGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomerGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomerGatewayArgs | CustomerGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: CustomerGatewayState = argsOrState as CustomerGatewayState | undefined;
            inputs["bgpAsn"] = state ? state.bgpAsn : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as CustomerGatewayArgs | undefined;
            if (!args || args.bgpAsn === undefined) {
                throw new Error("Missing required property 'bgpAsn'");
            }
            if (!args || args.ipAddress === undefined) {
                throw new Error("Missing required property 'ipAddress'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["bgpAsn"] = args ? args.bgpAsn : undefined;
            inputs["ipAddress"] = args ? args.ipAddress : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
        }
        super("aws:ec2/customerGateway:CustomerGateway", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomerGateway resources.
 */
export interface CustomerGatewayState {
    /**
     * The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
     */
    readonly bgpAsn?: pulumi.Input<number>;
    /**
     * The IP address of the gateway's Internet-routable external interface.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * Tags to apply to the gateway.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * The type of customer gateway. The only type AWS
     * supports at this time is "ipsec.1".
     */
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CustomerGateway resource.
 */
export interface CustomerGatewayArgs {
    /**
     * The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
     */
    readonly bgpAsn: pulumi.Input<number>;
    /**
     * The IP address of the gateway's Internet-routable external interface.
     */
    readonly ipAddress: pulumi.Input<string>;
    /**
     * Tags to apply to the gateway.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * The type of customer gateway. The only type AWS
     * supports at this time is "ipsec.1".
     */
    readonly type: pulumi.Input<string>;
}