# CreateLdapTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_dn** | **str** | Bind DN | 
**bind_dn_password** | **str** | Bind DN Password | 
**comment** | **str** | Comment about the target | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**ldap_ca_cert** | **str** | CA Certificate File Content | [optional] 
**ldap_url** | **str** | LDAP Server URL | 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** | Token expiration | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


