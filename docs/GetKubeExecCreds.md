# GetKubeExecCreds

getKubeExecCreds is a command that gets credentials for authentication with Kubernetes cluster based on a PKI cert issuer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | **str** | The Subject Alternative Names to be included in the PKI certificate (in a comma-separated list) (if CSR is supplied this flag is ignored and any DNS.* names are taken from it) | [optional] 
**api_version** | **str** | Client authentication API version | [optional] [default to 'v1']
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | 
**common_name** | **str** | The common name to be included in the PKI certificate (if CSR is supplied this flag is ignored and the CSR subject CN is taken) | [optional] 
**csr_data_base64** | **str** | Certificate Signing Request contents encoded in base64 to generate the certificate with | [optional] 
**extended_key_usage** | **str** | A comma-separated list of extended key usage requests which will be used for certificate issuance. Supported values: &#39;clientauth&#39;, &#39;serverauth&#39;. If critical is present the extension will be marked as critical | [optional] 
**extra_extensions** | **str** | A json string that defines the requested extra extensions for the certificate | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_data_base64** | **str** | PKI key file contents. If this option is used, the certificate will be printed to stdout | [optional] 
**max_path_len** | **int** | The maximum path length for the generated certificate. -1, means unlimited unless the signing certificate has a maximum path length set | [optional] [default to -1]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **str** | Updated certificate lifetime in seconds (must be less than the Certificate Issuer default TTL) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | The URI Subject Alternative Names to be included in the PKI certificate (in a comma-separated list) (if CSR is supplied this flag is ignored and any URI.* names are taken from it) | [optional] 

## Example

```python
from akeyless.models.get_kube_exec_creds import GetKubeExecCreds

# TODO update the JSON string below
json = "{}"
# create an instance of GetKubeExecCreds from a JSON string
get_kube_exec_creds_instance = GetKubeExecCreds.from_json(json)
# print the JSON string representation of the object
print(GetKubeExecCreds.to_json())

# convert the object into a dict
get_kube_exec_creds_dict = get_kube_exec_creds_instance.to_dict()
# create an instance of GetKubeExecCreds from a dict
get_kube_exec_creds_from_dict = GetKubeExecCreds.from_dict(get_kube_exec_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


