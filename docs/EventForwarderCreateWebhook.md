# EventForwarderCreateWebhook

eventForwarderCreateWebhook is a command that creates webhook event forwarder
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods_event_source_locations** | **list[str]** | Auth Method Event sources | [optional] 
**auth_token** | **str** | Base64 encoded Token string for authentication type Token | [optional] 
**auth_type** | **str** | The Webhook authentication type [user-pass, bearer-token, certificate] | [optional] [default to 'user-pass']
**client_cert_data** | **str** | Base64 encoded PEM certificate, relevant for certificate auth-type | [optional] 
**description** | **str** | Description of the object | [optional] 
**event_types** | **list[str]** | List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, next-automatic-rotation, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated, rate-limiting, usage-report, secret-sync] | [optional] 
**every** | **str** | Rate of periodic runner repetition in hours | [optional] 
**gateways_event_source_locations** | **list[str]** | Event sources | 
**items_event_source_locations** | **list[str]** | Items Event sources | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | EventForwarder name | 
**password** | **str** | Password for authentication relevant for user-pass auth-type | [optional] 
**private_key_data** | **str** | Base64 encoded PEM RSA Private Key, relevant for certificate auth-type | [optional] 
**runner_type** | **str** |  | 
**server_certificates** | **str** | Base64 encoded PEM certificate of the Webhook | [optional] 
**targets_event_source_locations** | **list[str]** | Targets Event sources | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**url** | **str** | Webhook URL | [optional] 
**username** | **str** | Username for authentication relevant for user-pass auth-type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


