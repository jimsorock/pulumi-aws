// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ApiGateway.Outputs
{

    [OutputType]
    public sealed class UsagePlanThrottleSettings
    {
        /// <summary>
        /// The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
        /// </summary>
        public readonly int? BurstLimit;
        /// <summary>
        /// The API request steady-state rate limit.
        /// </summary>
        public readonly double? RateLimit;

        [OutputConstructor]
        private UsagePlanThrottleSettings(
            int? burstLimit,

            double? rateLimit)
        {
            BurstLimit = burstLimit;
            RateLimit = rateLimit;
        }
    }
}
