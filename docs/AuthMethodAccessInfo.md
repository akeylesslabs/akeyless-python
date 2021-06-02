# AuthMethodAccessInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** |  | [optional] 
**access_id_alias** | **str** | for accounts where AccessId holds encrypted email this field will hold generated AccessId, for accounts based on regular AccessId it will be equal to accessId itself | [optional] 
**api_key_access_rules** | [**APIKeyAccessRules**](APIKeyAccessRules.md) |  | [optional] 
**aws_iam_access_rules** | [**AWSIAMAccessRules**](AWSIAMAccessRules.md) |  | [optional] 
**azure_ad_access_rules** | [**AzureADAccessRules**](AzureADAccessRules.md) |  | [optional] 
**cidr_whitelist** | **str** |  | [optional] 
**email_pass_access_rules** | [**EmailPassAccessRules**](EmailPassAccessRules.md) |  | [optional] 
**force_sub_claims** | **bool** | if true the role associated with this auth method must include sub claims | [optional] 
**gcp_access_rules** | [**GCPAccessRules**](GCPAccessRules.md) |  | [optional] 
**huawei_access_rules** | [**HuaweiAccessRules**](HuaweiAccessRules.md) |  | [optional] 
**ldap_access_rules** | [**LDAPAccessRules**](LDAPAccessRules.md) |  | [optional] 
**oauth2_access_rules** | [**OAuth2AccessRules**](OAuth2AccessRules.md) |  | [optional] 
**rules_type** | **str** |  | [optional] 
**saml_access_rules** | [**SAMLAccessRules**](SAMLAccessRules.md) |  | [optional] 
**universal_identity_access_rules** | [**UniversalIdentityAccessRules**](UniversalIdentityAccessRules.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


