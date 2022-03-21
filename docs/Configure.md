# Configure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access Key | [optional] 
**access_type** | **str** | Access Type (access_key/password/azure_ad/saml/oidc/aws_iam/gcp/k8s) | [optional] [default to 'access_key']
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**azure_ad_object_id** | **str** | Azure Active Directory ObjectId (relevant only for access-type&#x3D;azure_ad) | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] 
**k8s_auth_config_name** | **str** | The K8S Auth config name (relevant only for access-type&#x3D;k8s) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


