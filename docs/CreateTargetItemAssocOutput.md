# CreateTargetItemAssocOutput

CreateTargetItemAssocOutput defines output of CreateTargetItemAssoc operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_target_item_assoc_output import CreateTargetItemAssocOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetItemAssocOutput from a JSON string
create_target_item_assoc_output_instance = CreateTargetItemAssocOutput.from_json(json)
# print the JSON string representation of the object
print(CreateTargetItemAssocOutput.to_json())

# convert the object into a dict
create_target_item_assoc_output_dict = create_target_item_assoc_output_instance.to_dict()
# create an instance of CreateTargetItemAssocOutput from a dict
create_target_item_assoc_output_from_dict = CreateTargetItemAssocOutput.from_dict(create_target_item_assoc_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


