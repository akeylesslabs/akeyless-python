# RotatedSecretList

rotatedSecretList is a command that returns a list of rotated secrets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotated_secret_list import RotatedSecretList

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretList from a JSON string
rotated_secret_list_instance = RotatedSecretList.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretList.to_json())

# convert the object into a dict
rotated_secret_list_dict = rotated_secret_list_instance.to_dict()
# create an instance of RotatedSecretList from a dict
rotated_secret_list_from_dict = RotatedSecretList.from_dict(rotated_secret_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


