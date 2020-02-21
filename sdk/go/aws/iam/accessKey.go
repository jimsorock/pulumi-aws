// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package iam

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown.
type AccessKey struct {
	pulumi.CustomResourceState

	// The encrypted secret, base64 encoded, if `pgpKey` was specified.
	// > **NOTE:** The encrypted secret may be decrypted using the command line,
	EncryptedSecret pulumi.StringOutput `pulumi:"encryptedSecret"`
	// The fingerprint of the PGP key used to encrypt
	// the secret
	KeyFingerprint pulumi.StringOutput `pulumi:"keyFingerprint"`
	// Either a base-64 encoded PGP public key, or a
	// keybase username in the form `keybase:some_person_that_exists`, for use
	// in the `encryptedSecret` output attribute.
	PgpKey pulumi.StringPtrOutput `pulumi:"pgpKey"`
	// The secret access key. Note that this will be written
	// to the state file. If you use this, please protect your backend state file
	// judiciously. Alternatively, you may supply a `pgpKey` instead, which will
	// prevent the secret from being stored in plaintext, at the cost of preventing
	// the use of the secret key in automation.
	Secret pulumi.StringOutput `pulumi:"secret"`
	// **DEPRECATED** The secret access key converted into an SES SMTP
	// password by applying [AWS's documented conversion
	SesSmtpPassword pulumi.StringOutput `pulumi:"sesSmtpPassword"`
	// The secret access key converted into an SES SMTP
	// password by applying [AWS's documented Sigv4 conversion
	// algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).
	// As SigV4 is region specific, valid Provider regions are `ap-south-1`, `ap-southeast-2`, `eu-central-1`, `eu-west-1`, `us-east-1` and `us-west-2`. See current [AWS SES regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region)
	SesSmtpPasswordV4 pulumi.StringOutput `pulumi:"sesSmtpPasswordV4"`
	// The access key status to apply. Defaults to `Active`.
	// Valid values are `Active` and `Inactive`.
	Status pulumi.StringOutput `pulumi:"status"`
	// The IAM user to associate with this access key.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewAccessKey registers a new resource with the given unique name, arguments, and options.
func NewAccessKey(ctx *pulumi.Context,
	name string, args *AccessKeyArgs, opts ...pulumi.ResourceOption) (*AccessKey, error) {
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	if args == nil {
		args = &AccessKeyArgs{}
	}
	var resource AccessKey
	err := ctx.RegisterResource("aws:iam/accessKey:AccessKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessKey gets an existing AccessKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessKeyState, opts ...pulumi.ResourceOption) (*AccessKey, error) {
	var resource AccessKey
	err := ctx.ReadResource("aws:iam/accessKey:AccessKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessKey resources.
type accessKeyState struct {
	// The encrypted secret, base64 encoded, if `pgpKey` was specified.
	// > **NOTE:** The encrypted secret may be decrypted using the command line,
	EncryptedSecret *string `pulumi:"encryptedSecret"`
	// The fingerprint of the PGP key used to encrypt
	// the secret
	KeyFingerprint *string `pulumi:"keyFingerprint"`
	// Either a base-64 encoded PGP public key, or a
	// keybase username in the form `keybase:some_person_that_exists`, for use
	// in the `encryptedSecret` output attribute.
	PgpKey *string `pulumi:"pgpKey"`
	// The secret access key. Note that this will be written
	// to the state file. If you use this, please protect your backend state file
	// judiciously. Alternatively, you may supply a `pgpKey` instead, which will
	// prevent the secret from being stored in plaintext, at the cost of preventing
	// the use of the secret key in automation.
	Secret *string `pulumi:"secret"`
	// **DEPRECATED** The secret access key converted into an SES SMTP
	// password by applying [AWS's documented conversion
	SesSmtpPassword *string `pulumi:"sesSmtpPassword"`
	// The secret access key converted into an SES SMTP
	// password by applying [AWS's documented Sigv4 conversion
	// algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).
	// As SigV4 is region specific, valid Provider regions are `ap-south-1`, `ap-southeast-2`, `eu-central-1`, `eu-west-1`, `us-east-1` and `us-west-2`. See current [AWS SES regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region)
	SesSmtpPasswordV4 *string `pulumi:"sesSmtpPasswordV4"`
	// The access key status to apply. Defaults to `Active`.
	// Valid values are `Active` and `Inactive`.
	Status *string `pulumi:"status"`
	// The IAM user to associate with this access key.
	User *string `pulumi:"user"`
}

type AccessKeyState struct {
	// The encrypted secret, base64 encoded, if `pgpKey` was specified.
	// > **NOTE:** The encrypted secret may be decrypted using the command line,
	EncryptedSecret pulumi.StringPtrInput
	// The fingerprint of the PGP key used to encrypt
	// the secret
	KeyFingerprint pulumi.StringPtrInput
	// Either a base-64 encoded PGP public key, or a
	// keybase username in the form `keybase:some_person_that_exists`, for use
	// in the `encryptedSecret` output attribute.
	PgpKey pulumi.StringPtrInput
	// The secret access key. Note that this will be written
	// to the state file. If you use this, please protect your backend state file
	// judiciously. Alternatively, you may supply a `pgpKey` instead, which will
	// prevent the secret from being stored in plaintext, at the cost of preventing
	// the use of the secret key in automation.
	Secret pulumi.StringPtrInput
	// **DEPRECATED** The secret access key converted into an SES SMTP
	// password by applying [AWS's documented conversion
	SesSmtpPassword pulumi.StringPtrInput
	// The secret access key converted into an SES SMTP
	// password by applying [AWS's documented Sigv4 conversion
	// algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).
	// As SigV4 is region specific, valid Provider regions are `ap-south-1`, `ap-southeast-2`, `eu-central-1`, `eu-west-1`, `us-east-1` and `us-west-2`. See current [AWS SES regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region)
	SesSmtpPasswordV4 pulumi.StringPtrInput
	// The access key status to apply. Defaults to `Active`.
	// Valid values are `Active` and `Inactive`.
	Status pulumi.StringPtrInput
	// The IAM user to associate with this access key.
	User pulumi.StringPtrInput
}

func (AccessKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessKeyState)(nil)).Elem()
}

type accessKeyArgs struct {
	// Either a base-64 encoded PGP public key, or a
	// keybase username in the form `keybase:some_person_that_exists`, for use
	// in the `encryptedSecret` output attribute.
	PgpKey *string `pulumi:"pgpKey"`
	// The access key status to apply. Defaults to `Active`.
	// Valid values are `Active` and `Inactive`.
	Status *string `pulumi:"status"`
	// The IAM user to associate with this access key.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a AccessKey resource.
type AccessKeyArgs struct {
	// Either a base-64 encoded PGP public key, or a
	// keybase username in the form `keybase:some_person_that_exists`, for use
	// in the `encryptedSecret` output attribute.
	PgpKey pulumi.StringPtrInput
	// The access key status to apply. Defaults to `Active`.
	// Valid values are `Active` and `Inactive`.
	Status pulumi.StringPtrInput
	// The IAM user to associate with this access key.
	User pulumi.StringInput
}

func (AccessKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessKeyArgs)(nil)).Elem()
}

