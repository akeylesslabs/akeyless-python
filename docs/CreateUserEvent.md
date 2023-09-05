# CreateUserEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **list[str]** | List of the required capabilities options: [read, update, delete,sra_transparently_connect]. Relevant only for request-access event types | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | 
**item_name** | **str** | Event item name | 
**item_type** | **str** | Event item type can be either \&quot;target\&quot; or type of item eg \&quot;static_secret\&quot;/\&quot;dynamic_secret\&quot; To get type of some item run &#x60;akeyless describe-item -n {ITEM_NAME} --jq-expression .item_type&#x60; | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**request_access_ttl** | **int** | TTL in minutes for how long to grant the requested access | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


