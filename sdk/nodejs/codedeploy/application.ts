// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a CodeDeploy application to be used as a basis for deployments
 */
export class Application extends pulumi.CustomResource {
    /**
     * Get an existing Application resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState): Application {
        return new Application(name, <any>state, { id });
    }

    /**
     * The compute platform can either be `Server` or `Lambda`. Default is `Server`.
     */
    public readonly computePlatform: pulumi.Output<string | undefined>;
    /**
     * The name of the application.
     */
    public readonly name: pulumi.Output<string>;
    public readonly uniqueId: pulumi.Output<string>;

    /**
     * Create a Application resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationArgs | ApplicationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ApplicationState = argsOrState as ApplicationState | undefined;
            inputs["computePlatform"] = state ? state.computePlatform : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["uniqueId"] = state ? state.uniqueId : undefined;
        } else {
            const args = argsOrState as ApplicationArgs | undefined;
            inputs["computePlatform"] = args ? args.computePlatform : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["uniqueId"] = args ? args.uniqueId : undefined;
        }
        super("aws:codedeploy/application:Application", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Application resources.
 */
export interface ApplicationState {
    /**
     * The compute platform can either be `Server` or `Lambda`. Default is `Server`.
     */
    readonly computePlatform?: pulumi.Input<string>;
    /**
     * The name of the application.
     */
    readonly name?: pulumi.Input<string>;
    readonly uniqueId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Application resource.
 */
export interface ApplicationArgs {
    /**
     * The compute platform can either be `Server` or `Lambda`. Default is `Server`.
     */
    readonly computePlatform?: pulumi.Input<string>;
    /**
     * The name of the application.
     */
    readonly name?: pulumi.Input<string>;
    readonly uniqueId?: pulumi.Input<string>;
}