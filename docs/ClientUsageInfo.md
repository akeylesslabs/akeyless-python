# ClientUsageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 
**auth_method_name** | **str** |  | [optional] 
**client_unique_id** | **str** |  | [optional] 
**exceeded_clients** | **int** |  | [optional] 

## Example

```python
from akeyless.models.client_usage_info import ClientUsageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageInfo from a JSON string
client_usage_info_instance = ClientUsageInfo.from_json(json)
# print the JSON string representation of the object
print(ClientUsageInfo.to_json())

# convert the object into a dict
client_usage_info_dict = client_usage_info_instance.to_dict()
# create an instance of ClientUsageInfo from a dict
client_usage_info_from_dict = ClientUsageInfo.from_dict(client_usage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


