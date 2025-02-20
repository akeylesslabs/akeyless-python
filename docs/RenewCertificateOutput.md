# RenewCertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** |  | [optional] 
**cert_display_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**parent_cert** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**reading_token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.renew_certificate_output import RenewCertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RenewCertificateOutput from a JSON string
renew_certificate_output_instance = RenewCertificateOutput.from_json(json)
# print the JSON string representation of the object
print(RenewCertificateOutput.to_json())

# convert the object into a dict
renew_certificate_output_dict = renew_certificate_output_instance.to_dict()
# create an instance of RenewCertificateOutput from a dict
renew_certificate_output_from_dict = RenewCertificateOutput.from_dict(renew_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


