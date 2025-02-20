# KmipListClients


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_list_clients import KmipListClients

# TODO update the JSON string below
json = "{}"
# create an instance of KmipListClients from a JSON string
kmip_list_clients_instance = KmipListClients.from_json(json)
# print the JSON string representation of the object
print(KmipListClients.to_json())

# convert the object into a dict
kmip_list_clients_dict = kmip_list_clients_instance.to_dict()
# create an instance of KmipListClients from a dict
kmip_list_clients_from_dict = KmipListClients.from_dict(kmip_list_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


