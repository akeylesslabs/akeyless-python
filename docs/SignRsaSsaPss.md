# SignRsaSsaPss

signRsaSsaPss is a command that calculates the signature of a given message using rsassa-pss

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the RSA key to use in the signing process | [optional] 
**hash_function** | **str** | HashFunction defines the hash function (e.g. sha-256) | [optional] 
**item_id** | **int** | The item id of the RSA key to use in the signing process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the RSA key to use in the signing process | [optional] 
**message** | **str** | The input message to sign in a base64 format | 
**prehashed** | **bool** | Markes that the message is already hashed | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The version of the key to use for signing | [optional] 

## Example

```python
from akeyless.models.sign_rsa_ssa_pss import SignRsaSsaPss

# TODO update the JSON string below
json = "{}"
# create an instance of SignRsaSsaPss from a JSON string
sign_rsa_ssa_pss_instance = SignRsaSsaPss.from_json(json)
# print the JSON string representation of the object
print(SignRsaSsaPss.to_json())

# convert the object into a dict
sign_rsa_ssa_pss_dict = sign_rsa_ssa_pss_instance.to_dict()
# create an instance of SignRsaSsaPss from a dict
sign_rsa_ssa_pss_from_dict = SignRsaSsaPss.from_dict(sign_rsa_ssa_pss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


