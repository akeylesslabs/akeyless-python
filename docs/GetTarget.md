# GetTarget

getTarget is a command that returns target. [Deprecated: Use target-get command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Target name | 
**show_versions** | **bool** | Include all target versions in reply | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_target import GetTarget

# TODO update the JSON string below
json = "{}"
# create an instance of GetTarget from a JSON string
get_target_instance = GetTarget.from_json(json)
# print the JSON string representation of the object
print(GetTarget.to_json())

# convert the object into a dict
get_target_dict = get_target_instance.to_dict()
# create an instance of GetTarget from a dict
get_target_from_dict = GetTarget.from_dict(get_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


