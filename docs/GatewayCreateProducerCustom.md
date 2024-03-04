# GatewayCreateProducerCustom

gatewayCreateProducerCustom is a command that creates a custom producer. [Deprecated: Use dynamic-secret-create-custom command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_rotation_interval_days** | **int** | Define rotation interval in days | [optional] 
**create_sync_url** | **str** | URL of an endpoint that implements /sync/create method, for example https://webhook.example.com/sync/create | 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**enable_admin_rotation** | **bool** | Should admin credentials be rotated | [optional] [default to False]
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**payload** | **str** | Secret payload to be sent with each create/revoke webhook request | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**revoke_sync_url** | **str** | URL of an endpoint that implements /sync/revoke method, for example https://webhook.example.com/sync/revoke | 
**rotate_sync_url** | **str** | URL of an endpoint that implements /sync/rotate method, for example https://webhook.example.com/sync/rotate | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**timeout_sec** | **int** | Maximum allowed time in seconds for the webhook to return the results | [optional] [default to 60]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


