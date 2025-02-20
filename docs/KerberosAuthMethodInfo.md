# KerberosAuthMethodInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_keytab** | **str** |  | [optional] 
**kerberos_krb5_conf** | **str** |  | [optional] 
**ldap_anonymous_search** | **bool** |  | [optional] 
**ldap_bind_dn** | **str** |  | [optional] 
**ldap_bind_password** | **str** |  | [optional] 
**ldap_certificate** | **str** |  | [optional] 
**ldap_group_attr** | **str** |  | [optional] 
**ldap_group_dn** | **str** |  | [optional] 
**ldap_group_filter** | **str** |  | [optional] 
**ldap_url_address** | **str** |  | [optional] 
**ldap_user_attr** | **str** |  | [optional] 
**ldap_user_dn** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kerberos_auth_method_info import KerberosAuthMethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosAuthMethodInfo from a JSON string
kerberos_auth_method_info_instance = KerberosAuthMethodInfo.from_json(json)
# print the JSON string representation of the object
print(KerberosAuthMethodInfo.to_json())

# convert the object into a dict
kerberos_auth_method_info_dict = kerberos_auth_method_info_instance.to_dict()
# create an instance of KerberosAuthMethodInfo from a dict
kerberos_auth_method_info_from_dict = KerberosAuthMethodInfo.from_dict(kerberos_auth_method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


