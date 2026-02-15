# TargetUpdateLetsEncrypt

targetUpdateLetsEncrypt is a command that updates an existing Let's Encrypt target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_challenge** | **str** |  | [optional] [default to 'http']
**description** | **str** | Description of the object | [optional] 
**dns_target_creds** | **str** | Name of existing cloud target for DNS credentials. Required when acme-challenge&#x3D;dns. Supported: AWS, Azure, GCP targets | [optional] 
**email** | **str** | Email address for ACME account registration | [optional] 
**gcp_project** | **str** | GCP Cloud DNS: Project ID. Optional - can be derived from service account | [optional] 
**hosted_zone** | **str** | AWS Route53 hosted zone ID. Required when dns-target-creds points to AWS target | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**lets_encrypt_url** | **str** |  | [optional] [default to 'production']
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**resource_group** | **str** | Azure resource group name. Required when dns-target-creds points to Azure target | [optional] 
**timeout** | **str** |  | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


