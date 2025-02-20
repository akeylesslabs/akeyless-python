# UidGenerateToken

uidGenerateToken is a command that generates a new token using Akeyless Universal Identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** | The universal identity auth method name | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.uid_generate_token import UidGenerateToken

# TODO update the JSON string below
json = "{}"
# create an instance of UidGenerateToken from a JSON string
uid_generate_token_instance = UidGenerateToken.from_json(json)
# print the JSON string representation of the object
print(UidGenerateToken.to_json())

# convert the object into a dict
uid_generate_token_dict = uid_generate_token_instance.to_dict()
# create an instance of UidGenerateToken from a dict
uid_generate_token_from_dict = UidGenerateToken.from_dict(uid_generate_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


