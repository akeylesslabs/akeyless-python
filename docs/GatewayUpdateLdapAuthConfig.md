# GatewayUpdateLdapAuthConfig

gatewayUpdateLdapAuth is a command that updates ldap auth config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access ID of the Ldap auth method | [optional] 
**bind_dn** | **str** | Bind DN | [optional] 
**bind_dn_password** | **str** | Bind DN Password | [optional] 
**group_attr** | **str** | Group Attr | [optional] 
**group_dn** | **str** | Group Dn | [optional] 
**group_filter** | **str** | Group Filter | [optional] 
**ldap_ca_cert** | **str** | LDAP CA Certificate (base64 encoded) | [optional] 
**ldap_enable** | **str** | Enable Ldap | [optional] 
**ldap_url** | **str** | LDAP Server URL, e.g. ldap://planetexpress.com:389 | [optional] 
**ldap_anonymous_search** | **bool** | Ldap Anonymous Search | [optional] 
**signing_key_data** | **str** | The private key (base64 encoded), associated with the public key defined in the Ldap auth | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | User Attribute | [optional] 
**user_dn** | **str** | User DN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


