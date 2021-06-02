# DeleteItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_immediately** | **bool** | When delete-in-days&#x3D;-1, must be set | [optional] [default to False]
**delete_in_days** | **int** | The number of days to wait before deleting the item (relevant for keys only) | [optional] [default to 7]
**name** | **str** | Item name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 
**version** | **int** | The specific version you want to delete - 0&#x3D;last version, -1&#x3D;entire item with all versions (default) | [optional] [default to -1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


