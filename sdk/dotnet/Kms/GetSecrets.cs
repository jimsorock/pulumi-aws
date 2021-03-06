// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kms
{
    public static class GetSecrets
    {
        /// <summary>
        /// Decrypt multiple secrets from data encrypted with the AWS KMS service.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSecretsResult> InvokeAsync(GetSecretsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecretsResult>("aws:kms/getSecrets:getSecrets", args ?? new GetSecretsArgs(), options.WithVersion());
    }


    public sealed class GetSecretsArgs : Pulumi.InvokeArgs
    {
        [Input("secrets", required: true)]
        private List<Inputs.GetSecretsSecretArgs>? _secrets;

        /// <summary>
        /// One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
        /// </summary>
        public List<Inputs.GetSecretsSecretArgs> Secrets
        {
            get => _secrets ?? (_secrets = new List<Inputs.GetSecretsSecretArgs>());
            set => _secrets = value;
        }

        public GetSecretsArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSecretsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Map containing each `secret` `name` as the key with its decrypted plaintext value
        /// </summary>
        public readonly ImmutableDictionary<string, string> Plaintext;
        public readonly ImmutableArray<Outputs.GetSecretsSecretResult> Secrets;

        [OutputConstructor]
        private GetSecretsResult(
            string id,

            ImmutableDictionary<string, string> plaintext,

            ImmutableArray<Outputs.GetSecretsSecretResult> secrets)
        {
            Id = id;
            Plaintext = plaintext;
            Secrets = secrets;
        }
    }
}
