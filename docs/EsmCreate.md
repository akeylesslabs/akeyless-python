# EsmCreate

esmCreate is a command that creates a new secret in an External Secrets Manager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_value** | **bool** | Use this option if the external secret value is a base64 encoded binary | [optional] 
**description** | **str** | Description of the external secret | [optional] 
**esm_name** | **str** | Name of the External Secrets Manager item | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**secret_name** | **str** | Name for the new external secret | 
**tags** | **Dict[str, str]** | Tags for the external secret | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**value** | **str** | Value of the external secret item, either text or base64 encoded binary | 

## Example

```python
from akeyless.models.esm_create import EsmCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EsmCreate from a JSON string
esm_create_instance = EsmCreate.from_json(json)
# print the JSON string representation of the object
print(EsmCreate.to_json())

# convert the object into a dict
esm_create_dict = esm_create_instance.to_dict()
# create an instance of EsmCreate from a dict
esm_create_from_dict = EsmCreate.from_dict(esm_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


