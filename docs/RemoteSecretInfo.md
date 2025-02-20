# RemoteSecretInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_error** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**secret_id** | **str** |  | [optional] 
**secret_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.remote_secret_info import RemoteSecretInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSecretInfo from a JSON string
remote_secret_info_instance = RemoteSecretInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteSecretInfo.to_json())

# convert the object into a dict
remote_secret_info_dict = remote_secret_info_instance.to_dict()
# create an instance of RemoteSecretInfo from a dict
remote_secret_info_from_dict = RemoteSecretInfo.from_dict(remote_secret_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


