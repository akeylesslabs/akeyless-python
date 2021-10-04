# CreateLdapTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | 
**bind_dn** | **str** | Bind DN | [optional] 
**bind_dn_password** | **str** | Bind DN Password | [optional] 
**comment** | **str** | Comment about the target | [optional] 
**enable_anonym_search** | **bool** | EnableAnonymousSearch | [optional] 
**group_attribute** | **str** | Group attribute | [optional] 
**group_dn** | **str** | Group DN | [optional] 
**group_filter** | **str** | Group attribute | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**ldap_ca_cert** | **str** | CA Certificate File Content | [optional] 
**ldap_url** | **str** | LDAP Server URL | 
**name** | **str** | Target name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**private_key** | **str** | Base64-encoded ldap private key text | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** | Token expiration | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | User Attribute | [optional] 
**user_dn** | **str** | User DN | 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


