# BatchEncryptionResponseLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from akeyless.models.batch_encryption_response_line import BatchEncryptionResponseLine

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEncryptionResponseLine from a JSON string
batch_encryption_response_line_instance = BatchEncryptionResponseLine.from_json(json)
# print the JSON string representation of the object
print(BatchEncryptionResponseLine.to_json())

# convert the object into a dict
batch_encryption_response_line_dict = batch_encryption_response_line_instance.to_dict()
# create an instance of BatchEncryptionResponseLine from a dict
batch_encryption_response_line_from_dict = BatchEncryptionResponseLine.from_dict(batch_encryption_response_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


