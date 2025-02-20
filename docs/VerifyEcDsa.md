# VerifyEcDsa

verifyEcDsa is a command that verifies an ECDSA signature using a sha hash algorithm matching the key size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the EC key to use for the verification process | [optional] 
**item_id** | **int** | The item id of the EC key to use for the verification process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the EC key to use for the verification process | [optional] 
**message** | **str** | The message to be verified in a base64 format | 
**prehashed** | **bool** | Markes that the message is already hashed | [optional] 
**signature** | **str** | The message&#39;s signature | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The version of the key to use for verification | [optional] 

## Example

```python
from akeyless.models.verify_ec_dsa import VerifyEcDsa

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEcDsa from a JSON string
verify_ec_dsa_instance = VerifyEcDsa.from_json(json)
# print the JSON string representation of the object
print(VerifyEcDsa.to_json())

# convert the object into a dict
verify_ec_dsa_dict = verify_ec_dsa_instance.to_dict()
# create an instance of VerifyEcDsa from a dict
verify_ec_dsa_from_dict = VerifyEcDsa.from_dict(verify_ec_dsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


