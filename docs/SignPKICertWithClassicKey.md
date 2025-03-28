# SignPKICertWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The common name to be included in the PKI certificate | [optional] 
**country** | **str** | A comma-separated list of the country that will be set in the issued certificate | [optional] 
**display_id** | **str** | The name of the key to use in the sign PKI Cert process | 
**dns_names** | **str** | DNS Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_usage** | **str** | key-usage | [optional] [default to 'DigitalSignature,KeyAgreement,KeyEncipherment']
**locality** | **str** | A comma-separated list of the locality that will be set in the issued certificate | [optional] 
**organizational_units** | **str** | A comma-separated list of organizational units (OU) that will be set in the issued certificate | [optional] 
**organizations** | **str** | A comma-separated list of organizations (O) that will be set in the issued certificate | [optional] 
**postal_code** | **str** | A comma-separated list of the postal code that will be set in the issued certificate | [optional] 
**province** | **str** | A comma-separated list of the province that will be set in the issued certificate | [optional] 
**public_key_pem_data** | **str** | PublicKey using for signing in a PEM format. | [optional] 
**signing_method** | **str** | SigningMethod | 
**street_address** | **str** | A comma-separated list of the street address that will be set in the issued certificate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | he requested Time To Live for the certificate, in seconds | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.sign_pki_cert_with_classic_key import SignPKICertWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of SignPKICertWithClassicKey from a JSON string
sign_pki_cert_with_classic_key_instance = SignPKICertWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(SignPKICertWithClassicKey.to_json())

# convert the object into a dict
sign_pki_cert_with_classic_key_dict = sign_pki_cert_with_classic_key_instance.to_dict()
# create an instance of SignPKICertWithClassicKey from a dict
sign_pki_cert_with_classic_key_from_dict = SignPKICertWithClassicKey.from_dict(sign_pki_cert_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


