# TmpUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**custom_ttl** | **int** |  | [optional] 
**dynamic_secret_type** | **str** |  | [optional] 
**encrypted_secret** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from akeyless.models.tmp_user_data import TmpUserData

# TODO update the JSON string below
json = "{}"
# create an instance of TmpUserData from a JSON string
tmp_user_data_instance = TmpUserData.from_json(json)
# print the JSON string representation of the object
print(TmpUserData.to_json())

# convert the object into a dict
tmp_user_data_dict = tmp_user_data_instance.to_dict()
# create an instance of TmpUserData from a dict
tmp_user_data_from_dict = TmpUserData.from_dict(tmp_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


