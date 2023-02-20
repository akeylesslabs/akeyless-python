# Auth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access key (relevant only for access-type&#x3D;access_key) | [optional] 
**access_type** | **str** | Access Type (access_key/password/saml/ldap/k8s/azure_ad/oidc/aws_iam/universal_identity/jwt/gcp/cert) | [optional] [default to 'access_key']
**account_id** | **str** | Account id (relevant only for access-type&#x3D;password where the email address is associated with more than one account) | [optional] 
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**cert_data** | **str** | Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type&#x3D;cert) | [optional] 
**cloud_id** | **str** | The cloud identity (relevant only for access-type&#x3D;azure_ad,aws_iam,gcp) | [optional] 
**debug** | **bool** |  | [optional] 
**gateway_url** | **str** | Gateway URL for the K8S authenticated (relevant only for access-type&#x3D;k8s) | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] [default to 'akeyless.io']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt** | **str** | The Json Web Token (relevant only for access-type&#x3D;jwt/oidc) | [optional] 
**k8s_auth_config_name** | **str** | The K8S Auth config name (relevant only for access-type&#x3D;k8s) | [optional] 
**k8s_service_account_token** | **str** | The K8S service account token. (relevant only for access-type&#x3D;k8s) | [optional] 
**key_data** | **str** | Private key data encoded in base64. Used if file was not provided.(relevant only for access-type&#x3D;cert) | [optional] 
**ldap_password** | **str** | LDAP password (relevant only for access-type&#x3D;ldap) | [optional] 
**ldap_username** | **str** | LDAP username (relevant only for access-type&#x3D;ldap) | [optional] 
**uid_token** | **str** | The universal_identity token (relevant only for access-type&#x3D;universal_identity) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


