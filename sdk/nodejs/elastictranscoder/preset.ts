// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an Elastic Transcoder preset resource.
 */
export class Preset extends pulumi.CustomResource {
    /**
     * Get an existing Preset resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PresetState): Preset {
        return new Preset(name, <any>state, { id });
    }

    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * Audio parameters object (documented below).
     */
    public readonly audio: pulumi.Output<{ audioPackingMode?: string, bitRate?: string, channels?: string, codec?: string, sampleRate?: string } | undefined>;
    /**
     * Codec options for the audio parameters (documented below)
     */
    public readonly audioCodecOptions: pulumi.Output<{ bitDepth?: string, bitOrder?: string, profile?: string, signed?: string } | undefined>;
    /**
     * The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
     */
    public readonly container: pulumi.Output<string>;
    /**
     * A description of the preset (maximum 255 characters)
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The name of the preset. (maximum 40 characters)
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Thumbnail parameters object (documented below)
     */
    public readonly thumbnails: pulumi.Output<{ aspectRatio?: string, format?: string, interval?: string, maxHeight?: string, maxWidth?: string, paddingPolicy?: string, resolution?: string, sizingPolicy?: string } | undefined>;
    public readonly type: pulumi.Output<string>;
    /**
     * Video parameters object (documented below)
     */
    public readonly video: pulumi.Output<{ aspectRatio?: string, bitRate?: string, codec?: string, displayAspectRatio?: string, fixedGop?: string, frameRate?: string, keyframesMaxDist?: string, maxFrameRate?: string, maxHeight?: string, maxWidth?: string, paddingPolicy?: string, resolution?: string, sizingPolicy?: string } | undefined>;
    public readonly videoCodecOptions: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Watermark parameters for the video parameters (documented below)
     * * `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
     */
    public readonly videoWatermarks: pulumi.Output<{ horizontalAlign?: string, horizontalOffset?: string, id?: string, maxHeight?: string, maxWidth?: string, opacity?: string, sizingPolicy?: string, target?: string, verticalAlign?: string, verticalOffset?: string }[] | undefined>;

    /**
     * Create a Preset resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PresetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PresetArgs | PresetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PresetState = argsOrState as PresetState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["audio"] = state ? state.audio : undefined;
            inputs["audioCodecOptions"] = state ? state.audioCodecOptions : undefined;
            inputs["container"] = state ? state.container : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["thumbnails"] = state ? state.thumbnails : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["video"] = state ? state.video : undefined;
            inputs["videoCodecOptions"] = state ? state.videoCodecOptions : undefined;
            inputs["videoWatermarks"] = state ? state.videoWatermarks : undefined;
        } else {
            const args = argsOrState as PresetArgs | undefined;
            if (!args || args.container === undefined) {
                throw new Error("Missing required property 'container'");
            }
            inputs["audio"] = args ? args.audio : undefined;
            inputs["audioCodecOptions"] = args ? args.audioCodecOptions : undefined;
            inputs["container"] = args ? args.container : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["thumbnails"] = args ? args.thumbnails : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["video"] = args ? args.video : undefined;
            inputs["videoCodecOptions"] = args ? args.videoCodecOptions : undefined;
            inputs["videoWatermarks"] = args ? args.videoWatermarks : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:elastictranscoder/preset:Preset", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Preset resources.
 */
export interface PresetState {
    readonly arn?: pulumi.Input<string>;
    /**
     * Audio parameters object (documented below).
     */
    readonly audio?: pulumi.Input<{ audioPackingMode?: pulumi.Input<string>, bitRate?: pulumi.Input<string>, channels?: pulumi.Input<string>, codec?: pulumi.Input<string>, sampleRate?: pulumi.Input<string> }>;
    /**
     * Codec options for the audio parameters (documented below)
     */
    readonly audioCodecOptions?: pulumi.Input<{ bitDepth?: pulumi.Input<string>, bitOrder?: pulumi.Input<string>, profile?: pulumi.Input<string>, signed?: pulumi.Input<string> }>;
    /**
     * The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
     */
    readonly container?: pulumi.Input<string>;
    /**
     * A description of the preset (maximum 255 characters)
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the preset. (maximum 40 characters)
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Thumbnail parameters object (documented below)
     */
    readonly thumbnails?: pulumi.Input<{ aspectRatio?: pulumi.Input<string>, format?: pulumi.Input<string>, interval?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, paddingPolicy?: pulumi.Input<string>, resolution?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string> }>;
    readonly type?: pulumi.Input<string>;
    /**
     * Video parameters object (documented below)
     */
    readonly video?: pulumi.Input<{ aspectRatio?: pulumi.Input<string>, bitRate?: pulumi.Input<string>, codec?: pulumi.Input<string>, displayAspectRatio?: pulumi.Input<string>, fixedGop?: pulumi.Input<string>, frameRate?: pulumi.Input<string>, keyframesMaxDist?: pulumi.Input<string>, maxFrameRate?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, paddingPolicy?: pulumi.Input<string>, resolution?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string> }>;
    readonly videoCodecOptions?: pulumi.Input<{[key: string]: any}>;
    /**
     * Watermark parameters for the video parameters (documented below)
     * * `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
     */
    readonly videoWatermarks?: pulumi.Input<pulumi.Input<{ horizontalAlign?: pulumi.Input<string>, horizontalOffset?: pulumi.Input<string>, id?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, opacity?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string>, target?: pulumi.Input<string>, verticalAlign?: pulumi.Input<string>, verticalOffset?: pulumi.Input<string> }>[]>;
}

/**
 * The set of arguments for constructing a Preset resource.
 */
export interface PresetArgs {
    /**
     * Audio parameters object (documented below).
     */
    readonly audio?: pulumi.Input<{ audioPackingMode?: pulumi.Input<string>, bitRate?: pulumi.Input<string>, channels?: pulumi.Input<string>, codec?: pulumi.Input<string>, sampleRate?: pulumi.Input<string> }>;
    /**
     * Codec options for the audio parameters (documented below)
     */
    readonly audioCodecOptions?: pulumi.Input<{ bitDepth?: pulumi.Input<string>, bitOrder?: pulumi.Input<string>, profile?: pulumi.Input<string>, signed?: pulumi.Input<string> }>;
    /**
     * The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
     */
    readonly container: pulumi.Input<string>;
    /**
     * A description of the preset (maximum 255 characters)
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the preset. (maximum 40 characters)
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Thumbnail parameters object (documented below)
     */
    readonly thumbnails?: pulumi.Input<{ aspectRatio?: pulumi.Input<string>, format?: pulumi.Input<string>, interval?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, paddingPolicy?: pulumi.Input<string>, resolution?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string> }>;
    readonly type?: pulumi.Input<string>;
    /**
     * Video parameters object (documented below)
     */
    readonly video?: pulumi.Input<{ aspectRatio?: pulumi.Input<string>, bitRate?: pulumi.Input<string>, codec?: pulumi.Input<string>, displayAspectRatio?: pulumi.Input<string>, fixedGop?: pulumi.Input<string>, frameRate?: pulumi.Input<string>, keyframesMaxDist?: pulumi.Input<string>, maxFrameRate?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, paddingPolicy?: pulumi.Input<string>, resolution?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string> }>;
    readonly videoCodecOptions?: pulumi.Input<{[key: string]: any}>;
    /**
     * Watermark parameters for the video parameters (documented below)
     * * `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
     */
    readonly videoWatermarks?: pulumi.Input<pulumi.Input<{ horizontalAlign?: pulumi.Input<string>, horizontalOffset?: pulumi.Input<string>, id?: pulumi.Input<string>, maxHeight?: pulumi.Input<string>, maxWidth?: pulumi.Input<string>, opacity?: pulumi.Input<string>, sizingPolicy?: pulumi.Input<string>, target?: pulumi.Input<string>, verticalAlign?: pulumi.Input<string>, verticalOffset?: pulumi.Input<string> }>[]>;
}