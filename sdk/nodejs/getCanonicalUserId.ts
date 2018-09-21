// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
 * for the effective account in which Terraform is working.
 */
export function getCanonicalUserId(opts?: pulumi.InvokeOptions): Promise<GetCanonicalUserIdResult> {
    return pulumi.runtime.invoke("aws:index/getCanonicalUserId:getCanonicalUserId", {
    }, opts);
}

/**
 * A collection of values returned by getCanonicalUserId.
 */
export interface GetCanonicalUserIdResult {
    /**
     * The human-friendly name linked to the canonical user ID.
     */
    readonly displayName: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}