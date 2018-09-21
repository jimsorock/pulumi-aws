// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The VPC Peering Connection data source provides details about
 * a specific VPC peering connection.
 */
export function getVpcPeeringConnection(args?: GetVpcPeeringConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcPeeringConnectionResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:ec2/getVpcPeeringConnection:getVpcPeeringConnection", {
        "cidrBlock": args.cidrBlock,
        "filters": args.filters,
        "id": args.id,
        "ownerId": args.ownerId,
        "peerCidrBlock": args.peerCidrBlock,
        "peerOwnerId": args.peerOwnerId,
        "peerRegion": args.peerRegion,
        "peerVpcId": args.peerVpcId,
        "region": args.region,
        "status": args.status,
        "tags": args.tags,
        "vpcId": args.vpcId,
    }, opts);
}

/**
 * A collection of arguments for invoking getVpcPeeringConnection.
 */
export interface GetVpcPeeringConnectionArgs {
    /**
     * The CIDR block of the requester VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly cidrBlock?: string;
    /**
     * Custom filter block as described below.
     */
    readonly filters?: { name: string, values: string[] }[];
    /**
     * The ID of the specific VPC Peering Connection to retrieve.
     */
    readonly id?: string;
    /**
     * The AWS account ID of the owner of the requester VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly ownerId?: string;
    /**
     * The CIDR block of the accepter VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly peerCidrBlock?: string;
    /**
     * The AWS account ID of the owner of the accepter VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly peerOwnerId?: string;
    /**
     * The region of the accepter VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly peerRegion?: string;
    /**
     * The ID of the accepter VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly peerVpcId?: string;
    /**
     * The region of the requester VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly region?: string;
    /**
     * The status of the specific VPC Peering Connection to retrieve.
     */
    readonly status?: string;
    /**
     * A mapping of tags, each pair of which must exactly match
     * a pair on the desired VPC Peering Connection.
     */
    readonly tags?: {[key: string]: any};
    /**
     * The ID of the requester VPC of the specific VPC Peering Connection to retrieve.
     */
    readonly vpcId?: string;
}

/**
 * A collection of values returned by getVpcPeeringConnection.
 */
export interface GetVpcPeeringConnectionResult {
    /**
     * A configuration block that describes [VPC Peering Connection]
     * (http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
     */
    readonly accepter: {[key: string]: boolean};
    readonly cidrBlock: string;
    readonly id: string;
    readonly ownerId: string;
    readonly peerCidrBlock: string;
    readonly peerOwnerId: string;
    readonly peerRegion: string;
    readonly peerVpcId: string;
    readonly region: string;
    /**
     * A configuration block that describes [VPC Peering Connection]
     * (http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
     */
    readonly requester: {[key: string]: boolean};
    readonly status: string;
    readonly tags: {[key: string]: any};
    readonly vpcId: string;
}