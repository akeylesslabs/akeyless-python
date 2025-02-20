# BatchTokenizationResponseLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**tweak** | **str** |  | [optional] 

## Example

```python
from akeyless.models.batch_tokenization_response_line import BatchTokenizationResponseLine

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTokenizationResponseLine from a JSON string
batch_tokenization_response_line_instance = BatchTokenizationResponseLine.from_json(json)
# print the JSON string representation of the object
print(BatchTokenizationResponseLine.to_json())

# convert the object into a dict
batch_tokenization_response_line_dict = batch_tokenization_response_line_instance.to_dict()
# create an instance of BatchTokenizationResponseLine from a dict
batch_tokenization_response_line_from_dict = BatchTokenizationResponseLine.from_dict(batch_tokenization_response_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


