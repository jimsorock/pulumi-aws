// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Mq.Inputs
{

    public sealed class BrokerMaintenanceWindowStartTimeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The day of the week. e.g. `MONDAY`, `TUESDAY`, or `WEDNESDAY`
        /// </summary>
        [Input("dayOfWeek", required: true)]
        public Input<string> DayOfWeek { get; set; } = null!;

        /// <summary>
        /// The time, in 24-hour format. e.g. `02:00`
        /// </summary>
        [Input("timeOfDay", required: true)]
        public Input<string> TimeOfDay { get; set; } = null!;

        /// <summary>
        /// The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. `CET`
        /// </summary>
        [Input("timeZone", required: true)]
        public Input<string> TimeZone { get; set; } = null!;

        public BrokerMaintenanceWindowStartTimeGetArgs()
        {
        }
    }
}