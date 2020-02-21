// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * `aws.ec2.getSubnetIds` provides a set of ids for a vpcId
 * 
 * This resource can be useful for getting back a set of subnet ids for a vpc.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/subnet_ids.html.markdown.
 */
export function getSubnetIds(args: GetSubnetIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetIdsResult> & GetSubnetIdsResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetSubnetIdsResult> = pulumi.runtime.invoke("aws:ec2/getSubnetIds:getSubnetIds", {
        "filters": args.filters,
        "tags": args.tags,
        "vpcId": args.vpcId,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getSubnetIds.
 */
export interface GetSubnetIdsArgs {
    /**
     * Custom filter block as described below.
     */
    readonly filters?: inputs.ec2.GetSubnetIdsFilter[];
    /**
     * A mapping of tags, each pair of which must exactly match
     * a pair on the desired subnets.
     */
    readonly tags?: {[key: string]: any};
    /**
     * The VPC ID that you want to filter from.
     */
    readonly vpcId: string;
}

/**
 * A collection of values returned by getSubnetIds.
 */
export interface GetSubnetIdsResult {
    readonly filters?: outputs.ec2.GetSubnetIdsFilter[];
    /**
     * A set of all the subnet ids found. This data source will fail if none are found.
     */
    readonly ids: string[];
    readonly tags: {[key: string]: any};
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
