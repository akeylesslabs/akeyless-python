# BatchEncryptionRequestLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **Dict[str, str]** |  | [optional] 
**data** | **str** |  | [optional] 
**item_id** | **int** |  | [optional] 
**item_version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.batch_encryption_request_line import BatchEncryptionRequestLine

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEncryptionRequestLine from a JSON string
batch_encryption_request_line_instance = BatchEncryptionRequestLine.from_json(json)
# print the JSON string representation of the object
print(BatchEncryptionRequestLine.to_json())

# convert the object into a dict
batch_encryption_request_line_dict = batch_encryption_request_line_instance.to_dict()
# create an instance of BatchEncryptionRequestLine from a dict
batch_encryption_request_line_from_dict = BatchEncryptionRequestLine.from_dict(batch_encryption_request_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


