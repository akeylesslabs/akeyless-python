# EsmList

esmList is a command that lists the secrets of an External Secrets Manager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esm_name** | **str** | Name of the External Secrets Manager item | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.esm_list import EsmList

# TODO update the JSON string below
json = "{}"
# create an instance of EsmList from a JSON string
esm_list_instance = EsmList.from_json(json)
# print the JSON string representation of the object
print(EsmList.to_json())

# convert the object into a dict
esm_list_dict = esm_list_instance.to_dict()
# create an instance of EsmList from a dict
esm_list_from_dict = EsmList.from_dict(esm_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


