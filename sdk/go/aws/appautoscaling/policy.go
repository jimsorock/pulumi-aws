// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appautoscaling

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an Application AutoScaling Policy resource.
type Policy struct {
	pulumi.CustomResourceState

	// The ARN assigned by AWS to the scaling policy.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the policy.
	Name pulumi.StringOutput `pulumi:"name"`
	// The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to `StepScaling`. Certain services only support only one policy type. For more information see the [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
	PolicyType pulumi.StringPtrOutput `pulumi:"policyType"`
	// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ResourceId pulumi.StringOutput `pulumi:"resourceId"`
	// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ScalableDimension pulumi.StringOutput `pulumi:"scalableDimension"`
	// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ServiceNamespace pulumi.StringOutput `pulumi:"serviceNamespace"`
	// Step scaling policy configuration, requires `policyType = "StepScaling"` (default). See supported fields below.
	StepScalingPolicyConfiguration PolicyStepScalingPolicyConfigurationPtrOutput `pulumi:"stepScalingPolicyConfiguration"`
	// A target tracking policy, requires `policyType = "TargetTrackingScaling"`. See supported fields below.
	TargetTrackingScalingPolicyConfiguration PolicyTargetTrackingScalingPolicyConfigurationPtrOutput `pulumi:"targetTrackingScalingPolicyConfiguration"`
}

// NewPolicy registers a new resource with the given unique name, arguments, and options.
func NewPolicy(ctx *pulumi.Context,
	name string, args *PolicyArgs, opts ...pulumi.ResourceOption) (*Policy, error) {
	if args == nil || args.ResourceId == nil {
		return nil, errors.New("missing required argument 'ResourceId'")
	}
	if args == nil || args.ScalableDimension == nil {
		return nil, errors.New("missing required argument 'ScalableDimension'")
	}
	if args == nil || args.ServiceNamespace == nil {
		return nil, errors.New("missing required argument 'ServiceNamespace'")
	}
	if args == nil {
		args = &PolicyArgs{}
	}
	var resource Policy
	err := ctx.RegisterResource("aws:appautoscaling/policy:Policy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPolicy gets an existing Policy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PolicyState, opts ...pulumi.ResourceOption) (*Policy, error) {
	var resource Policy
	err := ctx.ReadResource("aws:appautoscaling/policy:Policy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Policy resources.
type policyState struct {
	// The ARN assigned by AWS to the scaling policy.
	Arn *string `pulumi:"arn"`
	// The name of the policy.
	Name *string `pulumi:"name"`
	// The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to `StepScaling`. Certain services only support only one policy type. For more information see the [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
	PolicyType *string `pulumi:"policyType"`
	// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ResourceId *string `pulumi:"resourceId"`
	// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ScalableDimension *string `pulumi:"scalableDimension"`
	// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ServiceNamespace *string `pulumi:"serviceNamespace"`
	// Step scaling policy configuration, requires `policyType = "StepScaling"` (default). See supported fields below.
	StepScalingPolicyConfiguration *PolicyStepScalingPolicyConfiguration `pulumi:"stepScalingPolicyConfiguration"`
	// A target tracking policy, requires `policyType = "TargetTrackingScaling"`. See supported fields below.
	TargetTrackingScalingPolicyConfiguration *PolicyTargetTrackingScalingPolicyConfiguration `pulumi:"targetTrackingScalingPolicyConfiguration"`
}

type PolicyState struct {
	// The ARN assigned by AWS to the scaling policy.
	Arn pulumi.StringPtrInput
	// The name of the policy.
	Name pulumi.StringPtrInput
	// The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to `StepScaling`. Certain services only support only one policy type. For more information see the [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
	PolicyType pulumi.StringPtrInput
	// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ResourceId pulumi.StringPtrInput
	// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ScalableDimension pulumi.StringPtrInput
	// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ServiceNamespace pulumi.StringPtrInput
	// Step scaling policy configuration, requires `policyType = "StepScaling"` (default). See supported fields below.
	StepScalingPolicyConfiguration PolicyStepScalingPolicyConfigurationPtrInput
	// A target tracking policy, requires `policyType = "TargetTrackingScaling"`. See supported fields below.
	TargetTrackingScalingPolicyConfiguration PolicyTargetTrackingScalingPolicyConfigurationPtrInput
}

func (PolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*policyState)(nil)).Elem()
}

type policyArgs struct {
	// The name of the policy.
	Name *string `pulumi:"name"`
	// The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to `StepScaling`. Certain services only support only one policy type. For more information see the [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
	PolicyType *string `pulumi:"policyType"`
	// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ResourceId string `pulumi:"resourceId"`
	// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ScalableDimension string `pulumi:"scalableDimension"`
	// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ServiceNamespace string `pulumi:"serviceNamespace"`
	// Step scaling policy configuration, requires `policyType = "StepScaling"` (default). See supported fields below.
	StepScalingPolicyConfiguration *PolicyStepScalingPolicyConfiguration `pulumi:"stepScalingPolicyConfiguration"`
	// A target tracking policy, requires `policyType = "TargetTrackingScaling"`. See supported fields below.
	TargetTrackingScalingPolicyConfiguration *PolicyTargetTrackingScalingPolicyConfiguration `pulumi:"targetTrackingScalingPolicyConfiguration"`
}

// The set of arguments for constructing a Policy resource.
type PolicyArgs struct {
	// The name of the policy.
	Name pulumi.StringPtrInput
	// The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to `StepScaling`. Certain services only support only one policy type. For more information see the [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
	PolicyType pulumi.StringPtrInput
	// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ResourceId pulumi.StringInput
	// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ScalableDimension pulumi.StringInput
	// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
	ServiceNamespace pulumi.StringInput
	// Step scaling policy configuration, requires `policyType = "StepScaling"` (default). See supported fields below.
	StepScalingPolicyConfiguration PolicyStepScalingPolicyConfigurationPtrInput
	// A target tracking policy, requires `policyType = "TargetTrackingScaling"`. See supported fields below.
	TargetTrackingScalingPolicyConfiguration PolicyTargetTrackingScalingPolicyConfigurationPtrInput
}

func (PolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*policyArgs)(nil)).Elem()
}
