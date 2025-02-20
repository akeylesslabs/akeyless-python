# KerberosAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_public_key** | **str** |  | [optional] 
**unique_identifier** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kerberos_access_rules import KerberosAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosAccessRules from a JSON string
kerberos_access_rules_instance = KerberosAccessRules.from_json(json)
# print the JSON string representation of the object
print(KerberosAccessRules.to_json())

# convert the object into a dict
kerberos_access_rules_dict = kerberos_access_rules_instance.to_dict()
# create an instance of KerberosAccessRules from a dict
kerberos_access_rules_from_dict = KerberosAccessRules.from_dict(kerberos_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


