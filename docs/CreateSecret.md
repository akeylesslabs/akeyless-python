# CreateSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | **dict(str, str)** | For Password Management use, additional fields | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**item_accessibility** | **str** | for personal password manager | [optional] 
**metadata** | **str** | Metadata about the secret | [optional] 
**multiline_value** | **bool** | The provided value is a multiline value (separated by &#39;\\n&#39;) | [optional] 
**name** | **str** | Secret name | 
**password_length** | **int** | For PasswordPolicy use | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_ssh_creds** | **str** |  | [optional] 
**secure_access_ssh_user** | **str** |  | [optional] 
**secure_access_url** | **str** |  | [optional] 
**secure_access_web_browsing** | **bool** |  | [optional] 
**secure_access_web_proxy** | **bool** |  | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | For Password Management use, reflect the website context | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_lower_letters** | **str** | For PasswordPolicy use | [optional] 
**use_numbers** | **str** | For PasswordPolicy use | [optional] 
**use_special_characters** | **str** | For PasswordPolicy use | [optional] 
**use_capital_letters** | **str** | For PasswordPolicy use | [optional] 
**username** | **str** | For Password Management use | [optional] 
**value** | **str** | The secret value | 
**website** | **str** | For Password Management use, reflect the website context | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


