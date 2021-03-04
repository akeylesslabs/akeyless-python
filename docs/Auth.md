# Auth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access key (relevant only for access-type&#x3D;access_key) | [optional] 
**access_type** | **str** | Access Type (access_key/password/saml/ldap/azure_ad/aws_iam/universal_identity/jwt/gcp) | [optional] [default to 'access_key']
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**cloud_id** | **str** | The cloud identity (relevant only for access-type&#x3D;azure_ad,aws_iam,gcp) | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] 
**jwt** | **str** | The Json Web Token (relevant only for access-type&#x3D;jwt/oidc) | [optional] 
**ldap_password** | **str** | LDAP password (relevant only for access-type&#x3D;ldap) | [optional] 
**ldap_username** | **str** | LDAP username (relevant only for access-type&#x3D;ldap) | [optional] 
**uid_token** | **str** | The universal_identity token (relevant only for access-type&#x3D;universal_identity) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


