# TargetItemAssociation

TargetItemAssociation includes details of an association between a target and an item. Also, between targets in case of child target or Linked target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**cluster_id** | **int** |  | [optional] 
**item_name** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**relationship** | **str** |  | [optional] 

## Example

```python
from akeyless.models.target_item_association import TargetItemAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of TargetItemAssociation from a JSON string
target_item_association_instance = TargetItemAssociation.from_json(json)
# print the JSON string representation of the object
print(TargetItemAssociation.to_json())

# convert the object into a dict
target_item_association_dict = target_item_association_instance.to_dict()
# create an instance of TargetItemAssociation from a dict
target_item_association_from_dict = TargetItemAssociation.from_dict(target_item_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


