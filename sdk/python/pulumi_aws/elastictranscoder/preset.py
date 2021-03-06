# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Preset(pulumi.CustomResource):
    arn: pulumi.Output[str]
    audio: pulumi.Output[dict]
    """
    Audio parameters object (documented below).

      * `audioPackingMode` (`str`) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
      * `bitRate` (`str`) - The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.
      * `channels` (`str`) - The number of audio channels in the output file
      * `codec` (`str`) - The audio codec for the output file. Valid values are `AAC`, `flac`, `mp2`, `mp3`, `pcm`, and `vorbis`.
      * `sampleRate` (`str`) - The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
    """
    audio_codec_options: pulumi.Output[dict]
    """
    Codec options for the audio parameters (documented below)

      * `bitDepth` (`str`) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
      * `bitOrder` (`str`) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
      * `profile` (`str`) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
      * `signed` (`str`) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
    """
    container: pulumi.Output[str]
    """
    The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
    """
    description: pulumi.Output[str]
    """
    A description of the preset (maximum 255 characters)
    """
    name: pulumi.Output[str]
    """
    The name of the preset. (maximum 40 characters)
    """
    thumbnails: pulumi.Output[dict]
    """
    Thumbnail parameters object (documented below)

      * `aspectRatio` (`str`) - The aspect ratio of thumbnails. The following values are valid: auto, 1:1, 4:3, 3:2, 16:9
      * `format` (`str`) - The format of thumbnails, if any. Valid formats are jpg and png.
      * `interval` (`str`) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
      * `maxHeight` (`str`) - The maximum height of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
      * `maxWidth` (`str`) - The maximum width of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
      * `paddingPolicy` (`str`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.
      * `resolution` (`str`) - The width and height of thumbnail files in pixels, in the format WidthxHeight, where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object. (To better control resolution and aspect ratio of thumbnails, we recommend that you use the thumbnail values `max_width`, `max_height`, `sizing_policy`, and `padding_policy` instead of `resolution` and `aspect_ratio`. The two groups of settings are mutually exclusive. Do not use them together)
      * `sizingPolicy` (`str`) - A value that controls scaling of thumbnails. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, and `ShrinkToFill`.
    """
    type: pulumi.Output[str]
    video: pulumi.Output[dict]
    """
    Video parameters object (documented below)

      * `aspectRatio` (`str`) - The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
      * `bitRate` (`str`) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
      * `codec` (`str`) - The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
      * `displayAspectRatio` (`str`) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
      * `fixedGop` (`str`) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
      * `frameRate` (`str`) - The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
      * `keyframesMaxDist` (`str`) - The maximum number of frames between key frames. Not applicable for containers of type gif.
      * `maxFrameRate` (`str`) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
      * `maxHeight` (`str`) - The maximum height of the output video in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072, inclusive.
      * `maxWidth` (`str`) - The maximum width of the output video in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096, inclusive.
      * `paddingPolicy` (`str`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
      * `resolution` (`str`) - The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
      * `sizingPolicy` (`str`) - A value that controls scaling of the output video. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, `ShrinkToFill`.
    """
    video_codec_options: pulumi.Output[dict]
    """
    Codec options for the video parameters
    """
    video_watermarks: pulumi.Output[list]
    """
    Watermark parameters for the video parameters (documented below)

      * `horizontalAlign` (`str`) - The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
      * `horizontalOffset` (`str`) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
      * `id` (`str`) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
      * `maxHeight` (`str`) - The maximum height of the watermark.
      * `maxWidth` (`str`) - The maximum width of the watermark.
      * `opacity` (`str`) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
      * `sizingPolicy` (`str`) - A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
      * `target` (`str`) - A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
      * `verticalAlign` (`str`) - The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
      * `verticalOffset` (`str`) - The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
    """
    def __init__(__self__, resource_name, opts=None, audio=None, audio_codec_options=None, container=None, description=None, name=None, thumbnails=None, type=None, video=None, video_codec_options=None, video_watermarks=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an Elastic Transcoder preset resource.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.elastictranscoder.Preset("bar",
            audio={
                "audioPackingMode": "SingleTrack",
                "bitRate": 96,
                "channels": 2,
                "codec": "AAC",
                "sampleRate": 44100,
            },
            audio_codec_options={
                "profile": "AAC-LC",
            },
            container="mp4",
            description="Sample Preset",
            thumbnails={
                "format": "png",
                "interval": 120,
                "maxHeight": "auto",
                "maxWidth": "auto",
                "paddingPolicy": "Pad",
                "sizingPolicy": "Fit",
            },
            video={
                "bitRate": "1600",
                "codec": "H.264",
                "displayAspectRatio": "16:9",
                "fixedGop": "false",
                "frameRate": "auto",
                "keyframesMaxDist": 240,
                "maxFrameRate": "60",
                "maxHeight": "auto",
                "maxWidth": "auto",
                "paddingPolicy": "Pad",
                "sizingPolicy": "Fit",
            },
            video_codec_options={
                "ColorSpaceConversionMode": "None",
                "InterlacedMode": "Progressive",
                "Level": "2.2",
                "MaxReferenceFrames": 3,
                "Profile": "main",
            },
            video_watermarks=[{
                "horizontalAlign": "Right",
                "horizontalOffset": "10px",
                "id": "Test",
                "maxHeight": "20%",
                "maxWidth": "20%",
                "opacity": "55.5",
                "sizingPolicy": "ShrinkToFit",
                "target": "Content",
                "verticalAlign": "Bottom",
                "verticalOffset": "10px",
            }])
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] audio: Audio parameters object (documented below).
        :param pulumi.Input[dict] audio_codec_options: Codec options for the audio parameters (documented below)
        :param pulumi.Input[str] container: The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
        :param pulumi.Input[str] description: A description of the preset (maximum 255 characters)
        :param pulumi.Input[str] name: The name of the preset. (maximum 40 characters)
        :param pulumi.Input[dict] thumbnails: Thumbnail parameters object (documented below)
        :param pulumi.Input[dict] video: Video parameters object (documented below)
        :param pulumi.Input[dict] video_codec_options: Codec options for the video parameters
        :param pulumi.Input[list] video_watermarks: Watermark parameters for the video parameters (documented below)

        The **audio** object supports the following:

          * `audioPackingMode` (`pulumi.Input[str]`) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
          * `bitRate` (`pulumi.Input[str]`) - The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.
          * `channels` (`pulumi.Input[str]`) - The number of audio channels in the output file
          * `codec` (`pulumi.Input[str]`) - The audio codec for the output file. Valid values are `AAC`, `flac`, `mp2`, `mp3`, `pcm`, and `vorbis`.
          * `sampleRate` (`pulumi.Input[str]`) - The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`

        The **audio_codec_options** object supports the following:

          * `bitDepth` (`pulumi.Input[str]`) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
          * `bitOrder` (`pulumi.Input[str]`) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
          * `profile` (`pulumi.Input[str]`) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
          * `signed` (`pulumi.Input[str]`) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)

        The **thumbnails** object supports the following:

          * `aspectRatio` (`pulumi.Input[str]`) - The aspect ratio of thumbnails. The following values are valid: auto, 1:1, 4:3, 3:2, 16:9
          * `format` (`pulumi.Input[str]`) - The format of thumbnails, if any. Valid formats are jpg and png.
          * `interval` (`pulumi.Input[str]`) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
          * `paddingPolicy` (`pulumi.Input[str]`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.
          * `resolution` (`pulumi.Input[str]`) - The width and height of thumbnail files in pixels, in the format WidthxHeight, where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object. (To better control resolution and aspect ratio of thumbnails, we recommend that you use the thumbnail values `max_width`, `max_height`, `sizing_policy`, and `padding_policy` instead of `resolution` and `aspect_ratio`. The two groups of settings are mutually exclusive. Do not use them together)
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of thumbnails. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, and `ShrinkToFill`.

        The **video** object supports the following:

          * `aspectRatio` (`pulumi.Input[str]`) - The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
          * `bitRate` (`pulumi.Input[str]`) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
          * `codec` (`pulumi.Input[str]`) - The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
          * `displayAspectRatio` (`pulumi.Input[str]`) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
          * `fixedGop` (`pulumi.Input[str]`) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
          * `frameRate` (`pulumi.Input[str]`) - The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
          * `keyframesMaxDist` (`pulumi.Input[str]`) - The maximum number of frames between key frames. Not applicable for containers of type gif.
          * `maxFrameRate` (`pulumi.Input[str]`) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of the output video in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072, inclusive.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of the output video in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096, inclusive.
          * `paddingPolicy` (`pulumi.Input[str]`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
          * `resolution` (`pulumi.Input[str]`) - The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of the output video. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, `ShrinkToFill`.

        The **video_watermarks** object supports the following:

          * `horizontalAlign` (`pulumi.Input[str]`) - The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
          * `horizontalOffset` (`pulumi.Input[str]`) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
          * `id` (`pulumi.Input[str]`) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of the watermark.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of the watermark.
          * `opacity` (`pulumi.Input[str]`) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
          * `target` (`pulumi.Input[str]`) - A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
          * `verticalAlign` (`pulumi.Input[str]`) - The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
          * `verticalOffset` (`pulumi.Input[str]`) - The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['audio'] = audio
            __props__['audio_codec_options'] = audio_codec_options
            if container is None:
                raise TypeError("Missing required property 'container'")
            __props__['container'] = container
            __props__['description'] = description
            __props__['name'] = name
            __props__['thumbnails'] = thumbnails
            __props__['type'] = type
            __props__['video'] = video
            __props__['video_codec_options'] = video_codec_options
            __props__['video_watermarks'] = video_watermarks
            __props__['arn'] = None
        super(Preset, __self__).__init__(
            'aws:elastictranscoder/preset:Preset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, audio=None, audio_codec_options=None, container=None, description=None, name=None, thumbnails=None, type=None, video=None, video_codec_options=None, video_watermarks=None):
        """
        Get an existing Preset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] audio: Audio parameters object (documented below).
        :param pulumi.Input[dict] audio_codec_options: Codec options for the audio parameters (documented below)
        :param pulumi.Input[str] container: The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
        :param pulumi.Input[str] description: A description of the preset (maximum 255 characters)
        :param pulumi.Input[str] name: The name of the preset. (maximum 40 characters)
        :param pulumi.Input[dict] thumbnails: Thumbnail parameters object (documented below)
        :param pulumi.Input[dict] video: Video parameters object (documented below)
        :param pulumi.Input[dict] video_codec_options: Codec options for the video parameters
        :param pulumi.Input[list] video_watermarks: Watermark parameters for the video parameters (documented below)

        The **audio** object supports the following:

          * `audioPackingMode` (`pulumi.Input[str]`) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
          * `bitRate` (`pulumi.Input[str]`) - The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.
          * `channels` (`pulumi.Input[str]`) - The number of audio channels in the output file
          * `codec` (`pulumi.Input[str]`) - The audio codec for the output file. Valid values are `AAC`, `flac`, `mp2`, `mp3`, `pcm`, and `vorbis`.
          * `sampleRate` (`pulumi.Input[str]`) - The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`

        The **audio_codec_options** object supports the following:

          * `bitDepth` (`pulumi.Input[str]`) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
          * `bitOrder` (`pulumi.Input[str]`) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
          * `profile` (`pulumi.Input[str]`) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
          * `signed` (`pulumi.Input[str]`) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)

        The **thumbnails** object supports the following:

          * `aspectRatio` (`pulumi.Input[str]`) - The aspect ratio of thumbnails. The following values are valid: auto, 1:1, 4:3, 3:2, 16:9
          * `format` (`pulumi.Input[str]`) - The format of thumbnails, if any. Valid formats are jpg and png.
          * `interval` (`pulumi.Input[str]`) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
          * `paddingPolicy` (`pulumi.Input[str]`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.
          * `resolution` (`pulumi.Input[str]`) - The width and height of thumbnail files in pixels, in the format WidthxHeight, where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object. (To better control resolution and aspect ratio of thumbnails, we recommend that you use the thumbnail values `max_width`, `max_height`, `sizing_policy`, and `padding_policy` instead of `resolution` and `aspect_ratio`. The two groups of settings are mutually exclusive. Do not use them together)
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of thumbnails. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, and `ShrinkToFill`.

        The **video** object supports the following:

          * `aspectRatio` (`pulumi.Input[str]`) - The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
          * `bitRate` (`pulumi.Input[str]`) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
          * `codec` (`pulumi.Input[str]`) - The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
          * `displayAspectRatio` (`pulumi.Input[str]`) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
          * `fixedGop` (`pulumi.Input[str]`) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
          * `frameRate` (`pulumi.Input[str]`) - The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
          * `keyframesMaxDist` (`pulumi.Input[str]`) - The maximum number of frames between key frames. Not applicable for containers of type gif.
          * `maxFrameRate` (`pulumi.Input[str]`) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of the output video in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072, inclusive.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of the output video in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096, inclusive.
          * `paddingPolicy` (`pulumi.Input[str]`) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
          * `resolution` (`pulumi.Input[str]`) - The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of the output video. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, `ShrinkToFill`.

        The **video_watermarks** object supports the following:

          * `horizontalAlign` (`pulumi.Input[str]`) - The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
          * `horizontalOffset` (`pulumi.Input[str]`) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
          * `id` (`pulumi.Input[str]`) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
          * `maxHeight` (`pulumi.Input[str]`) - The maximum height of the watermark.
          * `maxWidth` (`pulumi.Input[str]`) - The maximum width of the watermark.
          * `opacity` (`pulumi.Input[str]`) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
          * `sizingPolicy` (`pulumi.Input[str]`) - A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
          * `target` (`pulumi.Input[str]`) - A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
          * `verticalAlign` (`pulumi.Input[str]`) - The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
          * `verticalOffset` (`pulumi.Input[str]`) - The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["audio"] = audio
        __props__["audio_codec_options"] = audio_codec_options
        __props__["container"] = container
        __props__["description"] = description
        __props__["name"] = name
        __props__["thumbnails"] = thumbnails
        __props__["type"] = type
        __props__["video"] = video
        __props__["video_codec_options"] = video_codec_options
        __props__["video_watermarks"] = video_watermarks
        return Preset(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

