# GetPKICertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_display_id** | **str** |  | [optional] 
**cert_item_id** | **int** |  | [optional] 
**data** | **str** |  | [optional] 
**parent_cert** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**reading_token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.get_pki_certificate_output import GetPKICertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetPKICertificateOutput from a JSON string
get_pki_certificate_output_instance = GetPKICertificateOutput.from_json(json)
# print the JSON string representation of the object
print(GetPKICertificateOutput.to_json())

# convert the object into a dict
get_pki_certificate_output_dict = get_pki_certificate_output_instance.to_dict()
# create an instance of GetPKICertificateOutput from a dict
get_pki_certificate_output_from_dict = GetPKICertificateOutput.from_dict(get_pki_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


