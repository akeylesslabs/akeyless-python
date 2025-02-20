# GenerateCA

GenerateCA is a command that creates a new PKI CA and Intermediate issuers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**allowed_domains** | **str** | A list of the allowed domains that clients can request to be included in the certificate (in a comma-delimited list) | 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**extended_key_usage** | **str** | A comma sepereted list of extended key usage for the intermediate (serverauth / clientauth / codesigning) | [optional] [default to 'serverauth,clientauth']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_type** | **str** |  | [optional] 
**max_path_len** | **int** | The maximum number of intermediate certificates that can appear in a certification path | [optional] [default to 1]
**pki_chain_name** | **str** | PKI chain name | 
**protection_key_name** | **str** | The name of a key that used to encrypt the secrets values (if empty, the account default protectionKey key will be used) | [optional] 
**split_level** | **int** | The number of fragments that the item will be split into | [optional] [default to 3]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **str** | The maximum requested Time To Live for issued certificate by default in seconds, supported formats are s,m,h,d | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.generate_ca import GenerateCA

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCA from a JSON string
generate_ca_instance = GenerateCA.from_json(json)
# print the JSON string representation of the object
print(GenerateCA.to_json())

# convert the object into a dict
generate_ca_dict = generate_ca_instance.to_dict()
# create an instance of GenerateCA from a dict
generate_ca_from_dict = GenerateCA.from_dict(generate_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


