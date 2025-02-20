# UscGet

uscGet is a command that gets the value and internal details of a secret from a Universal Secrets Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**namespace** | **str** | The namespace (relevant for Hashi vault target) | [optional] 
**secret_id** | **str** | The secret id (or name, for AWS, Azure, K8s or Hashi vault targets) to get from the Universal Secrets Connector | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Name of the Universal Secrets Connector item | 
**version_id** | **str** | The version id (if not specified, will retrieve the last version) | [optional] 

## Example

```python
from akeyless.models.usc_get import UscGet

# TODO update the JSON string below
json = "{}"
# create an instance of UscGet from a JSON string
usc_get_instance = UscGet.from_json(json)
# print the JSON string representation of the object
print(UscGet.to_json())

# convert the object into a dict
usc_get_dict = usc_get_instance.to_dict()
# create an instance of UscGet from a dict
usc_get_from_dict = UscGet.from_dict(usc_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


