# EsmDelete

esmDelete is a command that deletes a secret from an External Secrets Manager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esm_name** | **str** | Name of the External Secrets Manager item | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**secret_id** | **str** | The external secret id (or name, for AWS, Azure or K8s targets) to delete | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.esm_delete import EsmDelete

# TODO update the JSON string below
json = "{}"
# create an instance of EsmDelete from a JSON string
esm_delete_instance = EsmDelete.from_json(json)
# print the JSON string representation of the object
print(EsmDelete.to_json())

# convert the object into a dict
esm_delete_dict = esm_delete_instance.to_dict()
# create an instance of EsmDelete from a dict
esm_delete_from_dict = EsmDelete.from_dict(esm_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


