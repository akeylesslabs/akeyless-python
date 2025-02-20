# KerberosConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_access_id** | **str** |  | [optional] 
**kerberos_keytab** | **str** |  | [optional] 
**kerberos_krb_5_conf** | **str** |  | [optional] 
**kerberos_private_key** | **str** |  | [optional] 
**ldap_anonymous_search** | **bool** |  | [optional] 
**ldap_bind_dn** | **str** |  | [optional] 
**ldap_bind_password** | **str** |  | [optional] 
**ldap_cert** | **str** |  | [optional] 
**ldap_group_attr** | **str** |  | [optional] 
**ldap_group_dn** | **str** |  | [optional] 
**ldap_group_filter** | **str** |  | [optional] 
**ldap_url** | **str** |  | [optional] 
**ldap_user_attr** | **str** |  | [optional] 
**ldap_user_dn** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kerberos_config_part import KerberosConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosConfigPart from a JSON string
kerberos_config_part_instance = KerberosConfigPart.from_json(json)
# print the JSON string representation of the object
print(KerberosConfigPart.to_json())

# convert the object into a dict
kerberos_config_part_dict = kerberos_config_part_instance.to_dict()
# create an instance of KerberosConfigPart from a dict
kerberos_config_part_from_dict = KerberosConfigPart.from_dict(kerberos_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


