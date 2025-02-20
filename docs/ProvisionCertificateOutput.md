# ProvisionCertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail_message** | **str** |  | [optional] 
**success_message** | **str** |  | [optional] 
**host_names** | **List[str]** |  | [optional] 
**provisioned_at** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.provision_certificate_output import ProvisionCertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionCertificateOutput from a JSON string
provision_certificate_output_instance = ProvisionCertificateOutput.from_json(json)
# print the JSON string representation of the object
print(ProvisionCertificateOutput.to_json())

# convert the object into a dict
provision_certificate_output_dict = provision_certificate_output_instance.to_dict()
# create an instance of ProvisionCertificateOutput from a dict
provision_certificate_output_from_dict = ProvisionCertificateOutput.from_dict(provision_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


