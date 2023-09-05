# GetLastUserEventStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | 
**item_name** | **str** | Event item name | 
**item_type** | **str** | Event item type can be either \&quot;target\&quot; or type of item eg \&quot;static_secret\&quot;/\&quot;dynamic_secret\&quot; To get type of some item run &#x60;akeyless describe-item -n {ITEM_NAME} --jq-expression .item_type&#x60; | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**time_back** | **str** | The time back to search the event, can be passed as string representation. For example if the value is \&quot;5m\&quot; we will return the last user event issued in the last 5 minutes By default we will search without any time boundary | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


