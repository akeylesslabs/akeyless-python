# AzureStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**storage_account** | **str** |  | [optional] 
**storage_container_name** | **str** |  | [optional] 
**tenant_id** | **str** | creds | [optional] 

## Example

```python
from akeyless.models.azure_storage import AzureStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AzureStorage from a JSON string
azure_storage_instance = AzureStorage.from_json(json)
# print the JSON string representation of the object
print(AzureStorage.to_json())

# convert the object into a dict
azure_storage_dict = azure_storage_instance.to_dict()
# create an instance of AzureStorage from a dict
azure_storage_from_dict = AzureStorage.from_dict(azure_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


