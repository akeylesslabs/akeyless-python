# SetItemState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_state** | **str** | Desired item state (Enabled, Disabled) | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Current item name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The specific version you want to update: 0&#x3D;item level state (default) (relevant only for keys) | [optional] [default to 0]

## Example

```python
from akeyless.models.set_item_state import SetItemState

# TODO update the JSON string below
json = "{}"
# create an instance of SetItemState from a JSON string
set_item_state_instance = SetItemState.from_json(json)
# print the JSON string representation of the object
print(SetItemState.to_json())

# convert the object into a dict
set_item_state_dict = set_item_state_instance.to_dict()
# create an instance of SetItemState from a dict
set_item_state_from_dict = SetItemState.from_dict(set_item_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


