# SAMLAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_uris** | **List[str]** | Allowed redirect URIs after the authentication | [optional] 
**bound_attributes** | [**List[SAMLAttribute]**](SAMLAttribute.md) | The attributes that login is restricted to. | [optional] 
**idp_metadata_url** | **str** | IDP metadata url | [optional] 
**idp_metadata_xml** | **str** | IDP metadata XML | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.saml_access_rules import SAMLAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLAccessRules from a JSON string
saml_access_rules_instance = SAMLAccessRules.from_json(json)
# print the JSON string representation of the object
print(SAMLAccessRules.to_json())

# convert the object into a dict
saml_access_rules_dict = saml_access_rules_instance.to_dict()
# create an instance of SAMLAccessRules from a dict
saml_access_rules_from_dict = SAMLAccessRules.from_dict(saml_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


