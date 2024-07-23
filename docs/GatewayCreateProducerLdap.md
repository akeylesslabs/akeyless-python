# GatewayCreateProducerLdap

gatewayCreateProducerLdap is a command that creates ldap producer [Deprecated: Use dynamic-secret-create-ldap command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**bind_dn** | **str** | Bind DN | [optional] 
**bind_dn_password** | **str** | Bind DN Password | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**external_username** | **str** | Externally provided username [true/false] | [optional] [default to 'false']
**group_dn** | **str** | Group DN which the temporary user should be added | [optional] 
**host_provider** | **str** | Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**ldap_ca_cert** | **str** | CA Certificate File Content | [optional] 
**ldap_url** | **str** | LDAP Server URL | [optional] 
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **list[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rd_gateway_server** | **str** | RD Gateway server | [optional] 
**secure_access_rdp_domain** | **str** | Required when the Dynamic Secret is used for a domain user | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target** | **list[str]** | A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** | Token expiration | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | User Attribute | [optional] 
**user_dn** | **str** | User DN | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


