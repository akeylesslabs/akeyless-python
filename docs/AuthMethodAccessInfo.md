# AuthMethodAccessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** |  | [optional] 
**access_id_alias** | **str** | for accounts where AccessId holds encrypted email this field will hold generated AccessId, for accounts based on regular AccessId it will be equal to accessId itself | [optional] 
**api_key_access_rules** | [**APIKeyAccessRules**](APIKeyAccessRules.md) |  | [optional] 
**audit_logs_claims** | **List[str]** |  | [optional] 
**aws_iam_access_rules** | [**AWSIAMAccessRules**](AWSIAMAccessRules.md) |  | [optional] 
**azure_ad_access_rules** | [**AzureADAccessRules**](AzureADAccessRules.md) |  | [optional] 
**cert_access_rules** | [**CertAccessRules**](CertAccessRules.md) |  | [optional] 
**cidr_whitelist** | **str** |  | [optional] 
**email_pass_access_rules** | [**EmailPassAccessRules**](EmailPassAccessRules.md) |  | [optional] 
**force_sub_claims** | **bool** | if true the role associated with this auth method must include sub claims | [optional] 
**gcp_access_rules** | [**GCPAccessRules**](GCPAccessRules.md) |  | [optional] 
**gw_cidr_whitelist** | **str** |  | [optional] 
**huawei_access_rules** | [**HuaweiAccessRules**](HuaweiAccessRules.md) |  | [optional] 
**jwt_ttl** | **int** |  | [optional] 
**k8s_access_rules** | [**KubernetesAccessRules**](KubernetesAccessRules.md) |  | [optional] 
**kerberos_access_rules** | [**KerberosAccessRules**](KerberosAccessRules.md) |  | [optional] 
**ldap_access_rules** | [**LDAPAccessRules**](LDAPAccessRules.md) |  | [optional] 
**oauth2_access_rules** | [**OAuth2AccessRules**](OAuth2AccessRules.md) |  | [optional] 
**oci_access_rules** | [**OCIAccessRules**](OCIAccessRules.md) |  | [optional] 
**oidc_access_rules** | [**OIDCAccessRules**](OIDCAccessRules.md) |  | [optional] 
**product_types** | **List[str]** | List of product types this auth method will be in use of | [optional] 
**rules_type** | **str** |  | [optional] 
**saml_access_rules** | [**SAMLAccessRules**](SAMLAccessRules.md) |  | [optional] 
**sub_claims_delimiters** | **List[str]** |  | [optional] 
**universal_identity_access_rules** | [**UniversalIdentityAccessRules**](UniversalIdentityAccessRules.md) |  | [optional] 

## Example

```python
from akeyless.models.auth_method_access_info import AuthMethodAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodAccessInfo from a JSON string
auth_method_access_info_instance = AuthMethodAccessInfo.from_json(json)
# print the JSON string representation of the object
print(AuthMethodAccessInfo.to_json())

# convert the object into a dict
auth_method_access_info_dict = auth_method_access_info_instance.to_dict()
# create an instance of AuthMethodAccessInfo from a dict
auth_method_access_info_from_dict = AuthMethodAccessInfo.from_dict(auth_method_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


