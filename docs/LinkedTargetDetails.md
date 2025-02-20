# LinkedTargetDetails

LinkedTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **Dict[str, str]** | key hostname, value description | [optional] 

## Example

```python
from akeyless.models.linked_target_details import LinkedTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedTargetDetails from a JSON string
linked_target_details_instance = LinkedTargetDetails.from_json(json)
# print the JSON string representation of the object
print(LinkedTargetDetails.to_json())

# convert the object into a dict
linked_target_details_dict = linked_target_details_instance.to_dict()
# create an instance of LinkedTargetDetails from a dict
linked_target_details_from_dict = LinkedTargetDetails.from_dict(linked_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


