# GatewayCreateProducerGke

gatewayCreateProducerGke is a command that creates gke producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**gke_cluster_cert** | **str** | GKE cluster CA certificate | 
**gke_cluster_endpoint** | **str** | GKE cluster URL endpoint | 
**gke_cluster_name** | **str** | GKE cluster name | 
**gke_service_account_email** | **str** | GKE service account email | 
**gke_service_account_key_file_path** | **str** | GKE Service Account key faile path | 
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


