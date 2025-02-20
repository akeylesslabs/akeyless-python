# RotateSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotate_all_services_boolean** | **bool** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Secret name (Rotated Secret or Custom Dynamic Secret) | 
**rotate_all_services** | **str** | Rotate all associated services | [optional] [default to 'false']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotate_secret import RotateSecret

# TODO update the JSON string below
json = "{}"
# create an instance of RotateSecret from a JSON string
rotate_secret_instance = RotateSecret.from_json(json)
# print the JSON string representation of the object
print(RotateSecret.to_json())

# convert the object into a dict
rotate_secret_dict = rotate_secret_instance.to_dict()
# create an instance of RotateSecret from a dict
rotate_secret_from_dict = RotateSecret.from_dict(rotate_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


