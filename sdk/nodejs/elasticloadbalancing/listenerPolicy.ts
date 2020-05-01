// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Attaches a load balancer policy to an ELB Listener.
 * 
 * 
 * ## Example Usage for Custom Policy
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const wuTang = new aws.elb.LoadBalancer("wu-tang", {
 *     availabilityZones: ["us-east-1a"],
 *     listeners: [{
 *         instancePort: 443,
 *         instanceProtocol: "http",
 *         lbPort: 443,
 *         lbProtocol: "https",
 *         sslCertificateId: "arn:aws:iam::000000000000:server-certificate/wu-tang.net",
 *     }],
 *     tags: {
 *         Name: "wu-tang",
 *     },
 * });
 * const wuTangSsl = new aws.elb.LoadBalancerPolicy("wu-tang-ssl", {
 *     loadBalancerName: wu_tang.name,
 *     policyAttributes: [
 *         {
 *             name: "ECDHE-ECDSA-AES128-GCM-SHA256",
 *             value: "true",
 *         },
 *         {
 *             name: "Protocol-TLSv1.2",
 *             value: "true",
 *         },
 *     ],
 *     policyName: "wu-tang-ssl",
 *     policyTypeName: "SSLNegotiationPolicyType",
 * });
 * const wuTangListenerPolicies443 = new aws.elb.ListenerPolicy("wu-tang-listener-policies-443", {
 *     loadBalancerName: wu_tang.name,
 *     loadBalancerPort: 443,
 *     policyNames: [wu_tang_ssl.policyName],
 * });
 * ```
 * 
 * This example shows how to customize the TLS settings of an HTTPS listener.
 * 
 * ## Example Usage for AWS Predefined Security Policy
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const wuTang = new aws.elb.LoadBalancer("wu-tang", {
 *     availabilityZones: ["us-east-1a"],
 *     listeners: [{
 *         instancePort: 443,
 *         instanceProtocol: "http",
 *         lbPort: 443,
 *         lbProtocol: "https",
 *         sslCertificateId: "arn:aws:iam::000000000000:server-certificate/wu-tang.net",
 *     }],
 *     tags: {
 *         Name: "wu-tang",
 *     },
 * });
 * const wuTangSslTls11 = new aws.elb.LoadBalancerPolicy("wu-tang-ssl-tls-1-1", {
 *     loadBalancerName: wu_tang.name,
 *     policyAttributes: [{
 *         name: "Reference-Security-Policy",
 *         value: "ELBSecurityPolicy-TLS-1-1-2017-01",
 *     }],
 *     policyName: "wu-tang-ssl",
 *     policyTypeName: "SSLNegotiationPolicyType",
 * });
 * const wuTangListenerPolicies443 = new aws.elb.ListenerPolicy("wu-tang-listener-policies-443", {
 *     loadBalancerName: wu_tang.name,
 *     loadBalancerPort: 443,
 *     policyNames: [wu_tang_ssl_tls_1_1.policyName],
 * });
 * ```
 * 
 * This example shows how to add a [Predefined Security Policy for ELBs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/load_balancer_listener_policy.html.markdown.
 */
/** @deprecated aws.elasticloadbalancing.ListenerPolicy has been deprecated in favour of aws.elb.ListenerPolicy */
export class ListenerPolicy extends pulumi.CustomResource {
    /**
     * Get an existing ListenerPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ListenerPolicyState, opts?: pulumi.CustomResourceOptions): ListenerPolicy {
        pulumi.log.warn("ListenerPolicy is deprecated: aws.elasticloadbalancing.ListenerPolicy has been deprecated in favour of aws.elb.ListenerPolicy")
        return new ListenerPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:elasticloadbalancing/listenerPolicy:ListenerPolicy';

    /**
     * Returns true if the given object is an instance of ListenerPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ListenerPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ListenerPolicy.__pulumiType;
    }

    /**
     * The load balancer to attach the policy to.
     */
    public readonly loadBalancerName!: pulumi.Output<string>;
    /**
     * The load balancer listener port to apply the policy to.
     */
    public readonly loadBalancerPort!: pulumi.Output<number>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    public readonly policyNames!: pulumi.Output<string[] | undefined>;

    /**
     * Create a ListenerPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated aws.elasticloadbalancing.ListenerPolicy has been deprecated in favour of aws.elb.ListenerPolicy */
    constructor(name: string, args: ListenerPolicyArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated aws.elasticloadbalancing.ListenerPolicy has been deprecated in favour of aws.elb.ListenerPolicy */
    constructor(name: string, argsOrState?: ListenerPolicyArgs | ListenerPolicyState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ListenerPolicy is deprecated: aws.elasticloadbalancing.ListenerPolicy has been deprecated in favour of aws.elb.ListenerPolicy")
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ListenerPolicyState | undefined;
            inputs["loadBalancerName"] = state ? state.loadBalancerName : undefined;
            inputs["loadBalancerPort"] = state ? state.loadBalancerPort : undefined;
            inputs["policyNames"] = state ? state.policyNames : undefined;
        } else {
            const args = argsOrState as ListenerPolicyArgs | undefined;
            if (!args || args.loadBalancerName === undefined) {
                throw new Error("Missing required property 'loadBalancerName'");
            }
            if (!args || args.loadBalancerPort === undefined) {
                throw new Error("Missing required property 'loadBalancerPort'");
            }
            inputs["loadBalancerName"] = args ? args.loadBalancerName : undefined;
            inputs["loadBalancerPort"] = args ? args.loadBalancerPort : undefined;
            inputs["policyNames"] = args ? args.policyNames : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ListenerPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ListenerPolicy resources.
 */
export interface ListenerPolicyState {
    /**
     * The load balancer to attach the policy to.
     */
    readonly loadBalancerName?: pulumi.Input<string>;
    /**
     * The load balancer listener port to apply the policy to.
     */
    readonly loadBalancerPort?: pulumi.Input<number>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    readonly policyNames?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a ListenerPolicy resource.
 */
export interface ListenerPolicyArgs {
    /**
     * The load balancer to attach the policy to.
     */
    readonly loadBalancerName: pulumi.Input<string>;
    /**
     * The load balancer listener port to apply the policy to.
     */
    readonly loadBalancerPort: pulumi.Input<number>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    readonly policyNames?: pulumi.Input<pulumi.Input<string>[]>;
}
