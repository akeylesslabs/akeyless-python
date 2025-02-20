# TargetGetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Target name | 
**show_versions** | **bool** | Include all target versions in reply | [optional] [default to False]
**target_version** | **int** | Target version | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_get_details import TargetGetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGetDetails from a JSON string
target_get_details_instance = TargetGetDetails.from_json(json)
# print the JSON string representation of the object
print(TargetGetDetails.to_json())

# convert the object into a dict
target_get_details_dict = target_get_details_instance.to_dict()
# create an instance of TargetGetDetails from a dict
target_get_details_from_dict = TargetGetDetails.from_dict(target_get_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


