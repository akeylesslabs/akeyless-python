# SignJWTWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The name of the key to use in the sign JWT process | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_claims** | **str** | JWTClaims | 
**signing_method** | **str** | SigningMethod | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.sign_jwt_with_classic_key import SignJWTWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of SignJWTWithClassicKey from a JSON string
sign_jwt_with_classic_key_instance = SignJWTWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(SignJWTWithClassicKey.to_json())

# convert the object into a dict
sign_jwt_with_classic_key_dict = sign_jwt_with_classic_key_instance.to_dict()
# create an instance of SignJWTWithClassicKey from a dict
sign_jwt_with_classic_key_from_dict = SignJWTWithClassicKey.from_dict(sign_jwt_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


