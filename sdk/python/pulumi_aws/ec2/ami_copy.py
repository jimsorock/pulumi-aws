# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class AmiCopy(pulumi.CustomResource):
    """
    The "AMI copy" resource allows duplication of an Amazon Machine Image (AMI),
    including cross-region copies.
    
    If the source AMI has associated EBS snapshots, those will also be duplicated
    along with the AMI.
    
    This is useful for taking a single AMI provisioned in one region and making
    it available in another for a multi-region deployment.
    
    Copying an AMI can take several minutes. The creation of this resource will
    block until the new AMI is available for use on new instances.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, ebs_block_devices=None, encrypted=None, ephemeral_block_devices=None, kms_key_id=None, name=None, source_ami_id=None, source_ami_region=None, tags=None):
        """Create a AmiCopy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A longer, human-readable description for the AMI.
        """
        __props__['description'] = description

        if ebs_block_devices and not isinstance(ebs_block_devices, list):
            raise TypeError('Expected property ebs_block_devices to be a list')
        __self__.ebs_block_devices = ebs_block_devices
        """
        Nested block describing an EBS block device that should be
        attached to created instances. The structure of this block is described below.
        """
        __props__['ebsBlockDevices'] = ebs_block_devices

        if encrypted and not isinstance(encrypted, bool):
            raise TypeError('Expected property encrypted to be a bool')
        __self__.encrypted = encrypted
        """
        Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
        """
        __props__['encrypted'] = encrypted

        if ephemeral_block_devices and not isinstance(ephemeral_block_devices, list):
            raise TypeError('Expected property ephemeral_block_devices to be a list')
        __self__.ephemeral_block_devices = ephemeral_block_devices
        """
        Nested block describing an ephemeral block device that
        should be attached to created instances. The structure of this block is described below.
        """
        __props__['ephemeralBlockDevices'] = ephemeral_block_devices

        if kms_key_id and not isinstance(kms_key_id, basestring):
            raise TypeError('Expected property kms_key_id to be a basestring')
        __self__.kms_key_id = kms_key_id
        """
        The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
        """
        __props__['kmsKeyId'] = kms_key_id

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A region-unique name for the AMI.
        """
        __props__['name'] = name

        if not source_ami_id:
            raise TypeError('Missing required property source_ami_id')
        elif not isinstance(source_ami_id, basestring):
            raise TypeError('Expected property source_ami_id to be a basestring')
        __self__.source_ami_id = source_ami_id
        """
        The id of the AMI to copy. This id must be valid in the region
        given by `source_ami_region`.
        """
        __props__['sourceAmiId'] = source_ami_id

        if not source_ami_region:
            raise TypeError('Missing required property source_ami_region')
        elif not isinstance(source_ami_region, basestring):
            raise TypeError('Expected property source_ami_region to be a basestring')
        __self__.source_ami_region = source_ami_region
        """
        The region from which the AMI will be copied. This may be the
        same as the AWS provider region in order to create a copy within the same region.
        """
        __props__['sourceAmiRegion'] = source_ami_region

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        __props__['tags'] = tags

        __self__.architecture = pulumi.runtime.UNKNOWN
        """
        Machine architecture for created instances. Defaults to "x86_64".
        """
        __self__.ena_support = pulumi.runtime.UNKNOWN
        """
        Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        """
        __self__.image_location = pulumi.runtime.UNKNOWN
        """
        Path to an S3 object containing an image manifest, e.g. created
        by the `ec2-upload-bundle` command in the EC2 command line tools.
        """
        __self__.kernel_id = pulumi.runtime.UNKNOWN
        """
        The id of the kernel image (AKI) that will be used as the paravirtual
        kernel in created instances.
        """
        __self__.manage_ebs_snapshots = pulumi.runtime.UNKNOWN
        __self__.ramdisk_id = pulumi.runtime.UNKNOWN
        """
        The id of an initrd image (ARI) that will be used when booting the
        created instances.
        """
        __self__.root_device_name = pulumi.runtime.UNKNOWN
        """
        The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        """
        __self__.root_snapshot_id = pulumi.runtime.UNKNOWN
        __self__.sriov_net_support = pulumi.runtime.UNKNOWN
        """
        When set to "simple" (the default), enables enhanced networking
        for created instances. No other value is supported at this time.
        """
        __self__.virtualization_type = pulumi.runtime.UNKNOWN
        """
        Keyword to choose what virtualization mode created instances
        will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
        changes the set of further arguments that are required, as described below.
        """

        super(AmiCopy, __self__).__init__(
            'aws:ec2/amiCopy:AmiCopy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'architecture' in outs:
            self.architecture = outs['architecture']
        if 'description' in outs:
            self.description = outs['description']
        if 'ebsBlockDevices' in outs:
            self.ebs_block_devices = outs['ebsBlockDevices']
        if 'enaSupport' in outs:
            self.ena_support = outs['enaSupport']
        if 'encrypted' in outs:
            self.encrypted = outs['encrypted']
        if 'ephemeralBlockDevices' in outs:
            self.ephemeral_block_devices = outs['ephemeralBlockDevices']
        if 'imageLocation' in outs:
            self.image_location = outs['imageLocation']
        if 'kernelId' in outs:
            self.kernel_id = outs['kernelId']
        if 'kmsKeyId' in outs:
            self.kms_key_id = outs['kmsKeyId']
        if 'manageEbsSnapshots' in outs:
            self.manage_ebs_snapshots = outs['manageEbsSnapshots']
        if 'name' in outs:
            self.name = outs['name']
        if 'ramdiskId' in outs:
            self.ramdisk_id = outs['ramdiskId']
        if 'rootDeviceName' in outs:
            self.root_device_name = outs['rootDeviceName']
        if 'rootSnapshotId' in outs:
            self.root_snapshot_id = outs['rootSnapshotId']
        if 'sourceAmiId' in outs:
            self.source_ami_id = outs['sourceAmiId']
        if 'sourceAmiRegion' in outs:
            self.source_ami_region = outs['sourceAmiRegion']
        if 'sriovNetSupport' in outs:
            self.sriov_net_support = outs['sriovNetSupport']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'virtualizationType' in outs:
            self.virtualization_type = outs['virtualizationType']