# UpdateLdapTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_dn** | **str** |  | [optional] 
**bind_dn_password** | **str** |  | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**keep_prev_version** | **str** |  | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**ldap_ca_cert** | **str** |  | [optional] 
**ldap_url** | **str** |  | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**server_type** | **str** | Set Ldap server type, Options:[OpenLDAP, ActiveDirectory] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** |  | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Deprecated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


