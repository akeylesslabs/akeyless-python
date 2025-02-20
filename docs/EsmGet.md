# EsmGet

esmGet is a command that gets the value and interal details of a secret from an External Secrets Manager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esm_name** | **str** | Name of the External Secrets Manager item | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**secret_id** | **str** | The secret id (or name, for AWS, Azure or K8s targets) to get from the External Secrets Manager | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.esm_get import EsmGet

# TODO update the JSON string below
json = "{}"
# create an instance of EsmGet from a JSON string
esm_get_instance = EsmGet.from_json(json)
# print the JSON string representation of the object
print(EsmGet.to_json())

# convert the object into a dict
esm_get_dict = esm_get_instance.to_dict()
# create an instance of EsmGet from a dict
esm_get_from_dict = EsmGet.from_dict(esm_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


