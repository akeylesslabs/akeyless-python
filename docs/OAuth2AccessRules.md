# OAuth2AccessRules

OAuth2AccessRules contains access rules specific to OAuth2 authentication method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | The audience in the JWT. | [optional] 
**authorized_gw_cluster_name** | **str** | The gateway cluster name that is authorized to access JWKeySetURL | [optional] 
**bound_claims** | [**List[OAuth2CustomClaim]**](OAuth2CustomClaim.md) | The claims that login is restricted to. | [optional] 
**bound_clients_id** | **List[str]** | The clients ids that login is restricted to. | [optional] 
**certificate** | **str** | Certificate to use when calling jwks_uri from the gateway. in PEM format | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**jwks_json_data** | **str** | The JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. base64 encoded string | [optional] 
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.o_auth2_access_rules import OAuth2AccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AccessRules from a JSON string
o_auth2_access_rules_instance = OAuth2AccessRules.from_json(json)
# print the JSON string representation of the object
print(OAuth2AccessRules.to_json())

# convert the object into a dict
o_auth2_access_rules_dict = o_auth2_access_rules_instance.to_dict()
# create an instance of OAuth2AccessRules from a dict
o_auth2_access_rules_from_dict = OAuth2AccessRules.from_dict(o_auth2_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


