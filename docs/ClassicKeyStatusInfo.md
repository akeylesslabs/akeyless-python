# ClassicKeyStatusInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_date** | **datetime** |  | [optional] 
**last_error** | **str** |  | [optional] 
**last_status** | **str** | ClassicKeyTargetStatus defines status of classic key target | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.classic_key_status_info import ClassicKeyStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClassicKeyStatusInfo from a JSON string
classic_key_status_info_instance = ClassicKeyStatusInfo.from_json(json)
# print the JSON string representation of the object
print(ClassicKeyStatusInfo.to_json())

# convert the object into a dict
classic_key_status_info_dict = classic_key_status_info_instance.to_dict()
# create an instance of ClassicKeyStatusInfo from a dict
classic_key_status_info_from_dict = ClassicKeyStatusInfo.from_dict(classic_key_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


