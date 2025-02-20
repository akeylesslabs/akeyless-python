# DecryptPKCS1Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaintext** | **str** |  | [optional] 

## Example

```python
from akeyless.models.decrypt_pkcs1_output import DecryptPKCS1Output

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptPKCS1Output from a JSON string
decrypt_pkcs1_output_instance = DecryptPKCS1Output.from_json(json)
# print the JSON string representation of the object
print(DecryptPKCS1Output.to_json())

# convert the object into a dict
decrypt_pkcs1_output_dict = decrypt_pkcs1_output_instance.to_dict()
# create an instance of DecryptPKCS1Output from a dict
decrypt_pkcs1_output_from_dict = DecryptPKCS1Output.from_dict(decrypt_pkcs1_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


