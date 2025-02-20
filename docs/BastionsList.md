# BastionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[BastionListEntry]**](BastionListEntry.md) |  | [optional] 

## Example

```python
from akeyless.models.bastions_list import BastionsList

# TODO update the JSON string below
json = "{}"
# create an instance of BastionsList from a JSON string
bastions_list_instance = BastionsList.from_json(json)
# print the JSON string representation of the object
print(BastionsList.to_json())

# convert the object into a dict
bastions_list_dict = bastions_list_instance.to_dict()
# create an instance of BastionsList from a dict
bastions_list_from_dict = BastionsList.from_dict(bastions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


