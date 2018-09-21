// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Registers a custom domain name for use with AWS API Gateway.
// 
// This resource just establishes ownership of and the TLS settings for
// a particular domain name. An API can be attached to a particular path
// under the registered domain name using
// the `aws_api_gateway_base_path_mapping` resource.
// 
// API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
// API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
// addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
// (either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
// attribute.
// 
// In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
// a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
// given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
// the `regional_domain_name` attribute.
// 
// ~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
type DomainName struct {
	s *pulumi.ResourceState
}

// NewDomainName registers a new resource with the given unique name, arguments, and options.
func NewDomainName(ctx *pulumi.Context,
	name string, args *DomainNameArgs, opts ...pulumi.ResourceOpt) (*DomainName, error) {
	if args == nil || args.DomainName == nil {
		return nil, errors.New("missing required argument 'DomainName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["certificateArn"] = nil
		inputs["certificateBody"] = nil
		inputs["certificateChain"] = nil
		inputs["certificateName"] = nil
		inputs["certificatePrivateKey"] = nil
		inputs["domainName"] = nil
		inputs["endpointConfiguration"] = nil
		inputs["regionalCertificateArn"] = nil
		inputs["regionalCertificateName"] = nil
	} else {
		inputs["certificateArn"] = args.CertificateArn
		inputs["certificateBody"] = args.CertificateBody
		inputs["certificateChain"] = args.CertificateChain
		inputs["certificateName"] = args.CertificateName
		inputs["certificatePrivateKey"] = args.CertificatePrivateKey
		inputs["domainName"] = args.DomainName
		inputs["endpointConfiguration"] = args.EndpointConfiguration
		inputs["regionalCertificateArn"] = args.RegionalCertificateArn
		inputs["regionalCertificateName"] = args.RegionalCertificateName
	}
	inputs["certificateUploadDate"] = nil
	inputs["cloudfrontDomainName"] = nil
	inputs["cloudfrontZoneId"] = nil
	inputs["regionalDomainName"] = nil
	inputs["regionalZoneId"] = nil
	s, err := ctx.RegisterResource("aws:apigateway/domainName:DomainName", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DomainName{s: s}, nil
}

// GetDomainName gets an existing DomainName resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomainName(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DomainNameState, opts ...pulumi.ResourceOpt) (*DomainName, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["certificateArn"] = state.CertificateArn
		inputs["certificateBody"] = state.CertificateBody
		inputs["certificateChain"] = state.CertificateChain
		inputs["certificateName"] = state.CertificateName
		inputs["certificatePrivateKey"] = state.CertificatePrivateKey
		inputs["certificateUploadDate"] = state.CertificateUploadDate
		inputs["cloudfrontDomainName"] = state.CloudfrontDomainName
		inputs["cloudfrontZoneId"] = state.CloudfrontZoneId
		inputs["domainName"] = state.DomainName
		inputs["endpointConfiguration"] = state.EndpointConfiguration
		inputs["regionalCertificateArn"] = state.RegionalCertificateArn
		inputs["regionalCertificateName"] = state.RegionalCertificateName
		inputs["regionalDomainName"] = state.RegionalDomainName
		inputs["regionalZoneId"] = state.RegionalZoneId
	}
	s, err := ctx.ReadResource("aws:apigateway/domainName:DomainName", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DomainName{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DomainName) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DomainName) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
// desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
// `regional_certificate_arn`, and `regional_certificate_name`.
func (r *DomainName) CertificateArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateArn"])
}

// The certificate issued for the domain name
// being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
// `regional_certificate_name`.
func (r *DomainName) CertificateBody() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateBody"])
}

// The certificate for the CA that issued the
// certificate, along with any intermediate CA certificates required to
// create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
// `regional_certificate_arn`, and `regional_certificate_name`.
func (r *DomainName) CertificateChain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateChain"])
}

// The unique name to use when registering this
// certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
// `regional_certificate_name`. Required if `certificate_arn` is not set.
func (r *DomainName) CertificateName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateName"])
}

// The private key associated with the
// domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
func (r *DomainName) CertificatePrivateKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificatePrivateKey"])
}

// The upload date associated with the domain certificate.
func (r *DomainName) CertificateUploadDate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateUploadDate"])
}

// The hostname created by Cloudfront to represent
// the distribution that implements this domain name mapping.
func (r *DomainName) CloudfrontDomainName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["cloudfrontDomainName"])
}

// For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
// that can be used to create a Route53 alias record for the distribution.
func (r *DomainName) CloudfrontZoneId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["cloudfrontZoneId"])
}

// The fully-qualified domain name to register
func (r *DomainName) DomainName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domainName"])
}

// Nested argument defining API endpoint configuration including endpoint type. Defined below.
func (r *DomainName) EndpointConfiguration() *pulumi.Output {
	return r.s.State["endpointConfiguration"]
}

// The ARN for an AWS-managed certificate. Used when a regional domain name is
// desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
// `certificate_private_key`.
func (r *DomainName) RegionalCertificateArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["regionalCertificateArn"])
}

// The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
// `certificate_private_key`.
func (r *DomainName) RegionalCertificateName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["regionalCertificateName"])
}

// The hostname for the custom domain's regional endpoint.
func (r *DomainName) RegionalDomainName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["regionalDomainName"])
}

// The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
func (r *DomainName) RegionalZoneId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["regionalZoneId"])
}

// Input properties used for looking up and filtering DomainName resources.
type DomainNameState struct {
	// The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
	// desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
	// `regional_certificate_arn`, and `regional_certificate_name`.
	CertificateArn interface{}
	// The certificate issued for the domain name
	// being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
	// `regional_certificate_name`.
	CertificateBody interface{}
	// The certificate for the CA that issued the
	// certificate, along with any intermediate CA certificates required to
	// create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
	// `regional_certificate_arn`, and `regional_certificate_name`.
	CertificateChain interface{}
	// The unique name to use when registering this
	// certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
	// `regional_certificate_name`. Required if `certificate_arn` is not set.
	CertificateName interface{}
	// The private key associated with the
	// domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
	CertificatePrivateKey interface{}
	// The upload date associated with the domain certificate.
	CertificateUploadDate interface{}
	// The hostname created by Cloudfront to represent
	// the distribution that implements this domain name mapping.
	CloudfrontDomainName interface{}
	// For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
	// that can be used to create a Route53 alias record for the distribution.
	CloudfrontZoneId interface{}
	// The fully-qualified domain name to register
	DomainName interface{}
	// Nested argument defining API endpoint configuration including endpoint type. Defined below.
	EndpointConfiguration interface{}
	// The ARN for an AWS-managed certificate. Used when a regional domain name is
	// desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
	// `certificate_private_key`.
	RegionalCertificateArn interface{}
	// The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
	// `certificate_private_key`.
	RegionalCertificateName interface{}
	// The hostname for the custom domain's regional endpoint.
	RegionalDomainName interface{}
	// The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
	RegionalZoneId interface{}
}

// The set of arguments for constructing a DomainName resource.
type DomainNameArgs struct {
	// The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
	// desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
	// `regional_certificate_arn`, and `regional_certificate_name`.
	CertificateArn interface{}
	// The certificate issued for the domain name
	// being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
	// `regional_certificate_name`.
	CertificateBody interface{}
	// The certificate for the CA that issued the
	// certificate, along with any intermediate CA certificates required to
	// create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
	// `regional_certificate_arn`, and `regional_certificate_name`.
	CertificateChain interface{}
	// The unique name to use when registering this
	// certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
	// `regional_certificate_name`. Required if `certificate_arn` is not set.
	CertificateName interface{}
	// The private key associated with the
	// domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
	CertificatePrivateKey interface{}
	// The fully-qualified domain name to register
	DomainName interface{}
	// Nested argument defining API endpoint configuration including endpoint type. Defined below.
	EndpointConfiguration interface{}
	// The ARN for an AWS-managed certificate. Used when a regional domain name is
	// desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
	// `certificate_private_key`.
	RegionalCertificateArn interface{}
	// The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
	// `certificate_private_key`.
	RegionalCertificateName interface{}
}