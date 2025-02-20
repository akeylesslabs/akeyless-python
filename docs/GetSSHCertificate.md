# GetSSHCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The name of the SSH certificate issuer | 
**cert_username** | **str** | The username to sign in the SSH certificate | [default to '-']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**legacy_signing_alg_name** | **bool** | Set this option to output legacy (&#39;ssh-rsa-cert-v01@openssh.com&#39;) signing algorithm name in the certificate. | [optional] [default to False]
**public_key_data** | **str** | SSH public key file contents. If this option is used, the certificate will be printed to stdout | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | Updated certificate lifetime in seconds (must be less than the Certificate Issuer default TTL) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_ssh_certificate import GetSSHCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of GetSSHCertificate from a JSON string
get_ssh_certificate_instance = GetSSHCertificate.from_json(json)
# print the JSON string representation of the object
print(GetSSHCertificate.to_json())

# convert the object into a dict
get_ssh_certificate_dict = get_ssh_certificate_instance.to_dict()
# create an instance of GetSSHCertificate from a dict
get_ssh_certificate_from_dict = GetSSHCertificate.from_dict(get_ssh_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


