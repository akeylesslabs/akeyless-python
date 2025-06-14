# CreateSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**change_event** | **str** | Trigger an event when a secret value changed [true/false] (Relevant only for Static Secret) | [optional] 
**custom_field** | **dict(str, str)** | For Password Management use, additional fields | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**format** | **str** | Secret format [text/json/key-value] (relevant only for type &#39;generic&#39;) | [optional] [default to 'text']
**inject_url** | **list[str]** | For Password Management use, reflect the website context | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**multiline_value** | **bool** | The provided value is a multiline value (separated by &#39;\\n&#39;) | [optional] 
**name** | **str** | Secret name | 
**password** | **str** | For Password Management use, additional fields | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_gateway** | **str** |  | [optional] 
**secure_access_host** | **list[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rdp_user** | **str** | Remote Desktop Username | [optional] 
**secure_access_ssh_creds** | **str** | Static-Secret values contains SSH Credentials, either Private Key or Password [password/private-key] | [optional] 
**secure_access_ssh_user** | **str** | Override the SSH username as indicated in SSH Certificate Issuer | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | The secret sub type [generic/password] | [optional] [default to 'generic']
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | For Password Management use | [optional] 
**value** | **str** | The secret value (relevant only for type &#39;generic&#39;) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


