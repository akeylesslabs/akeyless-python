# GatewayCreateProducerArtifactory

gatewayCreateProducerArtifactory is a command that creates artifactory producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactory_admin_name** | **str** | Artifactory Admin Name | 
**artifactory_admin_pwd** | **str** | Artifactory Admin password | 
**artifactory_token_audience** | **str** | Token Audience | 
**artifactory_token_scope** | **str** | Token Scope | 
**base_url** | **str** | Base URL | 
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


