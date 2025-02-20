# AllowedAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 
**cluster_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 
**sub_claims_case_insensitive** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.allowed_access import AllowedAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedAccess from a JSON string
allowed_access_instance = AllowedAccess.from_json(json)
# print the JSON string representation of the object
print(AllowedAccess.to_json())

# convert the object into a dict
allowed_access_dict = allowed_access_instance.to_dict()
# create an instance of AllowedAccess from a dict
allowed_access_from_dict = AllowedAccess.from_dict(allowed_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


