# ClassicKeyTargetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_kms_id** | [**ExternalKMSKeyId**](ExternalKMSKeyId.md) |  | [optional] 
**key_purpose** | **List[str]** |  | [optional] 
**key_status** | [**ClassicKeyStatusInfo**](ClassicKeyStatusInfo.md) |  | [optional] 
**target_assoc_id** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.classic_key_target_info import ClassicKeyTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClassicKeyTargetInfo from a JSON string
classic_key_target_info_instance = ClassicKeyTargetInfo.from_json(json)
# print the JSON string representation of the object
print(ClassicKeyTargetInfo.to_json())

# convert the object into a dict
classic_key_target_info_dict = classic_key_target_info_instance.to_dict()
# create an instance of ClassicKeyTargetInfo from a dict
classic_key_target_info_from_dict = ClassicKeyTargetInfo.from_dict(classic_key_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


