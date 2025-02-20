# ResetAccessKey

resetAccessKey is a command that resets an access key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.reset_access_key import ResetAccessKey

# TODO update the JSON string below
json = "{}"
# create an instance of ResetAccessKey from a JSON string
reset_access_key_instance = ResetAccessKey.from_json(json)
# print the JSON string representation of the object
print(ResetAccessKey.to_json())

# convert the object into a dict
reset_access_key_dict = reset_access_key_instance.to_dict()
# create an instance of ResetAccessKey from a dict
reset_access_key_from_dict = ResetAccessKey.from_dict(reset_access_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


