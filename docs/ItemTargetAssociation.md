# ItemTargetAssociation

and a target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**target_id** | **int** |  | [optional] 
**target_name** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.item_target_association import ItemTargetAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTargetAssociation from a JSON string
item_target_association_instance = ItemTargetAssociation.from_json(json)
# print the JSON string representation of the object
print(ItemTargetAssociation.to_json())

# convert the object into a dict
item_target_association_dict = item_target_association_instance.to_dict()
# create an instance of ItemTargetAssociation from a dict
item_target_association_from_dict = ItemTargetAssociation.from_dict(item_target_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


