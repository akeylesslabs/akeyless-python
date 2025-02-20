# CreateSSHCertIssuerOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_ssh_cert_issuer_output import CreateSSHCertIssuerOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSSHCertIssuerOutput from a JSON string
create_ssh_cert_issuer_output_instance = CreateSSHCertIssuerOutput.from_json(json)
# print the JSON string representation of the object
print(CreateSSHCertIssuerOutput.to_json())

# convert the object into a dict
create_ssh_cert_issuer_output_dict = create_ssh_cert_issuer_output_instance.to_dict()
# create an instance of CreateSSHCertIssuerOutput from a dict
create_ssh_cert_issuer_output_from_dict = CreateSSHCertIssuerOutput.from_dict(create_ssh_cert_issuer_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


