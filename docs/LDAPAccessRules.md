# LDAPAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**gen_key_pair** | **str** | Generate public/private key (the private key is required for the LDAP Auth Config in the Akeyless Gateway) | [optional] 
**key** | **str** | The public key value of LDAP. | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.ldap_access_rules import LDAPAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPAccessRules from a JSON string
ldap_access_rules_instance = LDAPAccessRules.from_json(json)
# print the JSON string representation of the object
print(LDAPAccessRules.to_json())

# convert the object into a dict
ldap_access_rules_dict = ldap_access_rules_instance.to_dict()
# create an instance of LDAPAccessRules from a dict
ldap_access_rules_from_dict = LDAPAccessRules.from_dict(ldap_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


