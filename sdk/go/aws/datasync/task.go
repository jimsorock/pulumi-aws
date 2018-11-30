// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this Terraform resource.
type Task struct {
	s *pulumi.ResourceState
}

// NewTask registers a new resource with the given unique name, arguments, and options.
func NewTask(ctx *pulumi.Context,
	name string, args *TaskArgs, opts ...pulumi.ResourceOpt) (*Task, error) {
	if args == nil || args.DestinationLocationArn == nil {
		return nil, errors.New("missing required argument 'DestinationLocationArn'")
	}
	if args == nil || args.SourceLocationArn == nil {
		return nil, errors.New("missing required argument 'SourceLocationArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["cloudwatchLogGroupArn"] = nil
		inputs["destinationLocationArn"] = nil
		inputs["name"] = nil
		inputs["options"] = nil
		inputs["sourceLocationArn"] = nil
		inputs["tags"] = nil
	} else {
		inputs["cloudwatchLogGroupArn"] = args.CloudwatchLogGroupArn
		inputs["destinationLocationArn"] = args.DestinationLocationArn
		inputs["name"] = args.Name
		inputs["options"] = args.Options
		inputs["sourceLocationArn"] = args.SourceLocationArn
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:datasync/task:Task", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Task{s: s}, nil
}

// GetTask gets an existing Task resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTask(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TaskState, opts ...pulumi.ResourceOpt) (*Task, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["cloudwatchLogGroupArn"] = state.CloudwatchLogGroupArn
		inputs["destinationLocationArn"] = state.DestinationLocationArn
		inputs["name"] = state.Name
		inputs["options"] = state.Options
		inputs["sourceLocationArn"] = state.SourceLocationArn
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:datasync/task:Task", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Task{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Task) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Task) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Amazon Resource Name (ARN) of the DataSync Task.
func (r *Task) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
func (r *Task) CloudwatchLogGroupArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["cloudwatchLogGroupArn"])
}

// Amazon Resource Name (ARN) of destination DataSync Location.
func (r *Task) DestinationLocationArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["destinationLocationArn"])
}

// Name of the DataSync Task.
func (r *Task) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
func (r *Task) Options() *pulumi.Output {
	return r.s.State["options"]
}

// Amazon Resource Name (ARN) of source DataSync Location.
func (r *Task) SourceLocationArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sourceLocationArn"])
}

// Key-value pairs of resource tags to assign to the DataSync Task.
func (r *Task) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Task resources.
type TaskState struct {
	// Amazon Resource Name (ARN) of the DataSync Task.
	Arn interface{}
	// Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
	CloudwatchLogGroupArn interface{}
	// Amazon Resource Name (ARN) of destination DataSync Location.
	DestinationLocationArn interface{}
	// Name of the DataSync Task.
	Name interface{}
	// Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
	Options interface{}
	// Amazon Resource Name (ARN) of source DataSync Location.
	SourceLocationArn interface{}
	// Key-value pairs of resource tags to assign to the DataSync Task.
	Tags interface{}
}

// The set of arguments for constructing a Task resource.
type TaskArgs struct {
	// Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
	CloudwatchLogGroupArn interface{}
	// Amazon Resource Name (ARN) of destination DataSync Location.
	DestinationLocationArn interface{}
	// Name of the DataSync Task.
	Name interface{}
	// Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
	Options interface{}
	// Amazon Resource Name (ARN) of source DataSync Location.
	SourceLocationArn interface{}
	// Key-value pairs of resource tags to assign to the DataSync Task.
	Tags interface{}
}
