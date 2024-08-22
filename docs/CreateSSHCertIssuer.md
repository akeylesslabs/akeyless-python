# CreateSSHCertIssuer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**allowed_users** | **str** | Users allowed to fetch the certificate, e.g root,ubuntu | 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**extensions** | **dict(str, str)** | Signed certificates with extensions, e.g permit-port-forwarding&#x3D;\\\&quot;\\\&quot; | [optional] 
**host_provider** | **str** | Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | SSH certificate issuer name | 
**principals** | **str** | Signed certificates with principal, e.g example_role1,example_role2 | [optional] 
**secure_access_bastion_api** | **str** | Bastion&#39;s SSH control API endpoint. E.g. https://my.bastion:9900 | [optional] 
**secure_access_bastion_ssh** | **str** | Bastion&#39;s SSH server. E.g. my.bastion:22 | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_enforce_hosts_restriction** | **bool** | Enable this flag to enforce connections only to the hosts listed in --secure-access-host | [optional] 
**secure_access_host** | **list[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_ssh_creds_user** | **str** | SSH username to connect to target server, must be in &#39;Allowed Users&#39; list | [optional] 
**secure_access_use_internal_bastion** | **bool** | Use internal SSH Bastion | [optional] 
**signer_key_name** | **str** | A key to sign the certificate with | 
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**target** | **list[str]** | A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | The requested Time To Live for the certificate, in seconds | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


