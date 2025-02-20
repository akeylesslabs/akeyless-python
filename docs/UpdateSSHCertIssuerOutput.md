# UpdateSSHCertIssuerOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.update_ssh_cert_issuer_output import UpdateSSHCertIssuerOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSSHCertIssuerOutput from a JSON string
update_ssh_cert_issuer_output_instance = UpdateSSHCertIssuerOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateSSHCertIssuerOutput.to_json())

# convert the object into a dict
update_ssh_cert_issuer_output_dict = update_ssh_cert_issuer_output_instance.to_dict()
# create an instance of UpdateSSHCertIssuerOutput from a dict
update_ssh_cert_issuer_output_from_dict = UpdateSSHCertIssuerOutput.from_dict(update_ssh_cert_issuer_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


