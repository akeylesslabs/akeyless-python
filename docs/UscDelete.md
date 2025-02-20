# UscDelete

uscDelete is a command that deletes a secret from a Universal Secrets Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**namespace** | **str** | The namespace (relevant for Hashi vault target) | [optional] 
**secret_id** | **str** | The universal secrets id (or name, for AWS, Azure, K8s or Hashi vault targets) to delete | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Name of the Universal Secrets Connector item | 

## Example

```python
from akeyless.models.usc_delete import UscDelete

# TODO update the JSON string below
json = "{}"
# create an instance of UscDelete from a JSON string
usc_delete_instance = UscDelete.from_json(json)
# print the JSON string representation of the object
print(UscDelete.to_json())

# convert the object into a dict
usc_delete_dict = usc_delete_instance.to_dict()
# create an instance of UscDelete from a dict
usc_delete_from_dict = UscDelete.from_dict(usc_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


