# RotatedSecretDelete

rotatedSecretDelete is a command that deletes a rotated secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The specific version you want to delete, -1&#x3D;entire item with all versions (default) | [optional] [default to -1]

## Example

```python
from akeyless.models.rotated_secret_delete import RotatedSecretDelete

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretDelete from a JSON string
rotated_secret_delete_instance = RotatedSecretDelete.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretDelete.to_json())

# convert the object into a dict
rotated_secret_delete_dict = rotated_secret_delete_instance.to_dict()
# create an instance of RotatedSecretDelete from a dict
rotated_secret_delete_from_dict = RotatedSecretDelete.from_dict(rotated_secret_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


