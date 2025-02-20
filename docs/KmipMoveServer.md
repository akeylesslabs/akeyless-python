# KmipMoveServer

kmipMoveServer is a command that Moves the root location of the kmip server and all associated items to a new root location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**new_root** | **str** | New root for the kmip server | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_move_server import KmipMoveServer

# TODO update the JSON string below
json = "{}"
# create an instance of KmipMoveServer from a JSON string
kmip_move_server_instance = KmipMoveServer.from_json(json)
# print the JSON string representation of the object
print(KmipMoveServer.to_json())

# convert the object into a dict
kmip_move_server_dict = kmip_move_server_instance.to_dict()
# create an instance of KmipMoveServer from a dict
kmip_move_server_from_dict = KmipMoveServer.from_dict(kmip_move_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


