// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Inputs
{

    public sealed class ProviderAssumeRoleArgs : Pulumi.ResourceArgs
    {
        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        [Input("policy")]
        public Input<string>? Policy { get; set; }

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        [Input("sessionName")]
        public Input<string>? SessionName { get; set; }

        public ProviderAssumeRoleArgs()
        {
        }
    }
}
