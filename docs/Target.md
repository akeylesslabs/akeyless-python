# Target


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_date** | **datetime** |  | [optional] 
**access_date_display** | **str** |  | [optional] 
**access_request_status** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** | this is not \&quot;omitempty\&quot; since an empty value causes no update while an empty map will clear the attributes | [optional] 
**client_permissions** | **List[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**credentials_less** | **bool** |  | [optional] 
**is_access_request_enabled** | **bool** |  | [optional] 
**last_version** | **int** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**protection_key_name** | **str** |  | [optional] 
**target_details** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**target_items_assoc** | [**List[TargetItemAssociation]**](TargetItemAssociation.md) |  | [optional] 
**target_name** | **str** |  | [optional] 
**target_sub_type** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**target_versions** | [**List[ItemVersion]**](ItemVersion.md) |  | [optional] 
**with_customer_fragment** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print(Target.to_json())

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_from_dict = Target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


