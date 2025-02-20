# KmipSetServerState

kmipSetServerState is a command that sets the environment state to active/inactive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**state** | **str** |  | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_set_server_state import KmipSetServerState

# TODO update the JSON string below
json = "{}"
# create an instance of KmipSetServerState from a JSON string
kmip_set_server_state_instance = KmipSetServerState.from_json(json)
# print the JSON string representation of the object
print(KmipSetServerState.to_json())

# convert the object into a dict
kmip_set_server_state_dict = kmip_set_server_state_instance.to_dict()
# create an instance of KmipSetServerState from a dict
kmip_set_server_state_from_dict = KmipSetServerState.from_dict(kmip_set_server_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


