// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Tags} from "../index";

/**
 * Creates a Snapshot of an EBS Volume.
 */
export class Snapshot extends pulumi.CustomResource {
    /**
     * Get an existing Snapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState): Snapshot {
        return new Snapshot(name, <any>state, { id });
    }

    /**
     * The data encryption key identifier for the snapshot.
     */
    public /*out*/ readonly dataEncryptionKeyId: pulumi.Output<string>;
    /**
     * A description of what the snapshot is.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * Whether the snapshot is encrypted.
     */
    public /*out*/ readonly encrypted: pulumi.Output<boolean>;
    /**
     * The ARN for the KMS encryption key.
     */
    public /*out*/ readonly kmsKeyId: pulumi.Output<string>;
    /**
     * Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
     */
    public /*out*/ readonly ownerAlias: pulumi.Output<string>;
    /**
     * The AWS account ID of the EBS snapshot owner.
     */
    public /*out*/ readonly ownerId: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the snapshot
     */
    public readonly tags: pulumi.Output<Tags | undefined>;
    /**
     * The Volume ID of which to make a snapshot.
     */
    public readonly volumeId: pulumi.Output<string>;
    /**
     * The size of the drive in GiBs.
     */
    public /*out*/ readonly volumeSize: pulumi.Output<number>;

    /**
     * Create a Snapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SnapshotArgs | SnapshotState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SnapshotState = argsOrState as SnapshotState | undefined;
            inputs["dataEncryptionKeyId"] = state ? state.dataEncryptionKeyId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["encrypted"] = state ? state.encrypted : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["ownerAlias"] = state ? state.ownerAlias : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["volumeId"] = state ? state.volumeId : undefined;
            inputs["volumeSize"] = state ? state.volumeSize : undefined;
        } else {
            const args = argsOrState as SnapshotArgs | undefined;
            if (!args || args.volumeId === undefined) {
                throw new Error("Missing required property 'volumeId'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["volumeId"] = args ? args.volumeId : undefined;
            inputs["dataEncryptionKeyId"] = undefined /*out*/;
            inputs["encrypted"] = undefined /*out*/;
            inputs["kmsKeyId"] = undefined /*out*/;
            inputs["ownerAlias"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
            inputs["volumeSize"] = undefined /*out*/;
        }
        super("aws:ebs/snapshot:Snapshot", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Snapshot resources.
 */
export interface SnapshotState {
    /**
     * The data encryption key identifier for the snapshot.
     */
    readonly dataEncryptionKeyId?: pulumi.Input<string>;
    /**
     * A description of what the snapshot is.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether the snapshot is encrypted.
     */
    readonly encrypted?: pulumi.Input<boolean>;
    /**
     * The ARN for the KMS encryption key.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
     */
    readonly ownerAlias?: pulumi.Input<string>;
    /**
     * The AWS account ID of the EBS snapshot owner.
     */
    readonly ownerId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the snapshot
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * The Volume ID of which to make a snapshot.
     */
    readonly volumeId?: pulumi.Input<string>;
    /**
     * The size of the drive in GiBs.
     */
    readonly volumeSize?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Snapshot resource.
 */
export interface SnapshotArgs {
    /**
     * A description of what the snapshot is.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the snapshot
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * The Volume ID of which to make a snapshot.
     */
    readonly volumeId: pulumi.Input<string>;
}