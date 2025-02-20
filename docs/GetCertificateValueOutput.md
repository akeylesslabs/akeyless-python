# GetCertificateValueOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_pem** | **str** |  | [optional] 
**private_key_pem** | **str** |  | [optional] 

## Example

```python
from akeyless.models.get_certificate_value_output import GetCertificateValueOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetCertificateValueOutput from a JSON string
get_certificate_value_output_instance = GetCertificateValueOutput.from_json(json)
# print the JSON string representation of the object
print(GetCertificateValueOutput.to_json())

# convert the object into a dict
get_certificate_value_output_dict = get_certificate_value_output_instance.to_dict()
# create an instance of GetCertificateValueOutput from a dict
get_certificate_value_output_from_dict = GetCertificateValueOutput.from_dict(get_certificate_value_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


