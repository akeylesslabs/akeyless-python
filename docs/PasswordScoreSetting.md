# PasswordScoreSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.password_score_setting import PasswordScoreSetting

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordScoreSetting from a JSON string
password_score_setting_instance = PasswordScoreSetting.from_json(json)
# print the JSON string representation of the object
print(PasswordScoreSetting.to_json())

# convert the object into a dict
password_score_setting_dict = password_score_setting_instance.to_dict()
# create an instance of PasswordScoreSetting from a dict
password_score_setting_from_dict = PasswordScoreSetting.from_dict(password_score_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


