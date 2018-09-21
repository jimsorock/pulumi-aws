// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to manage a GuardDuty ThreatIntelSet.
 * 
 * ~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)
 */
export class ThreatIntelSet extends pulumi.CustomResource {
    /**
     * Get an existing ThreatIntelSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThreatIntelSetState): ThreatIntelSet {
        return new ThreatIntelSet(name, <any>state, { id });
    }

    /**
     * Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
     */
    public readonly activate: pulumi.Output<boolean>;
    /**
     * The detector ID of the GuardDuty.
     */
    public readonly detectorId: pulumi.Output<string>;
    /**
     * The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
     */
    public readonly format: pulumi.Output<string>;
    /**
     * The URI of the file that contains the ThreatIntelSet.
     */
    public readonly location: pulumi.Output<string>;
    /**
     * The friendly name to identify the ThreatIntelSet.
     */
    public readonly name: pulumi.Output<string>;

    /**
     * Create a ThreatIntelSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ThreatIntelSetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ThreatIntelSetArgs | ThreatIntelSetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ThreatIntelSetState = argsOrState as ThreatIntelSetState | undefined;
            inputs["activate"] = state ? state.activate : undefined;
            inputs["detectorId"] = state ? state.detectorId : undefined;
            inputs["format"] = state ? state.format : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as ThreatIntelSetArgs | undefined;
            if (!args || args.activate === undefined) {
                throw new Error("Missing required property 'activate'");
            }
            if (!args || args.detectorId === undefined) {
                throw new Error("Missing required property 'detectorId'");
            }
            if (!args || args.format === undefined) {
                throw new Error("Missing required property 'format'");
            }
            if (!args || args.location === undefined) {
                throw new Error("Missing required property 'location'");
            }
            inputs["activate"] = args ? args.activate : undefined;
            inputs["detectorId"] = args ? args.detectorId : undefined;
            inputs["format"] = args ? args.format : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
        }
        super("aws:glacier/threatIntelSet:ThreatIntelSet", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ThreatIntelSet resources.
 */
export interface ThreatIntelSetState {
    /**
     * Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
     */
    readonly activate?: pulumi.Input<boolean>;
    /**
     * The detector ID of the GuardDuty.
     */
    readonly detectorId?: pulumi.Input<string>;
    /**
     * The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
     */
    readonly format?: pulumi.Input<string>;
    /**
     * The URI of the file that contains the ThreatIntelSet.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The friendly name to identify the ThreatIntelSet.
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ThreatIntelSet resource.
 */
export interface ThreatIntelSetArgs {
    /**
     * Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
     */
    readonly activate: pulumi.Input<boolean>;
    /**
     * The detector ID of the GuardDuty.
     */
    readonly detectorId: pulumi.Input<string>;
    /**
     * The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
     */
    readonly format: pulumi.Input<string>;
    /**
     * The URI of the file that contains the ThreatIntelSet.
     */
    readonly location: pulumi.Input<string>;
    /**
     * The friendly name to identify the ThreatIntelSet.
     */
    readonly name?: pulumi.Input<string>;
}