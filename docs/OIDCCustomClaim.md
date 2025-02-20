# OIDCCustomClaim

OIDCCustomClaim is a custom claim specific to OIDC authentication method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.oidc_custom_claim import OIDCCustomClaim

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCCustomClaim from a JSON string
oidc_custom_claim_instance = OIDCCustomClaim.from_json(json)
# print the JSON string representation of the object
print(OIDCCustomClaim.to_json())

# convert the object into a dict
oidc_custom_claim_dict = oidc_custom_claim_instance.to_dict()
# create an instance of OIDCCustomClaim from a dict
oidc_custom_claim_from_dict = OIDCCustomClaim.from_dict(oidc_custom_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


