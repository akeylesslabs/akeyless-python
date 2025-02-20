# UniversalIdentityAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deny_inheritance** | **bool** |  | [optional] 
**deny_rotate** | **bool** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from akeyless.models.universal_identity_access_rules import UniversalIdentityAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalIdentityAccessRules from a JSON string
universal_identity_access_rules_instance = UniversalIdentityAccessRules.from_json(json)
# print the JSON string representation of the object
print(UniversalIdentityAccessRules.to_json())

# convert the object into a dict
universal_identity_access_rules_dict = universal_identity_access_rules_instance.to_dict()
# create an instance of UniversalIdentityAccessRules from a dict
universal_identity_access_rules_from_dict = UniversalIdentityAccessRules.from_dict(universal_identity_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


