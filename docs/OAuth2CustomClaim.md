# OAuth2CustomClaim

OAuth2CustomClaim is a custom claim specific to OAuth2 authentication method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.o_auth2_custom_claim import OAuth2CustomClaim

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2CustomClaim from a JSON string
o_auth2_custom_claim_instance = OAuth2CustomClaim.from_json(json)
# print the JSON string representation of the object
print(OAuth2CustomClaim.to_json())

# convert the object into a dict
o_auth2_custom_claim_dict = o_auth2_custom_claim_instance.to_dict()
# create an instance of OAuth2CustomClaim from a dict
o_auth2_custom_claim_from_dict = OAuth2CustomClaim.from_dict(o_auth2_custom_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


