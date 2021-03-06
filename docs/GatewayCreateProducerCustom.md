# GatewayCreateProducerCustom

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_sync_url** | **str** | URL of an endpoint that implements /sync/create method, for example https://webhook.example.com/sync/create | 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**payload** | **str** | Secret payload to be sent with each create/revoke webhook request | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**revoke_sync_url** | **str** | URL of an endpoint that implements /sync/revoke method, for example https://webhook.example.com/sync/revoke | 
**rotate_sync_url** | **str** | URL of an endpoint that implements /sync/rotate method, for example https://webhook.example.com/sync/rotate | [optional] 
**timeout_sec** | **int** | Maximum allowed time in seconds for the webhook to return the results | [optional] [default to 60]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


