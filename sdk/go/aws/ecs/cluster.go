// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ecs

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an ECS cluster.
// 
// ## setting
// 
// The `setting` configuration block supports the following:
// 
// * `name` - (Required) Name of the setting to manage. Valid values: `containerInsights`.
// * `value` -  (Required) The value to assign to the setting. Value values are `enabled` and `disabled`.
// 
// ## defaultCapacityProviderStrategy
// 
// The `defaultCapacityProviderStrategy` configuration block supports the following:
// 
// * `capacityProvider` - (Required) The short name of the capacity provider.
// * `weight` - (Optional) The relative percentage of the total number of launched tasks that should use the specified capacity provider.
// * `base` - (Optional) The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecs_cluster.html.markdown.
type Cluster struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) that identifies the cluster
	Arn pulumi.StringOutput `pulumi:"arn"`
	// List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
	CapacityProviders pulumi.StringArrayOutput `pulumi:"capacityProviders"`
	// The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
	DefaultCapacityProviderStrategies ClusterDefaultCapacityProviderStrategyArrayOutput `pulumi:"defaultCapacityProviderStrategies"`
	// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
	Name pulumi.StringOutput `pulumi:"name"`
	// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
	Settings ClusterSettingArrayOutput `pulumi:"settings"`
	// Key-value mapping of resource tags
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		args = &ClusterArgs{}
	}
	var resource Cluster
	err := ctx.RegisterResource("aws:ecs/cluster:Cluster", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws:ecs/cluster:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
	// The Amazon Resource Name (ARN) that identifies the cluster
	Arn *string `pulumi:"arn"`
	// List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
	CapacityProviders []string `pulumi:"capacityProviders"`
	// The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
	DefaultCapacityProviderStrategies []ClusterDefaultCapacityProviderStrategy `pulumi:"defaultCapacityProviderStrategies"`
	// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
	Name *string `pulumi:"name"`
	// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
	Settings []ClusterSetting `pulumi:"settings"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

type ClusterState struct {
	// The Amazon Resource Name (ARN) that identifies the cluster
	Arn pulumi.StringPtrInput
	// List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
	CapacityProviders pulumi.StringArrayInput
	// The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
	DefaultCapacityProviderStrategies ClusterDefaultCapacityProviderStrategyArrayInput
	// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
	Name pulumi.StringPtrInput
	// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
	Settings ClusterSettingArrayInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	// List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
	CapacityProviders []string `pulumi:"capacityProviders"`
	// The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
	DefaultCapacityProviderStrategies []ClusterDefaultCapacityProviderStrategy `pulumi:"defaultCapacityProviderStrategies"`
	// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
	Name *string `pulumi:"name"`
	// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
	Settings []ClusterSetting `pulumi:"settings"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	// List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
	CapacityProviders pulumi.StringArrayInput
	// The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
	DefaultCapacityProviderStrategies ClusterDefaultCapacityProviderStrategyArrayInput
	// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
	Name pulumi.StringPtrInput
	// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
	Settings ClusterSettingArrayInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

