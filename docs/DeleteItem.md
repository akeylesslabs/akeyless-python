# DeleteItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_immediately** | **bool** | When delete-in-days&#x3D;-1, must be set | [optional] [default to False]
**delete_in_days** | **int** | The number of days to wait before deleting the item (relevant for keys only) | [optional] [default to 7]
**name** | **str** | Item name | 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The specific version you want to delete - 0&#x3D;last version, -1&#x3D;entire item with all versions (default) | [optional] [default to -1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


