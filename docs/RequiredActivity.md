# RequiredActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrations_required_activity** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from akeyless.models.required_activity import RequiredActivity

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredActivity from a JSON string
required_activity_instance = RequiredActivity.from_json(json)
# print the JSON string representation of the object
print(RequiredActivity.to_json())

# convert the object into a dict
required_activity_dict = required_activity_instance.to_dict()
# create an instance of RequiredActivity from a dict
required_activity_from_dict = RequiredActivity.from_dict(required_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


