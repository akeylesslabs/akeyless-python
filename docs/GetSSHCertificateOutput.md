# GetSSHCertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from akeyless.models.get_ssh_certificate_output import GetSSHCertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetSSHCertificateOutput from a JSON string
get_ssh_certificate_output_instance = GetSSHCertificateOutput.from_json(json)
# print the JSON string representation of the object
print(GetSSHCertificateOutput.to_json())

# convert the object into a dict
get_ssh_certificate_output_dict = get_ssh_certificate_output_instance.to_dict()
# create an instance of GetSSHCertificateOutput from a dict
get_ssh_certificate_output_from_dict = GetSSHCertificateOutput.from_dict(get_ssh_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


