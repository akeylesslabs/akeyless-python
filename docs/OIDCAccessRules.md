# OIDCAccessRules

OIDCAccessRules contains access rules specific to Open Id Connect authentication method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_uris** | **List[str]** | Allowed redirect URIs after the authentication | [optional] 
**audience** | **str** | Audience claim to be used as part of the authentication flow. In case set, it must match the one configured on the Identity Provider&#39;s Application | [optional] 
**bound_claims** | [**List[OIDCCustomClaim]**](OIDCCustomClaim.md) | The claims that login is restricted to. | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret | [optional] 
**is_internal** | **bool** | IsInternal indicates whether this is an internal Auth Method where the client has no control over it, or it was created by the client e.g - Sign In with Google will create an OIDC Auth Method with IsInternal&#x3D;true | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**required_scopes** | **List[str]** | A list of required scopes to request from the oidc provider, and to check on the token | [optional] 
**required_scopes_prefix** | **str** | A prefix to add to the required scopes (for example, azures&#39; Application ID URI) | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.oidc_access_rules import OIDCAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCAccessRules from a JSON string
oidc_access_rules_instance = OIDCAccessRules.from_json(json)
# print the JSON string representation of the object
print(OIDCAccessRules.to_json())

# convert the object into a dict
oidc_access_rules_dict = oidc_access_rules_instance.to_dict()
# create an instance of OIDCAccessRules from a dict
oidc_access_rules_from_dict = OIDCAccessRules.from_dict(oidc_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


