# BatchTokenizationRequestLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**item_id** | **int** |  | [optional] 
**tweak** | **str** |  | [optional] 

## Example

```python
from akeyless.models.batch_tokenization_request_line import BatchTokenizationRequestLine

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTokenizationRequestLine from a JSON string
batch_tokenization_request_line_instance = BatchTokenizationRequestLine.from_json(json)
# print the JSON string representation of the object
print(BatchTokenizationRequestLine.to_json())

# convert the object into a dict
batch_tokenization_request_line_dict = batch_tokenization_request_line_instance.to_dict()
# create an instance of BatchTokenizationRequestLine from a dict
batch_tokenization_request_line_from_dict = BatchTokenizationRequestLine.from_dict(batch_tokenization_request_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


