# EncryptOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 

## Example

```python
from akeyless.models.encrypt_output import EncryptOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptOutput from a JSON string
encrypt_output_instance = EncryptOutput.from_json(json)
# print the JSON string representation of the object
print(EncryptOutput.to_json())

# convert the object into a dict
encrypt_output_dict = encrypt_output_instance.to_dict()
# create an instance of EncryptOutput from a dict
encrypt_output_from_dict = EncryptOutput.from_dict(encrypt_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


