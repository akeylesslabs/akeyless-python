# PasswordPolicyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_length** | **int** |  | [optional] 
**use_capital_letters** | **bool** |  | [optional] 
**use_lower_letters** | **bool** |  | [optional] 
**use_numbers** | **bool** |  | [optional] 
**use_special_characters** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.password_policy_info import PasswordPolicyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyInfo from a JSON string
password_policy_info_instance = PasswordPolicyInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyInfo.to_json())

# convert the object into a dict
password_policy_info_dict = password_policy_info_instance.to_dict()
# create an instance of PasswordPolicyInfo from a dict
password_policy_info_from_dict = PasswordPolicyInfo.from_dict(password_policy_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


