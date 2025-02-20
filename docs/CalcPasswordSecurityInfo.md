# CalcPasswordSecurityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**min_length** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.calc_password_security_info import CalcPasswordSecurityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CalcPasswordSecurityInfo from a JSON string
calc_password_security_info_instance = CalcPasswordSecurityInfo.from_json(json)
# print the JSON string representation of the object
print(CalcPasswordSecurityInfo.to_json())

# convert the object into a dict
calc_password_security_info_dict = calc_password_security_info_instance.to_dict()
# create an instance of CalcPasswordSecurityInfo from a dict
calc_password_security_info_from_dict = CalcPasswordSecurityInfo.from_dict(calc_password_security_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


