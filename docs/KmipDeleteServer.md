# KmipDeleteServer

kmipDeleteServer is a command that the kmip server (allowed only if it has no clients nor associated items)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_delete_server import KmipDeleteServer

# TODO update the JSON string below
json = "{}"
# create an instance of KmipDeleteServer from a JSON string
kmip_delete_server_instance = KmipDeleteServer.from_json(json)
# print the JSON string representation of the object
print(KmipDeleteServer.to_json())

# convert the object into a dict
kmip_delete_server_dict = kmip_delete_server_instance.to_dict()
# create an instance of KmipDeleteServer from a dict
kmip_delete_server_from_dict = KmipDeleteServer.from_dict(kmip_delete_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


