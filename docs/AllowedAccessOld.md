# AllowedAccessOld

Deprecated: AllowedAccessOld please use Gator allowed_access API structs such as AllowedAccessInput/AllowedAccess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acc_id** | **str** |  | [optional] 
**access_permissions** | **List[str]** |  | [optional] 
**access_rules_type** | **str** |  | [optional] 
**allowed_api** | **bool** |  | [optional] 
**alloweds_login** | **bool** |  | [optional] 
**editable** | **bool** |  | [optional] 
**err_msg** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from akeyless.models.allowed_access_old import AllowedAccessOld

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedAccessOld from a JSON string
allowed_access_old_instance = AllowedAccessOld.from_json(json)
# print the JSON string representation of the object
print(AllowedAccessOld.to_json())

# convert the object into a dict
allowed_access_old_dict = allowed_access_old_instance.to_dict()
# create an instance of AllowedAccessOld from a dict
allowed_access_old_from_dict = AllowedAccessOld.from_dict(allowed_access_old_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


