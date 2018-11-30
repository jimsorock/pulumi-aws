// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package waf

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a WAF Rule Resource
type Rule struct {
	s *pulumi.ResourceState
}

// NewRule registers a new resource with the given unique name, arguments, and options.
func NewRule(ctx *pulumi.Context,
	name string, args *RuleArgs, opts ...pulumi.ResourceOpt) (*Rule, error) {
	if args == nil || args.MetricName == nil {
		return nil, errors.New("missing required argument 'MetricName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["metricName"] = nil
		inputs["name"] = nil
		inputs["predicates"] = nil
	} else {
		inputs["metricName"] = args.MetricName
		inputs["name"] = args.Name
		inputs["predicates"] = args.Predicates
	}
	s, err := ctx.RegisterResource("aws:waf/rule:Rule", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Rule{s: s}, nil
}

// GetRule gets an existing Rule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRule(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RuleState, opts ...pulumi.ResourceOpt) (*Rule, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["metricName"] = state.MetricName
		inputs["name"] = state.Name
		inputs["predicates"] = state.Predicates
	}
	s, err := ctx.ReadResource("aws:waf/rule:Rule", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Rule{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Rule) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Rule) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
func (r *Rule) MetricName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["metricName"])
}

// The name or description of the rule.
func (r *Rule) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
func (r *Rule) Predicates() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["predicates"])
}

// Input properties used for looking up and filtering Rule resources.
type RuleState struct {
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName interface{}
	// The name or description of the rule.
	Name interface{}
	// One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
	Predicates interface{}
}

// The set of arguments for constructing a Rule resource.
type RuleArgs struct {
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName interface{}
	// The name or description of the rule.
	Name interface{}
	// One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
	Predicates interface{}
}
