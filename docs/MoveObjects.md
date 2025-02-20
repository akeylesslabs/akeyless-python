# MoveObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**objects_type** | **str** | The objects type to move (item/auth_method/role) | [optional] [default to 'item']
**source** | **str** | Source path to move the objects from | 
**target** | **str** | Target path to move the objects to | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.move_objects import MoveObjects

# TODO update the JSON string below
json = "{}"
# create an instance of MoveObjects from a JSON string
move_objects_instance = MoveObjects.from_json(json)
# print the JSON string representation of the object
print(MoveObjects.to_json())

# convert the object into a dict
move_objects_dict = move_objects_instance.to_dict()
# create an instance of MoveObjects from a dict
move_objects_from_dict = MoveObjects.from_dict(move_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


