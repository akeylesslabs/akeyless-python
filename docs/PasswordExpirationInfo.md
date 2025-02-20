# PasswordExpirationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_before_expire** | **int** |  | [optional] 
**days_before_notification** | **int** |  | [optional] 
**days_until_expire** | **int** | r/o calculated parameter | [optional] 
**enable** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.password_expiration_info import PasswordExpirationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordExpirationInfo from a JSON string
password_expiration_info_instance = PasswordExpirationInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordExpirationInfo.to_json())

# convert the object into a dict
password_expiration_info_dict = password_expiration_info_instance.to_dict()
# create an instance of PasswordExpirationInfo from a dict
password_expiration_info_from_dict = PasswordExpirationInfo.from_dict(password_expiration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


