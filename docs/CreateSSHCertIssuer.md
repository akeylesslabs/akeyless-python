# CreateSSHCertIssuer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_users** | **str** | Users allowed to fetch the certificate, e.g root,ubuntu | 
**extensions** | **dict(str, str)** | Signed certificates with extensions, e.g permit-port-forwarding&#x3D;\\\&quot;\\\&quot; | [optional] 
**metadata** | **str** | A metadata about the issuer | [optional] 
**name** | **str** | SSH certificate issuer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**principals** | **str** | Signed certificates with principal, e.g example_role1,example_role2 | [optional] 
**secure_access_bastion_api** | **str** |  | [optional] 
**secure_access_bastion_ssh** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_ssh_creds_user** | **str** |  | [optional] 
**secure_access_use_internal_bastion** | **bool** |  | [optional] 
**signer_key_name** | **str** | A key to sign the certificate with | 
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | he requested Time To Live for the certificate, in seconds | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


