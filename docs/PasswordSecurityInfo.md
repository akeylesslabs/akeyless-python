# PasswordSecurityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_info** | [**PasswordBreachInfo**](PasswordBreachInfo.md) |  | [optional] 
**score_info** | [**PasswordScoreInfo**](PasswordScoreInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.password_security_info import PasswordSecurityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSecurityInfo from a JSON string
password_security_info_instance = PasswordSecurityInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordSecurityInfo.to_json())

# convert the object into a dict
password_security_info_dict = password_security_info_instance.to_dict()
# create an instance of PasswordSecurityInfo from a dict
password_security_info_from_dict = PasswordSecurityInfo.from_dict(password_security_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


