# CreateGKETarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment about the target | [optional] 
**gke_cluster_cert** | **str** | GKE cluster CA certificate | 
**gke_cluster_endpoint** | **str** | GKE cluster URL endpoint | 
**gke_cluster_name** | **str** | GKE cluster name | 
**gke_service_account_email** | **str** | GKE service account email | 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Target name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


