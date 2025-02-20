# PasswordScoreInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**suggestions** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.password_score_info import PasswordScoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordScoreInfo from a JSON string
password_score_info_instance = PasswordScoreInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordScoreInfo.to_json())

# convert the object into a dict
password_score_info_dict = password_score_info_instance.to_dict()
# create an instance of PasswordScoreInfo from a dict
password_score_info_from_dict = PasswordScoreInfo.from_dict(password_score_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


