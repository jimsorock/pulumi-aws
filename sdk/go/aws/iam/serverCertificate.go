// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an IAM Server Certificate resource to upload Server Certificates.
// Certs uploaded to IAM can easily work with other AWS services such as:
//
// - AWS Elastic Beanstalk
// - Elastic Load Balancing
// - CloudFront
// - AWS OpsWorks
//
// For information about server certificates in IAM, see [Managing Server
// Certificates][2] in AWS Documentation.
//
// > **Note:** All arguments including the private key will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
type ServerCertificate struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody pulumi.StringOutput `pulumi:"certificateBody"`
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain pulumi.StringPtrOutput `pulumi:"certificateChain"`
	// The name of the Server Certificate. Do not include the
	// path in this value. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more details on IAM Paths.
	Path pulumi.StringPtrOutput `pulumi:"path"`
	// The contents of the private key in PEM-encoded format.
	PrivateKey pulumi.StringOutput `pulumi:"privateKey"`
}

// NewServerCertificate registers a new resource with the given unique name, arguments, and options.
func NewServerCertificate(ctx *pulumi.Context,
	name string, args *ServerCertificateArgs, opts ...pulumi.ResourceOption) (*ServerCertificate, error) {
	if args == nil || args.CertificateBody == nil {
		return nil, errors.New("missing required argument 'CertificateBody'")
	}
	if args == nil || args.PrivateKey == nil {
		return nil, errors.New("missing required argument 'PrivateKey'")
	}
	if args == nil {
		args = &ServerCertificateArgs{}
	}
	var resource ServerCertificate
	err := ctx.RegisterResource("aws:iam/serverCertificate:ServerCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServerCertificate gets an existing ServerCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServerCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerCertificateState, opts ...pulumi.ResourceOption) (*ServerCertificate, error) {
	var resource ServerCertificate
	err := ctx.ReadResource("aws:iam/serverCertificate:ServerCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServerCertificate resources.
type serverCertificateState struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn *string `pulumi:"arn"`
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody *string `pulumi:"certificateBody"`
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain *string `pulumi:"certificateChain"`
	// The name of the Server Certificate. Do not include the
	// path in this value. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more details on IAM Paths.
	Path *string `pulumi:"path"`
	// The contents of the private key in PEM-encoded format.
	PrivateKey *string `pulumi:"privateKey"`
}

type ServerCertificateState struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn pulumi.StringPtrInput
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody pulumi.StringPtrInput
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain pulumi.StringPtrInput
	// The name of the Server Certificate. Do not include the
	// path in this value. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more details on IAM Paths.
	Path pulumi.StringPtrInput
	// The contents of the private key in PEM-encoded format.
	PrivateKey pulumi.StringPtrInput
}

func (ServerCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverCertificateState)(nil)).Elem()
}

type serverCertificateArgs struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn *string `pulumi:"arn"`
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody string `pulumi:"certificateBody"`
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain *string `pulumi:"certificateChain"`
	// The name of the Server Certificate. Do not include the
	// path in this value. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more details on IAM Paths.
	Path *string `pulumi:"path"`
	// The contents of the private key in PEM-encoded format.
	PrivateKey string `pulumi:"privateKey"`
}

// The set of arguments for constructing a ServerCertificate resource.
type ServerCertificateArgs struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn pulumi.StringPtrInput
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody pulumi.StringInput
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain pulumi.StringPtrInput
	// The name of the Server Certificate. Do not include the
	// path in this value. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more details on IAM Paths.
	Path pulumi.StringPtrInput
	// The contents of the private key in PEM-encoded format.
	PrivateKey pulumi.StringInput
}

func (ServerCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverCertificateArgs)(nil)).Elem()
}
