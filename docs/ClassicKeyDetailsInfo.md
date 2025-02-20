# ClassicKeyDetailsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classic_key_attributes** | **Dict[str, List[str]]** |  | [optional] 
**classic_key_id** | **str** |  | [optional] 
**credential_id** | **str** |  | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**has_certificate** | **bool** |  | [optional] 
**is_provided_by_user** | **bool** |  | [optional] 
**is_unexportable** | **bool** |  | [optional] 
**key_state** | **str** | ItemState defines the different states an Item can be in | [optional] 
**key_type** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**target_alias_helper** | **str** |  | [optional] 
**target_types** | **List[str]** |  | [optional] 
**targets** | [**List[ClassicKeyTargetInfo]**](ClassicKeyTargetInfo.md) |  | [optional] 
**username** | **str** |  | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.classic_key_details_info import ClassicKeyDetailsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClassicKeyDetailsInfo from a JSON string
classic_key_details_info_instance = ClassicKeyDetailsInfo.from_json(json)
# print the JSON string representation of the object
print(ClassicKeyDetailsInfo.to_json())

# convert the object into a dict
classic_key_details_info_dict = classic_key_details_info_instance.to_dict()
# create an instance of ClassicKeyDetailsInfo from a dict
classic_key_details_info_from_dict = ClassicKeyDetailsInfo.from_dict(classic_key_details_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


