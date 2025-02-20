# ExternalKMSKeyId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | [optional] 
**key_reference** | **str** |  | [optional] 

## Example

```python
from akeyless.models.external_kms_key_id import ExternalKMSKeyId

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKMSKeyId from a JSON string
external_kms_key_id_instance = ExternalKMSKeyId.from_json(json)
# print the JSON string representation of the object
print(ExternalKMSKeyId.to_json())

# convert the object into a dict
external_kms_key_id_dict = external_kms_key_id_instance.to_dict()
# create an instance of ExternalKMSKeyId from a dict
external_kms_key_id_from_dict = ExternalKMSKeyId.from_dict(external_kms_key_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


