// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package emr

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an Elastic MapReduce Cluster, a web service that makes it easy to
// process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
// for more information.
//
// To configure [Instance Groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for [task nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-task), see the [`emr.InstanceGroup` resource](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html).
//
// > Support for [Instance Fleets](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-fleets) will be made available in an upcoming release.
type Cluster struct {
	pulumi.CustomResourceState

	// A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.
	AdditionalInfo pulumi.StringPtrOutput `pulumi:"additionalInfo"`
	// A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
	Applications pulumi.StringArrayOutput `pulumi:"applications"`
	Arn          pulumi.StringOutput      `pulumi:"arn"`
	// An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
	AutoscalingRole pulumi.StringPtrOutput `pulumi:"autoscalingRole"`
	// Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.
	BootstrapActions ClusterBootstrapActionArrayOutput `pulumi:"bootstrapActions"`
	ClusterState     pulumi.StringOutput               `pulumi:"clusterState"`
	// List of configurations supplied for the EMR cluster you are creating
	Configurations pulumi.StringPtrOutput `pulumi:"configurations"`
	// A JSON string for supplying list of configurations for the EMR cluster.
	ConfigurationsJson pulumi.StringPtrOutput `pulumi:"configurationsJson"`
	// Use the `coreInstanceGroup` configuration block `instanceCount` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`coreInstanceCount`-1) as core nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set. Default `1`
	//
	// Deprecated: use `core_instance_group` configuration block `instance_count` argument instead
	CoreInstanceCount pulumi.IntOutput `pulumi:"coreInstanceCount"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core). Cannot be specified if `coreInstanceCount` argument, `coreInstanceType` argument, or `instanceGroup` configuration blocks are set. Detailed below.
	CoreInstanceGroup ClusterCoreInstanceGroupOutput `pulumi:"coreInstanceGroup"`
	// Use the `coreInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `core_instance_group` configuration block `instance_type` argument instead
	CoreInstanceType pulumi.StringOutput `pulumi:"coreInstanceType"`
	// A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
	CustomAmiId pulumi.StringPtrOutput `pulumi:"customAmiId"`
	// Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
	EbsRootVolumeSize pulumi.IntPtrOutput `pulumi:"ebsRootVolumeSize"`
	// Attributes for the EC2 instances running the job flow. Defined below
	Ec2Attributes ClusterEc2AttributesPtrOutput `pulumi:"ec2Attributes"`
	// Use the `masterInstanceGroup` configuration block, `coreInstanceGroup` configuration block and [`emr.InstanceGroup` resource(s)](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) instead. A list of `instanceGroup` objects for each instance group in the cluster. Exactly one of `masterInstanceType` and `instanceGroup` must be specified. If `instanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Cannot be specified if `masterInstanceGroup` or `coreInstanceGroup` configuration blocks are set. Defined below
	//
	// Deprecated: use `master_instance_group` configuration block, `core_instance_group` configuration block, and `aws_emr_instance_group` resource(s) instead
	InstanceGroups ClusterInstanceGroupArrayOutput `pulumi:"instanceGroups"`
	// Switch on/off run cluster with no steps or when all steps are complete (default is on)
	KeepJobFlowAliveWhenNoSteps pulumi.BoolOutput `pulumi:"keepJobFlowAliveWhenNoSteps"`
	// Kerberos configuration for the cluster. Defined below
	KerberosAttributes ClusterKerberosAttributesPtrOutput `pulumi:"kerberosAttributes"`
	// S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
	LogUri pulumi.StringPtrOutput `pulumi:"logUri"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master). Cannot be specified if `masterInstanceType` argument or `instanceGroup` configuration blocks are set. Detailed below.
	MasterInstanceGroup ClusterMasterInstanceGroupOutput `pulumi:"masterInstanceGroup"`
	// Use the `masterInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the master node. Cannot be specified if `masterInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `master_instance_group` configuration block `instance_type` argument instead
	MasterInstanceType pulumi.StringOutput `pulumi:"masterInstanceType"`
	// The public DNS name of the master EC2 instance.
	// * `core_instance_group.0.id` - Core node type Instance Group ID, if using Instance Group for this node type.
	MasterPublicDns pulumi.StringOutput `pulumi:"masterPublicDns"`
	// The name of the step.
	Name pulumi.StringOutput `pulumi:"name"`
	// The release label for the Amazon EMR release
	ReleaseLabel pulumi.StringOutput `pulumi:"releaseLabel"`
	// The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
	ScaleDownBehavior pulumi.StringOutput `pulumi:"scaleDownBehavior"`
	// The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `releaseLabel` 4.8.0 or greater
	SecurityConfiguration pulumi.StringPtrOutput `pulumi:"securityConfiguration"`
	// IAM role that will be assumed by the Amazon EMR service to access AWS resources
	ServiceRole pulumi.StringOutput `pulumi:"serviceRole"`
	// The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `releaseLabel` 5.28.0 or greater. (default is 1)
	StepConcurrencyLevel pulumi.IntPtrOutput `pulumi:"stepConcurrencyLevel"`
	// List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) if other steps are being managed outside of this provider.
	Steps ClusterStepArrayOutput `pulumi:"steps"`
	// list of tags to apply to the EMR Cluster
	Tags pulumi.MapOutput `pulumi:"tags"`
	// Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.
	TerminationProtection pulumi.BoolOutput `pulumi:"terminationProtection"`
	// Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
	VisibleToAllUsers pulumi.BoolPtrOutput `pulumi:"visibleToAllUsers"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil || args.ReleaseLabel == nil {
		return nil, errors.New("missing required argument 'ReleaseLabel'")
	}
	if args == nil || args.ServiceRole == nil {
		return nil, errors.New("missing required argument 'ServiceRole'")
	}
	if args == nil {
		args = &ClusterArgs{}
	}
	var resource Cluster
	err := ctx.RegisterResource("aws:emr/cluster:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("aws:emr/cluster:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
	// A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.
	AdditionalInfo *string `pulumi:"additionalInfo"`
	// A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
	Applications []string `pulumi:"applications"`
	Arn          *string  `pulumi:"arn"`
	// An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
	AutoscalingRole *string `pulumi:"autoscalingRole"`
	// Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.
	BootstrapActions []ClusterBootstrapAction `pulumi:"bootstrapActions"`
	ClusterState     *string                  `pulumi:"clusterState"`
	// List of configurations supplied for the EMR cluster you are creating
	Configurations *string `pulumi:"configurations"`
	// A JSON string for supplying list of configurations for the EMR cluster.
	ConfigurationsJson *string `pulumi:"configurationsJson"`
	// Use the `coreInstanceGroup` configuration block `instanceCount` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`coreInstanceCount`-1) as core nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set. Default `1`
	//
	// Deprecated: use `core_instance_group` configuration block `instance_count` argument instead
	CoreInstanceCount *int `pulumi:"coreInstanceCount"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core). Cannot be specified if `coreInstanceCount` argument, `coreInstanceType` argument, or `instanceGroup` configuration blocks are set. Detailed below.
	CoreInstanceGroup *ClusterCoreInstanceGroup `pulumi:"coreInstanceGroup"`
	// Use the `coreInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `core_instance_group` configuration block `instance_type` argument instead
	CoreInstanceType *string `pulumi:"coreInstanceType"`
	// A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
	CustomAmiId *string `pulumi:"customAmiId"`
	// Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
	EbsRootVolumeSize *int `pulumi:"ebsRootVolumeSize"`
	// Attributes for the EC2 instances running the job flow. Defined below
	Ec2Attributes *ClusterEc2Attributes `pulumi:"ec2Attributes"`
	// Use the `masterInstanceGroup` configuration block, `coreInstanceGroup` configuration block and [`emr.InstanceGroup` resource(s)](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) instead. A list of `instanceGroup` objects for each instance group in the cluster. Exactly one of `masterInstanceType` and `instanceGroup` must be specified. If `instanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Cannot be specified if `masterInstanceGroup` or `coreInstanceGroup` configuration blocks are set. Defined below
	//
	// Deprecated: use `master_instance_group` configuration block, `core_instance_group` configuration block, and `aws_emr_instance_group` resource(s) instead
	InstanceGroups []ClusterInstanceGroup `pulumi:"instanceGroups"`
	// Switch on/off run cluster with no steps or when all steps are complete (default is on)
	KeepJobFlowAliveWhenNoSteps *bool `pulumi:"keepJobFlowAliveWhenNoSteps"`
	// Kerberos configuration for the cluster. Defined below
	KerberosAttributes *ClusterKerberosAttributes `pulumi:"kerberosAttributes"`
	// S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
	LogUri *string `pulumi:"logUri"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master). Cannot be specified if `masterInstanceType` argument or `instanceGroup` configuration blocks are set. Detailed below.
	MasterInstanceGroup *ClusterMasterInstanceGroup `pulumi:"masterInstanceGroup"`
	// Use the `masterInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the master node. Cannot be specified if `masterInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `master_instance_group` configuration block `instance_type` argument instead
	MasterInstanceType *string `pulumi:"masterInstanceType"`
	// The public DNS name of the master EC2 instance.
	// * `core_instance_group.0.id` - Core node type Instance Group ID, if using Instance Group for this node type.
	MasterPublicDns *string `pulumi:"masterPublicDns"`
	// The name of the step.
	Name *string `pulumi:"name"`
	// The release label for the Amazon EMR release
	ReleaseLabel *string `pulumi:"releaseLabel"`
	// The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
	ScaleDownBehavior *string `pulumi:"scaleDownBehavior"`
	// The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `releaseLabel` 4.8.0 or greater
	SecurityConfiguration *string `pulumi:"securityConfiguration"`
	// IAM role that will be assumed by the Amazon EMR service to access AWS resources
	ServiceRole *string `pulumi:"serviceRole"`
	// The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `releaseLabel` 5.28.0 or greater. (default is 1)
	StepConcurrencyLevel *int `pulumi:"stepConcurrencyLevel"`
	// List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) if other steps are being managed outside of this provider.
	Steps []ClusterStep `pulumi:"steps"`
	// list of tags to apply to the EMR Cluster
	Tags map[string]interface{} `pulumi:"tags"`
	// Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.
	TerminationProtection *bool `pulumi:"terminationProtection"`
	// Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
	VisibleToAllUsers *bool `pulumi:"visibleToAllUsers"`
}

type ClusterState struct {
	// A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.
	AdditionalInfo pulumi.StringPtrInput
	// A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
	Applications pulumi.StringArrayInput
	Arn          pulumi.StringPtrInput
	// An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
	AutoscalingRole pulumi.StringPtrInput
	// Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.
	BootstrapActions ClusterBootstrapActionArrayInput
	ClusterState     pulumi.StringPtrInput
	// List of configurations supplied for the EMR cluster you are creating
	Configurations pulumi.StringPtrInput
	// A JSON string for supplying list of configurations for the EMR cluster.
	ConfigurationsJson pulumi.StringPtrInput
	// Use the `coreInstanceGroup` configuration block `instanceCount` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`coreInstanceCount`-1) as core nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set. Default `1`
	//
	// Deprecated: use `core_instance_group` configuration block `instance_count` argument instead
	CoreInstanceCount pulumi.IntPtrInput
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core). Cannot be specified if `coreInstanceCount` argument, `coreInstanceType` argument, or `instanceGroup` configuration blocks are set. Detailed below.
	CoreInstanceGroup ClusterCoreInstanceGroupPtrInput
	// Use the `coreInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `core_instance_group` configuration block `instance_type` argument instead
	CoreInstanceType pulumi.StringPtrInput
	// A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
	CustomAmiId pulumi.StringPtrInput
	// Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
	EbsRootVolumeSize pulumi.IntPtrInput
	// Attributes for the EC2 instances running the job flow. Defined below
	Ec2Attributes ClusterEc2AttributesPtrInput
	// Use the `masterInstanceGroup` configuration block, `coreInstanceGroup` configuration block and [`emr.InstanceGroup` resource(s)](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) instead. A list of `instanceGroup` objects for each instance group in the cluster. Exactly one of `masterInstanceType` and `instanceGroup` must be specified. If `instanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Cannot be specified if `masterInstanceGroup` or `coreInstanceGroup` configuration blocks are set. Defined below
	//
	// Deprecated: use `master_instance_group` configuration block, `core_instance_group` configuration block, and `aws_emr_instance_group` resource(s) instead
	InstanceGroups ClusterInstanceGroupArrayInput
	// Switch on/off run cluster with no steps or when all steps are complete (default is on)
	KeepJobFlowAliveWhenNoSteps pulumi.BoolPtrInput
	// Kerberos configuration for the cluster. Defined below
	KerberosAttributes ClusterKerberosAttributesPtrInput
	// S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
	LogUri pulumi.StringPtrInput
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master). Cannot be specified if `masterInstanceType` argument or `instanceGroup` configuration blocks are set. Detailed below.
	MasterInstanceGroup ClusterMasterInstanceGroupPtrInput
	// Use the `masterInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the master node. Cannot be specified if `masterInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `master_instance_group` configuration block `instance_type` argument instead
	MasterInstanceType pulumi.StringPtrInput
	// The public DNS name of the master EC2 instance.
	// * `core_instance_group.0.id` - Core node type Instance Group ID, if using Instance Group for this node type.
	MasterPublicDns pulumi.StringPtrInput
	// The name of the step.
	Name pulumi.StringPtrInput
	// The release label for the Amazon EMR release
	ReleaseLabel pulumi.StringPtrInput
	// The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
	ScaleDownBehavior pulumi.StringPtrInput
	// The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `releaseLabel` 4.8.0 or greater
	SecurityConfiguration pulumi.StringPtrInput
	// IAM role that will be assumed by the Amazon EMR service to access AWS resources
	ServiceRole pulumi.StringPtrInput
	// The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `releaseLabel` 5.28.0 or greater. (default is 1)
	StepConcurrencyLevel pulumi.IntPtrInput
	// List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) if other steps are being managed outside of this provider.
	Steps ClusterStepArrayInput
	// list of tags to apply to the EMR Cluster
	Tags pulumi.MapInput
	// Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.
	TerminationProtection pulumi.BoolPtrInput
	// Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
	VisibleToAllUsers pulumi.BoolPtrInput
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	// A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.
	AdditionalInfo *string `pulumi:"additionalInfo"`
	// A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
	Applications []string `pulumi:"applications"`
	// An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
	AutoscalingRole *string `pulumi:"autoscalingRole"`
	// Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.
	BootstrapActions []ClusterBootstrapAction `pulumi:"bootstrapActions"`
	// List of configurations supplied for the EMR cluster you are creating
	Configurations *string `pulumi:"configurations"`
	// A JSON string for supplying list of configurations for the EMR cluster.
	ConfigurationsJson *string `pulumi:"configurationsJson"`
	// Use the `coreInstanceGroup` configuration block `instanceCount` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`coreInstanceCount`-1) as core nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set. Default `1`
	//
	// Deprecated: use `core_instance_group` configuration block `instance_count` argument instead
	CoreInstanceCount *int `pulumi:"coreInstanceCount"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core). Cannot be specified if `coreInstanceCount` argument, `coreInstanceType` argument, or `instanceGroup` configuration blocks are set. Detailed below.
	CoreInstanceGroup *ClusterCoreInstanceGroup `pulumi:"coreInstanceGroup"`
	// Use the `coreInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `core_instance_group` configuration block `instance_type` argument instead
	CoreInstanceType *string `pulumi:"coreInstanceType"`
	// A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
	CustomAmiId *string `pulumi:"customAmiId"`
	// Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
	EbsRootVolumeSize *int `pulumi:"ebsRootVolumeSize"`
	// Attributes for the EC2 instances running the job flow. Defined below
	Ec2Attributes *ClusterEc2Attributes `pulumi:"ec2Attributes"`
	// Use the `masterInstanceGroup` configuration block, `coreInstanceGroup` configuration block and [`emr.InstanceGroup` resource(s)](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) instead. A list of `instanceGroup` objects for each instance group in the cluster. Exactly one of `masterInstanceType` and `instanceGroup` must be specified. If `instanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Cannot be specified if `masterInstanceGroup` or `coreInstanceGroup` configuration blocks are set. Defined below
	//
	// Deprecated: use `master_instance_group` configuration block, `core_instance_group` configuration block, and `aws_emr_instance_group` resource(s) instead
	InstanceGroups []ClusterInstanceGroup `pulumi:"instanceGroups"`
	// Switch on/off run cluster with no steps or when all steps are complete (default is on)
	KeepJobFlowAliveWhenNoSteps *bool `pulumi:"keepJobFlowAliveWhenNoSteps"`
	// Kerberos configuration for the cluster. Defined below
	KerberosAttributes *ClusterKerberosAttributes `pulumi:"kerberosAttributes"`
	// S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
	LogUri *string `pulumi:"logUri"`
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master). Cannot be specified if `masterInstanceType` argument or `instanceGroup` configuration blocks are set. Detailed below.
	MasterInstanceGroup *ClusterMasterInstanceGroup `pulumi:"masterInstanceGroup"`
	// Use the `masterInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the master node. Cannot be specified if `masterInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `master_instance_group` configuration block `instance_type` argument instead
	MasterInstanceType *string `pulumi:"masterInstanceType"`
	// The name of the step.
	Name *string `pulumi:"name"`
	// The release label for the Amazon EMR release
	ReleaseLabel string `pulumi:"releaseLabel"`
	// The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
	ScaleDownBehavior *string `pulumi:"scaleDownBehavior"`
	// The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `releaseLabel` 4.8.0 or greater
	SecurityConfiguration *string `pulumi:"securityConfiguration"`
	// IAM role that will be assumed by the Amazon EMR service to access AWS resources
	ServiceRole string `pulumi:"serviceRole"`
	// The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `releaseLabel` 5.28.0 or greater. (default is 1)
	StepConcurrencyLevel *int `pulumi:"stepConcurrencyLevel"`
	// List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) if other steps are being managed outside of this provider.
	Steps []ClusterStep `pulumi:"steps"`
	// list of tags to apply to the EMR Cluster
	Tags map[string]interface{} `pulumi:"tags"`
	// Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.
	TerminationProtection *bool `pulumi:"terminationProtection"`
	// Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
	VisibleToAllUsers *bool `pulumi:"visibleToAllUsers"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	// A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.
	AdditionalInfo pulumi.StringPtrInput
	// A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
	Applications pulumi.StringArrayInput
	// An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
	AutoscalingRole pulumi.StringPtrInput
	// Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.
	BootstrapActions ClusterBootstrapActionArrayInput
	// List of configurations supplied for the EMR cluster you are creating
	Configurations pulumi.StringPtrInput
	// A JSON string for supplying list of configurations for the EMR cluster.
	ConfigurationsJson pulumi.StringPtrInput
	// Use the `coreInstanceGroup` configuration block `instanceCount` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`coreInstanceCount`-1) as core nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set. Default `1`
	//
	// Deprecated: use `core_instance_group` configuration block `instance_count` argument instead
	CoreInstanceCount pulumi.IntPtrInput
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core). Cannot be specified if `coreInstanceCount` argument, `coreInstanceType` argument, or `instanceGroup` configuration blocks are set. Detailed below.
	CoreInstanceGroup ClusterCoreInstanceGroupPtrInput
	// Use the `coreInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `coreInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `core_instance_group` configuration block `instance_type` argument instead
	CoreInstanceType pulumi.StringPtrInput
	// A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
	CustomAmiId pulumi.StringPtrInput
	// Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
	EbsRootVolumeSize pulumi.IntPtrInput
	// Attributes for the EC2 instances running the job flow. Defined below
	Ec2Attributes ClusterEc2AttributesPtrInput
	// Use the `masterInstanceGroup` configuration block, `coreInstanceGroup` configuration block and [`emr.InstanceGroup` resource(s)](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) instead. A list of `instanceGroup` objects for each instance group in the cluster. Exactly one of `masterInstanceType` and `instanceGroup` must be specified. If `instanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Cannot be specified if `masterInstanceGroup` or `coreInstanceGroup` configuration blocks are set. Defined below
	//
	// Deprecated: use `master_instance_group` configuration block, `core_instance_group` configuration block, and `aws_emr_instance_group` resource(s) instead
	InstanceGroups ClusterInstanceGroupArrayInput
	// Switch on/off run cluster with no steps or when all steps are complete (default is on)
	KeepJobFlowAliveWhenNoSteps pulumi.BoolPtrInput
	// Kerberos configuration for the cluster. Defined below
	KerberosAttributes ClusterKerberosAttributesPtrInput
	// S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
	LogUri pulumi.StringPtrInput
	// Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node type](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master). Cannot be specified if `masterInstanceType` argument or `instanceGroup` configuration blocks are set. Detailed below.
	MasterInstanceGroup ClusterMasterInstanceGroupPtrInput
	// Use the `masterInstanceGroup` configuration block `instanceType` argument instead. The EC2 instance type of the master node. Cannot be specified if `masterInstanceGroup` or `instanceGroup` configuration blocks are set.
	//
	// Deprecated: use `master_instance_group` configuration block `instance_type` argument instead
	MasterInstanceType pulumi.StringPtrInput
	// The name of the step.
	Name pulumi.StringPtrInput
	// The release label for the Amazon EMR release
	ReleaseLabel pulumi.StringInput
	// The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
	ScaleDownBehavior pulumi.StringPtrInput
	// The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `releaseLabel` 4.8.0 or greater
	SecurityConfiguration pulumi.StringPtrInput
	// IAM role that will be assumed by the Amazon EMR service to access AWS resources
	ServiceRole pulumi.StringInput
	// The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `releaseLabel` 5.28.0 or greater. (default is 1)
	StepConcurrencyLevel pulumi.IntPtrInput
	// List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) if other steps are being managed outside of this provider.
	Steps ClusterStepArrayInput
	// list of tags to apply to the EMR Cluster
	Tags pulumi.MapInput
	// Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.
	TerminationProtection pulumi.BoolPtrInput
	// Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
	VisibleToAllUsers pulumi.BoolPtrInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}
