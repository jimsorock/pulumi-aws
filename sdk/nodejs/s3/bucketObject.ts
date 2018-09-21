// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Tags} from "../index";
import {Bucket} from "./bucket";

/**
 * Provides a S3 bucket object resource.
 */
export class BucketObject extends pulumi.CustomResource {
    /**
     * Get an existing BucketObject resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketObjectState): BucketObject {
        return new BucketObject(name, <any>state, { id });
    }

    /**
     * The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".
     */
    public readonly acl: pulumi.Output<string | undefined>;
    /**
     * The name of the bucket to put the file in.
     */
    public readonly bucket: pulumi.Output<string>;
    /**
     * Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
     */
    public readonly cacheControl: pulumi.Output<string | undefined>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    public readonly content: pulumi.Output<string | undefined>;
    /**
     * Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
     */
    public readonly contentBase64: pulumi.Output<string | undefined>;
    /**
     * Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
     */
    public readonly contentDisposition: pulumi.Output<string | undefined>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
     */
    public readonly contentEncoding: pulumi.Output<string | undefined>;
    /**
     * The language the content is in e.g. en-US or en-GB.
     */
    public readonly contentLanguage: pulumi.Output<string | undefined>;
    /**
     * A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
     */
    public readonly contentType: pulumi.Output<string>;
    /**
     * Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
     * This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.
     */
    public readonly etag: pulumi.Output<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    public readonly key: pulumi.Output<string>;
    /**
     * Specifies the AWS KMS Key ARN to use for object encryption.
     * This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
     * use the exported `arn` attribute:
     * `kms_key_id = "${aws_kms_key.foo.arn}"`
     */
    public readonly kmsKeyId: pulumi.Output<string | undefined>;
    /**
     * Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".
     */
    public readonly serverSideEncryption: pulumi.Output<string>;
    /**
     * The path to a file that will be read and uploaded as raw bytes for the object content.
     */
    public readonly source: pulumi.Output<pulumi.asset.Asset | undefined>;
    /**
     * Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
     * for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".
     */
    public readonly storageClass: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the object.
     */
    public readonly tags: pulumi.Output<Tags | undefined>;
    /**
     * A unique version ID value for the object, if bucket versioning
     * is enabled.
     */
    public /*out*/ readonly versionId: pulumi.Output<string>;
    /**
     * Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).
     */
    public readonly websiteRedirect: pulumi.Output<string | undefined>;

    /**
     * Create a BucketObject resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BucketObjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BucketObjectArgs | BucketObjectState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: BucketObjectState = argsOrState as BucketObjectState | undefined;
            inputs["acl"] = state ? state.acl : undefined;
            inputs["bucket"] = state ? state.bucket : undefined;
            inputs["cacheControl"] = state ? state.cacheControl : undefined;
            inputs["content"] = state ? state.content : undefined;
            inputs["contentBase64"] = state ? state.contentBase64 : undefined;
            inputs["contentDisposition"] = state ? state.contentDisposition : undefined;
            inputs["contentEncoding"] = state ? state.contentEncoding : undefined;
            inputs["contentLanguage"] = state ? state.contentLanguage : undefined;
            inputs["contentType"] = state ? state.contentType : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["key"] = state ? state.key : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["serverSideEncryption"] = state ? state.serverSideEncryption : undefined;
            inputs["source"] = state ? state.source : undefined;
            inputs["storageClass"] = state ? state.storageClass : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["versionId"] = state ? state.versionId : undefined;
            inputs["websiteRedirect"] = state ? state.websiteRedirect : undefined;
        } else {
            const args = argsOrState as BucketObjectArgs | undefined;
            if (!args || args.bucket === undefined) {
                throw new Error("Missing required property 'bucket'");
            }
            inputs["acl"] = args ? args.acl : undefined;
            inputs["bucket"] = args ? args.bucket : undefined;
            inputs["cacheControl"] = args ? args.cacheControl : undefined;
            inputs["content"] = args ? args.content : undefined;
            inputs["contentBase64"] = args ? args.contentBase64 : undefined;
            inputs["contentDisposition"] = args ? args.contentDisposition : undefined;
            inputs["contentEncoding"] = args ? args.contentEncoding : undefined;
            inputs["contentLanguage"] = args ? args.contentLanguage : undefined;
            inputs["contentType"] = args ? args.contentType : undefined;
            inputs["etag"] = args ? args.etag : undefined;
            inputs["key"] = args ? args.key : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["serverSideEncryption"] = args ? args.serverSideEncryption : undefined;
            inputs["source"] = args ? args.source : undefined;
            inputs["storageClass"] = args ? args.storageClass : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["websiteRedirect"] = args ? args.websiteRedirect : undefined;
            inputs["versionId"] = undefined /*out*/;
        }
        super("aws:s3/bucketObject:BucketObject", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BucketObject resources.
 */
export interface BucketObjectState {
    /**
     * The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".
     */
    readonly acl?: pulumi.Input<string>;
    /**
     * The name of the bucket to put the file in.
     */
    readonly bucket?: pulumi.Input<string | Bucket>;
    /**
     * Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
     */
    readonly cacheControl?: pulumi.Input<string>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    readonly content?: pulumi.Input<string>;
    /**
     * Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
     */
    readonly contentBase64?: pulumi.Input<string>;
    /**
     * Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
     */
    readonly contentDisposition?: pulumi.Input<string>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
     */
    readonly contentEncoding?: pulumi.Input<string>;
    /**
     * The language the content is in e.g. en-US or en-GB.
     */
    readonly contentLanguage?: pulumi.Input<string>;
    /**
     * A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
     * This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    readonly key?: pulumi.Input<string>;
    /**
     * Specifies the AWS KMS Key ARN to use for object encryption.
     * This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
     * use the exported `arn` attribute:
     * `kms_key_id = "${aws_kms_key.foo.arn}"`
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".
     */
    readonly serverSideEncryption?: pulumi.Input<string>;
    /**
     * The path to a file that will be read and uploaded as raw bytes for the object content.
     */
    readonly source?: pulumi.Input<pulumi.asset.Asset>;
    /**
     * Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
     * for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".
     */
    readonly storageClass?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * A unique version ID value for the object, if bucket versioning
     * is enabled.
     */
    readonly versionId?: pulumi.Input<string>;
    /**
     * Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).
     */
    readonly websiteRedirect?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BucketObject resource.
 */
export interface BucketObjectArgs {
    /**
     * The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".
     */
    readonly acl?: pulumi.Input<string>;
    /**
     * The name of the bucket to put the file in.
     */
    readonly bucket: pulumi.Input<string | Bucket>;
    /**
     * Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
     */
    readonly cacheControl?: pulumi.Input<string>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    readonly content?: pulumi.Input<string>;
    /**
     * Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
     */
    readonly contentBase64?: pulumi.Input<string>;
    /**
     * Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
     */
    readonly contentDisposition?: pulumi.Input<string>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
     */
    readonly contentEncoding?: pulumi.Input<string>;
    /**
     * The language the content is in e.g. en-US or en-GB.
     */
    readonly contentLanguage?: pulumi.Input<string>;
    /**
     * A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
     * This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    readonly key?: pulumi.Input<string>;
    /**
     * Specifies the AWS KMS Key ARN to use for object encryption.
     * This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
     * use the exported `arn` attribute:
     * `kms_key_id = "${aws_kms_key.foo.arn}"`
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".
     */
    readonly serverSideEncryption?: pulumi.Input<string>;
    /**
     * The path to a file that will be read and uploaded as raw bytes for the object content.
     */
    readonly source?: pulumi.Input<pulumi.asset.Asset>;
    /**
     * Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
     * for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".
     */
    readonly storageClass?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).
     */
    readonly websiteRedirect?: pulumi.Input<string>;
}