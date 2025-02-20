# VerifyJWTWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The name of the key to use in the verify JWT process | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt** | **str** | JWT | 
**required_claims** | **str** | RequiredClaims | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.verify_jwt_with_classic_key import VerifyJWTWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyJWTWithClassicKey from a JSON string
verify_jwt_with_classic_key_instance = VerifyJWTWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(VerifyJWTWithClassicKey.to_json())

# convert the object into a dict
verify_jwt_with_classic_key_dict = verify_jwt_with_classic_key_instance.to_dict()
# create an instance of VerifyJWTWithClassicKey from a dict
verify_jwt_with_classic_key_from_dict = VerifyJWTWithClassicKey.from_dict(verify_jwt_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


