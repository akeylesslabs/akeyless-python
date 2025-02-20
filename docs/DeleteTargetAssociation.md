# DeleteTargetAssociation

deleteTargetAssociation is a command that deletes an association between target and item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** | The association id to be deleted | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Item name | 
**target_name** | **str** | The target to associate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_target_association import DeleteTargetAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTargetAssociation from a JSON string
delete_target_association_instance = DeleteTargetAssociation.from_json(json)
# print the JSON string representation of the object
print(DeleteTargetAssociation.to_json())

# convert the object into a dict
delete_target_association_dict = delete_target_association_instance.to_dict()
# create an instance of DeleteTargetAssociation from a dict
delete_target_association_from_dict = DeleteTargetAssociation.from_dict(delete_target_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


