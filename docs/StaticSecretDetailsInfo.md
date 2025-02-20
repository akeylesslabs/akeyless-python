# StaticSecretDetailsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | StaticSecretFormat defines the format of static secret (e.g. Text) | [optional] 
**max_versions** | **int** |  | [optional] 
**notify_on_change_event** | **bool** |  | [optional] 
**password_security_info** | [**PasswordSecurityInfo**](PasswordSecurityInfo.md) |  | [optional] 
**username** | **str** |  | [optional] 
**website** | **str** | deprecated | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.static_secret_details_info import StaticSecretDetailsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSecretDetailsInfo from a JSON string
static_secret_details_info_instance = StaticSecretDetailsInfo.from_json(json)
# print the JSON string representation of the object
print(StaticSecretDetailsInfo.to_json())

# convert the object into a dict
static_secret_details_info_dict = static_secret_details_info_instance.to_dict()
# create an instance of StaticSecretDetailsInfo from a dict
static_secret_details_info_from_dict = StaticSecretDetailsInfo.from_dict(static_secret_details_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


