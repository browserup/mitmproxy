# HarEntryResponseContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Size** | **int32** |  | 
**Compression** | Pointer to **int32** |  | [optional] 
**MimeType** | **string** |  | 
**Text** | Pointer to **string** |  | [optional] 
**Encoding** | Pointer to **string** |  | [optional] 
**VideoBufferedPercent** | Pointer to **int64** |  | [optional] [default to -1]
**VideoStallCount** | Pointer to **int64** |  | [optional] [default to -1]
**VideoDecodedByteCount** | Pointer to **int64** |  | [optional] [default to -1]
**VideoWaitingCount** | Pointer to **int64** |  | [optional] [default to -1]
**VideoErrorCount** | Pointer to **int64** |  | [optional] [default to -1]
**VideoDroppedFrames** | Pointer to **int64** |  | [optional] [default to -1]
**VideoTotalFrames** | Pointer to **int64** |  | [optional] [default to -1]
**VideoAudioBytesDecoded** | Pointer to **int64** |  | [optional] [default to -1]
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryResponseContent

`func NewHarEntryResponseContent(size int32, mimeType string, ) *HarEntryResponseContent`

NewHarEntryResponseContent instantiates a new HarEntryResponseContent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryResponseContentWithDefaults

`func NewHarEntryResponseContentWithDefaults() *HarEntryResponseContent`

NewHarEntryResponseContentWithDefaults instantiates a new HarEntryResponseContent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSize

`func (o *HarEntryResponseContent) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *HarEntryResponseContent) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *HarEntryResponseContent) SetSize(v int32)`

SetSize sets Size field to given value.


### GetCompression

`func (o *HarEntryResponseContent) GetCompression() int32`

GetCompression returns the Compression field if non-nil, zero value otherwise.

### GetCompressionOk

`func (o *HarEntryResponseContent) GetCompressionOk() (*int32, bool)`

GetCompressionOk returns a tuple with the Compression field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompression

`func (o *HarEntryResponseContent) SetCompression(v int32)`

SetCompression sets Compression field to given value.

### HasCompression

`func (o *HarEntryResponseContent) HasCompression() bool`

HasCompression returns a boolean if a field has been set.

### GetMimeType

`func (o *HarEntryResponseContent) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *HarEntryResponseContent) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *HarEntryResponseContent) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.


### GetText

`func (o *HarEntryResponseContent) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *HarEntryResponseContent) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *HarEntryResponseContent) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *HarEntryResponseContent) HasText() bool`

HasText returns a boolean if a field has been set.

### GetEncoding

`func (o *HarEntryResponseContent) GetEncoding() string`

GetEncoding returns the Encoding field if non-nil, zero value otherwise.

### GetEncodingOk

`func (o *HarEntryResponseContent) GetEncodingOk() (*string, bool)`

GetEncodingOk returns a tuple with the Encoding field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEncoding

`func (o *HarEntryResponseContent) SetEncoding(v string)`

SetEncoding sets Encoding field to given value.

### HasEncoding

`func (o *HarEntryResponseContent) HasEncoding() bool`

HasEncoding returns a boolean if a field has been set.

### GetVideoBufferedPercent

`func (o *HarEntryResponseContent) GetVideoBufferedPercent() int64`

GetVideoBufferedPercent returns the VideoBufferedPercent field if non-nil, zero value otherwise.

### GetVideoBufferedPercentOk

`func (o *HarEntryResponseContent) GetVideoBufferedPercentOk() (*int64, bool)`

GetVideoBufferedPercentOk returns a tuple with the VideoBufferedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoBufferedPercent

`func (o *HarEntryResponseContent) SetVideoBufferedPercent(v int64)`

SetVideoBufferedPercent sets VideoBufferedPercent field to given value.

### HasVideoBufferedPercent

`func (o *HarEntryResponseContent) HasVideoBufferedPercent() bool`

HasVideoBufferedPercent returns a boolean if a field has been set.

### GetVideoStallCount

`func (o *HarEntryResponseContent) GetVideoStallCount() int64`

GetVideoStallCount returns the VideoStallCount field if non-nil, zero value otherwise.

### GetVideoStallCountOk

`func (o *HarEntryResponseContent) GetVideoStallCountOk() (*int64, bool)`

GetVideoStallCountOk returns a tuple with the VideoStallCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoStallCount

`func (o *HarEntryResponseContent) SetVideoStallCount(v int64)`

SetVideoStallCount sets VideoStallCount field to given value.

### HasVideoStallCount

`func (o *HarEntryResponseContent) HasVideoStallCount() bool`

HasVideoStallCount returns a boolean if a field has been set.

### GetVideoDecodedByteCount

`func (o *HarEntryResponseContent) GetVideoDecodedByteCount() int64`

GetVideoDecodedByteCount returns the VideoDecodedByteCount field if non-nil, zero value otherwise.

### GetVideoDecodedByteCountOk

`func (o *HarEntryResponseContent) GetVideoDecodedByteCountOk() (*int64, bool)`

GetVideoDecodedByteCountOk returns a tuple with the VideoDecodedByteCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoDecodedByteCount

`func (o *HarEntryResponseContent) SetVideoDecodedByteCount(v int64)`

SetVideoDecodedByteCount sets VideoDecodedByteCount field to given value.

### HasVideoDecodedByteCount

`func (o *HarEntryResponseContent) HasVideoDecodedByteCount() bool`

HasVideoDecodedByteCount returns a boolean if a field has been set.

### GetVideoWaitingCount

`func (o *HarEntryResponseContent) GetVideoWaitingCount() int64`

GetVideoWaitingCount returns the VideoWaitingCount field if non-nil, zero value otherwise.

### GetVideoWaitingCountOk

`func (o *HarEntryResponseContent) GetVideoWaitingCountOk() (*int64, bool)`

GetVideoWaitingCountOk returns a tuple with the VideoWaitingCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoWaitingCount

`func (o *HarEntryResponseContent) SetVideoWaitingCount(v int64)`

SetVideoWaitingCount sets VideoWaitingCount field to given value.

### HasVideoWaitingCount

`func (o *HarEntryResponseContent) HasVideoWaitingCount() bool`

HasVideoWaitingCount returns a boolean if a field has been set.

### GetVideoErrorCount

`func (o *HarEntryResponseContent) GetVideoErrorCount() int64`

GetVideoErrorCount returns the VideoErrorCount field if non-nil, zero value otherwise.

### GetVideoErrorCountOk

`func (o *HarEntryResponseContent) GetVideoErrorCountOk() (*int64, bool)`

GetVideoErrorCountOk returns a tuple with the VideoErrorCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoErrorCount

`func (o *HarEntryResponseContent) SetVideoErrorCount(v int64)`

SetVideoErrorCount sets VideoErrorCount field to given value.

### HasVideoErrorCount

`func (o *HarEntryResponseContent) HasVideoErrorCount() bool`

HasVideoErrorCount returns a boolean if a field has been set.

### GetVideoDroppedFrames

`func (o *HarEntryResponseContent) GetVideoDroppedFrames() int64`

GetVideoDroppedFrames returns the VideoDroppedFrames field if non-nil, zero value otherwise.

### GetVideoDroppedFramesOk

`func (o *HarEntryResponseContent) GetVideoDroppedFramesOk() (*int64, bool)`

GetVideoDroppedFramesOk returns a tuple with the VideoDroppedFrames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoDroppedFrames

`func (o *HarEntryResponseContent) SetVideoDroppedFrames(v int64)`

SetVideoDroppedFrames sets VideoDroppedFrames field to given value.

### HasVideoDroppedFrames

`func (o *HarEntryResponseContent) HasVideoDroppedFrames() bool`

HasVideoDroppedFrames returns a boolean if a field has been set.

### GetVideoTotalFrames

`func (o *HarEntryResponseContent) GetVideoTotalFrames() int64`

GetVideoTotalFrames returns the VideoTotalFrames field if non-nil, zero value otherwise.

### GetVideoTotalFramesOk

`func (o *HarEntryResponseContent) GetVideoTotalFramesOk() (*int64, bool)`

GetVideoTotalFramesOk returns a tuple with the VideoTotalFrames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoTotalFrames

`func (o *HarEntryResponseContent) SetVideoTotalFrames(v int64)`

SetVideoTotalFrames sets VideoTotalFrames field to given value.

### HasVideoTotalFrames

`func (o *HarEntryResponseContent) HasVideoTotalFrames() bool`

HasVideoTotalFrames returns a boolean if a field has been set.

### GetVideoAudioBytesDecoded

`func (o *HarEntryResponseContent) GetVideoAudioBytesDecoded() int64`

GetVideoAudioBytesDecoded returns the VideoAudioBytesDecoded field if non-nil, zero value otherwise.

### GetVideoAudioBytesDecodedOk

`func (o *HarEntryResponseContent) GetVideoAudioBytesDecodedOk() (*int64, bool)`

GetVideoAudioBytesDecodedOk returns a tuple with the VideoAudioBytesDecoded field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideoAudioBytesDecoded

`func (o *HarEntryResponseContent) SetVideoAudioBytesDecoded(v int64)`

SetVideoAudioBytesDecoded sets VideoAudioBytesDecoded field to given value.

### HasVideoAudioBytesDecoded

`func (o *HarEntryResponseContent) HasVideoAudioBytesDecoded() bool`

HasVideoAudioBytesDecoded returns a boolean if a field has been set.

### GetComment

`func (o *HarEntryResponseContent) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryResponseContent) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryResponseContent) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryResponseContent) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


