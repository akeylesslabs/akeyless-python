# UscUpdate

uscUpdate is a command that updates a secret in a Universal Secrets Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_value** | **bool** | Use this option if the universal secrets value is a base64 encoded binary | [optional] 
**description** | **str** | Description of the universal secrets | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**namespace** | **str** | The namespace (relevant for Hashi vault target) | [optional] 
**secret_id** | **str** | The universal secrets id (or name, for AWS, Azure, K8s or Hashi vault targets) to update | 
**tags** | **Dict[str, str]** | Tags for the universal secrets | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Name of the Universal Secrets Connector item | 
**value** | **str** | Value of the universal secrets item, either text or base64 encoded binary | 

## Example

```python
from akeyless.models.usc_update import UscUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UscUpdate from a JSON string
usc_update_instance = UscUpdate.from_json(json)
# print the JSON string representation of the object
print(UscUpdate.to_json())

# convert the object into a dict
usc_update_dict = usc_update_instance.to_dict()
# create an instance of UscUpdate from a dict
usc_update_from_dict = UscUpdate.from_dict(usc_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


