# ListSraSessionsOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_gateways** | [**list[GatewayNameInfo]**](GatewayNameInfo.md) | Gateways whose sessions the caller may see in full. Omitted when the request asks for own sessions only, and when it carries a pagination token | [optional] 
**next_page** | **str** | Cursor for the following page, sent back as the pagination token. Empty when the result set is exhausted, so stop when it is empty rather than waiting for the field to disappear | [optional] 
**sessions** | [**list[SraSessionEntryOut]**](SraSessionEntryOut.md) | The requested page of sessions, newest first by start time then session id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


