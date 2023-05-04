# Configure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access Key | [optional] 
**access_type** | **str** | Access Type (access_key/password/azure_ad/saml/oidc/aws_iam/gcp/k8s/cert) | [optional] [default to 'access_key']
**account_id** | **str** | Account id (relevant only for access-type&#x3D;password where the email address is associated with more than one account) | [optional] 
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**azure_ad_object_id** | **str** | Azure Active Directory ObjectId (relevant only for access-type&#x3D;azure_ad) | [optional] 
**cert_data** | **str** | Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type&#x3D;cert in Curl Context) | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] [default to 'akeyless.io']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_auth_config_name** | **str** | The K8S Auth config name (relevant only for access-type&#x3D;k8s) | [optional] 
**key_data** | **str** | Private key data encoded in base64. Used if file was not provided.(relevant only for access-type&#x3D;cert in Curl Context) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


