// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an SSM Maintenance Window resource
 */
export class MaintenanceWindow extends pulumi.CustomResource {
    /**
     * Get an existing MaintenanceWindow resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowState): MaintenanceWindow {
        return new MaintenanceWindow(name, <any>state, { id });
    }

    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    public readonly allowUnassociatedTargets: pulumi.Output<boolean | undefined>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    public readonly cutoff: pulumi.Output<number>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    public readonly duration: pulumi.Output<number>;
    public readonly enabled: pulumi.Output<boolean | undefined>;
    /**
     * The name of the maintenance window.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    public readonly schedule: pulumi.Output<string>;

    /**
     * Create a MaintenanceWindow resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MaintenanceWindowArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MaintenanceWindowArgs | MaintenanceWindowState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: MaintenanceWindowState = argsOrState as MaintenanceWindowState | undefined;
            inputs["allowUnassociatedTargets"] = state ? state.allowUnassociatedTargets : undefined;
            inputs["cutoff"] = state ? state.cutoff : undefined;
            inputs["duration"] = state ? state.duration : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["schedule"] = state ? state.schedule : undefined;
        } else {
            const args = argsOrState as MaintenanceWindowArgs | undefined;
            if (!args || args.cutoff === undefined) {
                throw new Error("Missing required property 'cutoff'");
            }
            if (!args || args.duration === undefined) {
                throw new Error("Missing required property 'duration'");
            }
            if (!args || args.schedule === undefined) {
                throw new Error("Missing required property 'schedule'");
            }
            inputs["allowUnassociatedTargets"] = args ? args.allowUnassociatedTargets : undefined;
            inputs["cutoff"] = args ? args.cutoff : undefined;
            inputs["duration"] = args ? args.duration : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
        }
        super("aws:ssm/maintenanceWindow:MaintenanceWindow", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MaintenanceWindow resources.
 */
export interface MaintenanceWindowState {
    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    readonly allowUnassociatedTargets?: pulumi.Input<boolean>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    readonly cutoff?: pulumi.Input<number>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    readonly duration?: pulumi.Input<number>;
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the maintenance window.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    readonly schedule?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MaintenanceWindow resource.
 */
export interface MaintenanceWindowArgs {
    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    readonly allowUnassociatedTargets?: pulumi.Input<boolean>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    readonly cutoff: pulumi.Input<number>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    readonly duration: pulumi.Input<number>;
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the maintenance window.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    readonly schedule: pulumi.Input<string>;
}