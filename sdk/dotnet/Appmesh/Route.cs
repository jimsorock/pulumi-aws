// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh
{
    /// <summary>
    /// Provides an AWS App Mesh route resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_route.html.markdown.
    /// </summary>
    public partial class Route : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the route.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The creation date of the route.
        /// </summary>
        [Output("createdDate")]
        public Output<string> CreatedDate { get; private set; } = null!;

        /// <summary>
        /// The last update date of the route.
        /// </summary>
        [Output("lastUpdatedDate")]
        public Output<string> LastUpdatedDate { get; private set; } = null!;

        /// <summary>
        /// The name of the service mesh in which to create the route.
        /// </summary>
        [Output("meshName")]
        public Output<string> MeshName { get; private set; } = null!;

        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The route specification to apply.
        /// </summary>
        [Output("spec")]
        public Output<Outputs.RouteSpec> Spec { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The name of the virtual router in which to create the route.
        /// </summary>
        [Output("virtualRouterName")]
        public Output<string> VirtualRouterName { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws:appmesh/route:Route", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, RouteState? state = null, CustomResourceOptions? options = null)
            : base("aws:appmesh/route:Route", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, RouteState? state = null, CustomResourceOptions? options = null)
        {
            return new Route(name, id, state, options);
        }
    }

    public sealed class RouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the service mesh in which to create the route.
        /// </summary>
        [Input("meshName", required: true)]
        public Input<string> MeshName { get; set; } = null!;

        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The route specification to apply.
        /// </summary>
        [Input("spec", required: true)]
        public Input<Inputs.RouteSpecArgs> Spec { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of the virtual router in which to create the route.
        /// </summary>
        [Input("virtualRouterName", required: true)]
        public Input<string> VirtualRouterName { get; set; } = null!;

        public RouteArgs()
        {
        }
    }

    public sealed class RouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the route.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The creation date of the route.
        /// </summary>
        [Input("createdDate")]
        public Input<string>? CreatedDate { get; set; }

        /// <summary>
        /// The last update date of the route.
        /// </summary>
        [Input("lastUpdatedDate")]
        public Input<string>? LastUpdatedDate { get; set; }

        /// <summary>
        /// The name of the service mesh in which to create the route.
        /// </summary>
        [Input("meshName")]
        public Input<string>? MeshName { get; set; }

        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The route specification to apply.
        /// </summary>
        [Input("spec")]
        public Input<Inputs.RouteSpecGetArgs>? Spec { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of the virtual router in which to create the route.
        /// </summary>
        [Input("virtualRouterName")]
        public Input<string>? VirtualRouterName { get; set; }

        public RouteState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class RouteSpecArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The HTTP routing information for the route.
        /// </summary>
        [Input("httpRoute")]
        public Input<RouteSpecHttpRouteArgs>? HttpRoute { get; set; }

        /// <summary>
        /// The priority for the route, between `0` and `1000`.
        /// Routes are matched based on the specified value, where `0` is the highest priority.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// The TCP routing information for the route.
        /// </summary>
        [Input("tcpRoute")]
        public Input<RouteSpecTcpRouteArgs>? TcpRoute { get; set; }

        public RouteSpecArgs()
        {
        }
    }

    public sealed class RouteSpecGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The HTTP routing information for the route.
        /// </summary>
        [Input("httpRoute")]
        public Input<RouteSpecHttpRouteGetArgs>? HttpRoute { get; set; }

        /// <summary>
        /// The priority for the route, between `0` and `1000`.
        /// Routes are matched based on the specified value, where `0` is the highest priority.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// The TCP routing information for the route.
        /// </summary>
        [Input("tcpRoute")]
        public Input<RouteSpecTcpRouteGetArgs>? TcpRoute { get; set; }

        public RouteSpecGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteActionArgs : Pulumi.ResourceArgs
    {
        [Input("weightedTargets", required: true)]
        private InputList<RouteSpecHttpRouteActionWeightedTargetsArgs>? _weightedTargets;

        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public InputList<RouteSpecHttpRouteActionWeightedTargetsArgs> WeightedTargets
        {
            get => _weightedTargets ?? (_weightedTargets = new InputList<RouteSpecHttpRouteActionWeightedTargetsArgs>());
            set => _weightedTargets = value;
        }

        public RouteSpecHttpRouteActionArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteActionGetArgs : Pulumi.ResourceArgs
    {
        [Input("weightedTargets", required: true)]
        private InputList<RouteSpecHttpRouteActionWeightedTargetsGetArgs>? _weightedTargets;

        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public InputList<RouteSpecHttpRouteActionWeightedTargetsGetArgs> WeightedTargets
        {
            get => _weightedTargets ?? (_weightedTargets = new InputList<RouteSpecHttpRouteActionWeightedTargetsGetArgs>());
            set => _weightedTargets = value;
        }

        public RouteSpecHttpRouteActionGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteActionWeightedTargetsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        [Input("virtualNode", required: true)]
        public Input<string> VirtualNode { get; set; } = null!;

        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public RouteSpecHttpRouteActionWeightedTargetsArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteActionWeightedTargetsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        [Input("virtualNode", required: true)]
        public Input<string> VirtualNode { get; set; } = null!;

        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public RouteSpecHttpRouteActionWeightedTargetsGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        [Input("action", required: true)]
        public Input<RouteSpecHttpRouteActionArgs> Action { get; set; } = null!;

        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        [Input("match", required: true)]
        public Input<RouteSpecHttpRouteMatchArgs> Match { get; set; } = null!;

        public RouteSpecHttpRouteArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        [Input("action", required: true)]
        public Input<RouteSpecHttpRouteActionGetArgs> Action { get; set; } = null!;

        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        [Input("match", required: true)]
        public Input<RouteSpecHttpRouteMatchGetArgs> Match { get; set; } = null!;

        public RouteSpecHttpRouteGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchArgs : Pulumi.ResourceArgs
    {
        [Input("headers")]
        private InputList<RouteSpecHttpRouteMatchHeadersArgs>? _headers;

        /// <summary>
        /// The client request headers to match on.
        /// </summary>
        public InputList<RouteSpecHttpRouteMatchHeadersArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<RouteSpecHttpRouteMatchHeadersArgs>());
            set => _headers = value;
        }

        /// <summary>
        /// The client request header method to match on. Valid values: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        /// <summary>
        /// The client request header scheme to match on. Valid values: `http`, `https`.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        public RouteSpecHttpRouteMatchArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchGetArgs : Pulumi.ResourceArgs
    {
        [Input("headers")]
        private InputList<RouteSpecHttpRouteMatchHeadersGetArgs>? _headers;

        /// <summary>
        /// The client request headers to match on.
        /// </summary>
        public InputList<RouteSpecHttpRouteMatchHeadersGetArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<RouteSpecHttpRouteMatchHeadersGetArgs>());
            set => _headers = value;
        }

        /// <summary>
        /// The client request header method to match on. Valid values: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        /// <summary>
        /// The client request header scheme to match on. Valid values: `http`, `https`.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        public RouteSpecHttpRouteMatchGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If `true`, the match is on the opposite of the `match` method and value. Default is `false`.
        /// </summary>
        [Input("invert")]
        public Input<bool>? Invert { get; set; }

        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        [Input("match")]
        public Input<RouteSpecHttpRouteMatchHeadersMatchArgs>? Match { get; set; }

        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public RouteSpecHttpRouteMatchHeadersArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If `true`, the match is on the opposite of the `match` method and value. Default is `false`.
        /// </summary>
        [Input("invert")]
        public Input<bool>? Invert { get; set; }

        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        [Input("match")]
        public Input<RouteSpecHttpRouteMatchHeadersMatchGetArgs>? Match { get; set; }

        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public RouteSpecHttpRouteMatchHeadersGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersMatchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The header value sent by the client must match the specified value exactly.
        /// </summary>
        [Input("exact")]
        public Input<string>? Exact { get; set; }

        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("range")]
        public Input<RouteSpecHttpRouteMatchHeadersMatchRangeArgs>? Range { get; set; }

        /// <summary>
        /// The header value sent by the client must include the specified characters.
        /// </summary>
        [Input("regex")]
        public Input<string>? Regex { get; set; }

        /// <summary>
        /// The header value sent by the client must end with the specified characters.
        /// </summary>
        [Input("suffix")]
        public Input<string>? Suffix { get; set; }

        public RouteSpecHttpRouteMatchHeadersMatchArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersMatchGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The header value sent by the client must match the specified value exactly.
        /// </summary>
        [Input("exact")]
        public Input<string>? Exact { get; set; }

        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("range")]
        public Input<RouteSpecHttpRouteMatchHeadersMatchRangeGetArgs>? Range { get; set; }

        /// <summary>
        /// The header value sent by the client must include the specified characters.
        /// </summary>
        [Input("regex")]
        public Input<string>? Regex { get; set; }

        /// <summary>
        /// The header value sent by the client must end with the specified characters.
        /// </summary>
        [Input("suffix")]
        public Input<string>? Suffix { get; set; }

        public RouteSpecHttpRouteMatchHeadersMatchGetArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersMatchRangeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The end of the range.
        /// </summary>
        [Input("end", required: true)]
        public Input<int> End { get; set; } = null!;

        /// <summary>
        /// The start of the range.
        /// </summary>
        [Input("start", required: true)]
        public Input<int> Start { get; set; } = null!;

        public RouteSpecHttpRouteMatchHeadersMatchRangeArgs()
        {
        }
    }

    public sealed class RouteSpecHttpRouteMatchHeadersMatchRangeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The end of the range.
        /// </summary>
        [Input("end", required: true)]
        public Input<int> End { get; set; } = null!;

        /// <summary>
        /// The start of the range.
        /// </summary>
        [Input("start", required: true)]
        public Input<int> Start { get; set; } = null!;

        public RouteSpecHttpRouteMatchHeadersMatchRangeGetArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteActionArgs : Pulumi.ResourceArgs
    {
        [Input("weightedTargets", required: true)]
        private InputList<RouteSpecTcpRouteActionWeightedTargetsArgs>? _weightedTargets;

        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public InputList<RouteSpecTcpRouteActionWeightedTargetsArgs> WeightedTargets
        {
            get => _weightedTargets ?? (_weightedTargets = new InputList<RouteSpecTcpRouteActionWeightedTargetsArgs>());
            set => _weightedTargets = value;
        }

        public RouteSpecTcpRouteActionArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteActionGetArgs : Pulumi.ResourceArgs
    {
        [Input("weightedTargets", required: true)]
        private InputList<RouteSpecTcpRouteActionWeightedTargetsGetArgs>? _weightedTargets;

        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public InputList<RouteSpecTcpRouteActionWeightedTargetsGetArgs> WeightedTargets
        {
            get => _weightedTargets ?? (_weightedTargets = new InputList<RouteSpecTcpRouteActionWeightedTargetsGetArgs>());
            set => _weightedTargets = value;
        }

        public RouteSpecTcpRouteActionGetArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteActionWeightedTargetsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        [Input("virtualNode", required: true)]
        public Input<string> VirtualNode { get; set; } = null!;

        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public RouteSpecTcpRouteActionWeightedTargetsArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteActionWeightedTargetsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        [Input("virtualNode", required: true)]
        public Input<string> VirtualNode { get; set; } = null!;

        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public RouteSpecTcpRouteActionWeightedTargetsGetArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        [Input("action", required: true)]
        public Input<RouteSpecTcpRouteActionArgs> Action { get; set; } = null!;

        public RouteSpecTcpRouteArgs()
        {
        }
    }

    public sealed class RouteSpecTcpRouteGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        [Input("action", required: true)]
        public Input<RouteSpecTcpRouteActionGetArgs> Action { get; set; } = null!;

        public RouteSpecTcpRouteGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class RouteSpec
    {
        /// <summary>
        /// The HTTP routing information for the route.
        /// </summary>
        public readonly RouteSpecHttpRoute? HttpRoute;
        /// <summary>
        /// The priority for the route, between `0` and `1000`.
        /// Routes are matched based on the specified value, where `0` is the highest priority.
        /// </summary>
        public readonly int? Priority;
        /// <summary>
        /// The TCP routing information for the route.
        /// </summary>
        public readonly RouteSpecTcpRoute? TcpRoute;

        [OutputConstructor]
        private RouteSpec(
            RouteSpecHttpRoute? httpRoute,
            int? priority,
            RouteSpecTcpRoute? tcpRoute)
        {
            HttpRoute = httpRoute;
            Priority = priority;
            TcpRoute = tcpRoute;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRoute
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        public readonly RouteSpecHttpRouteAction Action;
        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        public readonly RouteSpecHttpRouteMatch Match;

        [OutputConstructor]
        private RouteSpecHttpRoute(
            RouteSpecHttpRouteAction action,
            RouteSpecHttpRouteMatch match)
        {
            Action = action;
            Match = match;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteAction
    {
        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public readonly ImmutableArray<RouteSpecHttpRouteActionWeightedTargets> WeightedTargets;

        [OutputConstructor]
        private RouteSpecHttpRouteAction(ImmutableArray<RouteSpecHttpRouteActionWeightedTargets> weightedTargets)
        {
            WeightedTargets = weightedTargets;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteActionWeightedTargets
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        public readonly string VirtualNode;
        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private RouteSpecHttpRouteActionWeightedTargets(
            string virtualNode,
            int weight)
        {
            VirtualNode = virtualNode;
            Weight = weight;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteMatch
    {
        /// <summary>
        /// The client request headers to match on.
        /// </summary>
        public readonly ImmutableArray<RouteSpecHttpRouteMatchHeaders> Headers;
        /// <summary>
        /// The client request header method to match on. Valid values: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`.
        /// </summary>
        public readonly string? Method;
        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        public readonly string Prefix;
        /// <summary>
        /// The client request header scheme to match on. Valid values: `http`, `https`.
        /// </summary>
        public readonly string? Scheme;

        [OutputConstructor]
        private RouteSpecHttpRouteMatch(
            ImmutableArray<RouteSpecHttpRouteMatchHeaders> headers,
            string? method,
            string prefix,
            string? scheme)
        {
            Headers = headers;
            Method = method;
            Prefix = prefix;
            Scheme = scheme;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteMatchHeaders
    {
        /// <summary>
        /// If `true`, the match is on the opposite of the `match` method and value. Default is `false`.
        /// </summary>
        public readonly bool? Invert;
        /// <summary>
        /// The method and value to match the header value sent with a request. Specify one match method.
        /// </summary>
        public readonly RouteSpecHttpRouteMatchHeadersMatch? Match;
        /// <summary>
        /// A name for the HTTP header in the client request that will be matched on.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private RouteSpecHttpRouteMatchHeaders(
            bool? invert,
            RouteSpecHttpRouteMatchHeadersMatch? match,
            string name)
        {
            Invert = invert;
            Match = match;
            Name = name;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteMatchHeadersMatch
    {
        /// <summary>
        /// The header value sent by the client must match the specified value exactly.
        /// </summary>
        public readonly string? Exact;
        /// <summary>
        /// The header value sent by the client must begin with the specified characters.
        /// * `range`- (Optional) The object that specifies the range of numbers that the header value sent by the client must be included in.
        /// </summary>
        public readonly string? Prefix;
        public readonly RouteSpecHttpRouteMatchHeadersMatchRange? Range;
        /// <summary>
        /// The header value sent by the client must include the specified characters.
        /// </summary>
        public readonly string? Regex;
        /// <summary>
        /// The header value sent by the client must end with the specified characters.
        /// </summary>
        public readonly string? Suffix;

        [OutputConstructor]
        private RouteSpecHttpRouteMatchHeadersMatch(
            string? exact,
            string? prefix,
            RouteSpecHttpRouteMatchHeadersMatchRange? range,
            string? regex,
            string? suffix)
        {
            Exact = exact;
            Prefix = prefix;
            Range = range;
            Regex = regex;
            Suffix = suffix;
        }
    }

    [OutputType]
    public sealed class RouteSpecHttpRouteMatchHeadersMatchRange
    {
        /// <summary>
        /// The end of the range.
        /// </summary>
        public readonly int End;
        /// <summary>
        /// The start of the range.
        /// </summary>
        public readonly int Start;

        [OutputConstructor]
        private RouteSpecHttpRouteMatchHeadersMatchRange(
            int end,
            int start)
        {
            End = end;
            Start = start;
        }
    }

    [OutputType]
    public sealed class RouteSpecTcpRoute
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        public readonly RouteSpecTcpRouteAction Action;

        [OutputConstructor]
        private RouteSpecTcpRoute(RouteSpecTcpRouteAction action)
        {
            Action = action;
        }
    }

    [OutputType]
    public sealed class RouteSpecTcpRouteAction
    {
        /// <summary>
        /// The targets that traffic is routed to when a request matches the route.
        /// You can specify one or more targets and their relative weights with which to distribute traffic.
        /// </summary>
        public readonly ImmutableArray<RouteSpecTcpRouteActionWeightedTargets> WeightedTargets;

        [OutputConstructor]
        private RouteSpecTcpRouteAction(ImmutableArray<RouteSpecTcpRouteActionWeightedTargets> weightedTargets)
        {
            WeightedTargets = weightedTargets;
        }
    }

    [OutputType]
    public sealed class RouteSpecTcpRouteActionWeightedTargets
    {
        /// <summary>
        /// The virtual node to associate with the weighted target.
        /// </summary>
        public readonly string VirtualNode;
        /// <summary>
        /// The relative weight of the weighted target. An integer between 0 and 100.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private RouteSpecTcpRouteActionWeightedTargets(
            string virtualNode,
            int weight)
        {
            VirtualNode = virtualNode;
            Weight = weight;
        }
    }
    }
}
