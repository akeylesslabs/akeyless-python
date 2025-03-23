# UpdateSSHCertIssuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**add_tag** | **List[str]** | List of the new tags that will be attached to this item | [optional] 
**allowed_users** | **str** | Users allowed to fetch the certificate, e.g root,ubuntu | [default to '-']
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**extensions** | **Dict[str, str]** | Signed certificates with extensions, e.g permit-port-forwarding&#x3D;\\\&quot;\\\&quot; | [optional] 
**external_username** | **str** | Externally provided username [true/false] | [optional] [default to 'false']
**fixed_user_claim_keyname** | **str** | For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for external-username&#x3D;true) | [optional] 
**host_provider** | **str** | Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | SSH certificate issuer name | 
**new_name** | **str** | New item name | [optional] 
**principals** | **str** | Signed certificates with principal, e.g example_role1,example_role2 | [optional] 
**rm_tag** | **List[str]** | List of the existent tags that will be removed from this item | [optional] 
**secure_access_api** | **str** | Secure Access SSH control API endpoint. E.g. https://my.sra-server:9900 | [optional] 
**secure_access_bastion_api** | **str** | Deprecated. use secure-access-api | [optional] 
**secure_access_bastion_ssh** | **str** | Deprecated. use secure-access-ssh | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_enforce_hosts_restriction** | **bool** | Enable this flag to enforce connections only to the hosts listed in --secure-access-host | [optional] 
**secure_access_gateway** | **str** |  | [optional] 
**secure_access_host** | **List[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_ssh** | **str** | Bastion&#39;s SSH server. E.g. my.sra-server:22 | [optional] 
**secure_access_ssh_creds_user** | **str** | SSH username to connect to target server, must be in &#39;Allowed Users&#39; list | [optional] 
**secure_access_use_internal_bastion** | **bool** | Deprecated. Use secure-access-use-internal-ssh-access | [optional] 
**secure_access_use_internal_ssh_access** | **bool** | Use internal SSH Access | [optional] 
**signer_key_name** | **str** | A key to sign the certificate with | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | The requested Time To Live for the certificate, in seconds | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_ssh_cert_issuer import UpdateSSHCertIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSSHCertIssuer from a JSON string
update_ssh_cert_issuer_instance = UpdateSSHCertIssuer.from_json(json)
# print the JSON string representation of the object
print(UpdateSSHCertIssuer.to_json())

# convert the object into a dict
update_ssh_cert_issuer_dict = update_ssh_cert_issuer_instance.to_dict()
# create an instance of UpdateSSHCertIssuer from a dict
update_ssh_cert_issuer_from_dict = UpdateSSHCertIssuer.from_dict(update_ssh_cert_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


