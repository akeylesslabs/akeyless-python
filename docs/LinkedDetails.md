# LinkedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **Dict[str, str]** |  | [optional] 

## Example

```python
from akeyless.models.linked_details import LinkedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedDetails from a JSON string
linked_details_instance = LinkedDetails.from_json(json)
# print the JSON string representation of the object
print(LinkedDetails.to_json())

# convert the object into a dict
linked_details_dict = linked_details_instance.to_dict()
# create an instance of LinkedDetails from a dict
linked_details_from_dict = LinkedDetails.from_dict(linked_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


