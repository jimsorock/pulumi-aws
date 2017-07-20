// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class AmiFromInstance extends lumi.NamedResource implements AmiFromInstanceArgs {
    public /*out*/ readonly architecture: string;
    public readonly description?: string;
    public readonly ebsBlockDevice: { deleteOnTermination: boolean, deviceName: string, encrypted: boolean, iops: number, snapshotId: string, volumeSize: number, volumeType: string }[];
    public readonly ephemeralBlockDevice: { deviceName: string, virtualName: string }[];
    public /*out*/ readonly amiId: string;
    public /*out*/ readonly imageLocation: string;
    public /*out*/ readonly kernelId: string;
    public /*out*/ readonly manageEbsSnapshots: boolean;
    public readonly amiFromInstanceName?: string;
    public /*out*/ readonly ramdiskId: string;
    public /*out*/ readonly rootDeviceName: string;
    public readonly snapshotWithoutReboot?: boolean;
    public readonly sourceInstanceId: string;
    public /*out*/ readonly sriovNetSupport: string;
    public readonly tags?: {[key: string]: any};
    public /*out*/ readonly virtualizationType: string;

    constructor(name: string, args: AmiFromInstanceArgs) {
        super(name);
        this.description = args.description;
        this.ebsBlockDevice = args.ebsBlockDevice;
        this.ephemeralBlockDevice = args.ephemeralBlockDevice;
        this.amiFromInstanceName = args.amiFromInstanceName;
        this.snapshotWithoutReboot = args.snapshotWithoutReboot;
        if (lumirt.defaultIfComputed(args.sourceInstanceId, "") === undefined) {
            throw new Error("Property argument 'sourceInstanceId' is required, but was missing");
        }
        this.sourceInstanceId = args.sourceInstanceId;
        this.tags = args.tags;
    }
}

export interface AmiFromInstanceArgs {
    readonly description?: string;
    readonly ebsBlockDevice?: { deleteOnTermination: boolean, deviceName: string, encrypted: boolean, iops: number, snapshotId: string, volumeSize: number, volumeType: string }[];
    readonly ephemeralBlockDevice?: { deviceName: string, virtualName: string }[];
    readonly amiFromInstanceName?: string;
    readonly snapshotWithoutReboot?: boolean;
    readonly sourceInstanceId: string;
    readonly tags?: {[key: string]: any};
}
