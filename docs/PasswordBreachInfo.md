# PasswordBreachInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_check_date** | **datetime** |  | [optional] 
**breach_count** | **int** |  | [optional] 
**breach_suggestions** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from akeyless.models.password_breach_info import PasswordBreachInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordBreachInfo from a JSON string
password_breach_info_instance = PasswordBreachInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordBreachInfo.to_json())

# convert the object into a dict
password_breach_info_dict = password_breach_info_instance.to_dict()
# create an instance of PasswordBreachInfo from a dict
password_breach_info_from_dict = PasswordBreachInfo.from_dict(password_breach_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


