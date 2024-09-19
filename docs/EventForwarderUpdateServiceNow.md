# EventForwarderUpdateServiceNow

eventForwarderUpdateServiceNow is a command that updates service now event forwarder
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** | Workstation Admin Name | [optional] 
**admin_pwd** | **str** | Workstation Admin Password | [optional] 
**app_private_key_base64** | **str** | The RSA Private Key to use when connecting with jwt authentication | [optional] 
**auth_methods_event_source_locations** | **list[str]** | Auth Method Event sources | [optional] 
**auth_type** | **str** | The authentication type to use [user-pass/jwt] | [optional] [default to 'user-pass']
**client_id** | **str** | The client ID to use when connecting with jwt authentication | [optional] 
**client_secret** | **str** | The client secret to use when connecting with jwt authentication | [optional] 
**description** | **str** | Description of the object | [optional] 
**enable** | **str** | Enable/Disable Event Forwarder [true/false] | [optional] [default to 'true']
**event_types** | **list[str]** | List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, next-automatic-rotation, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated] | [optional] 
**gateways_event_source_locations** | **list[str]** | Event sources | 
**host** | **str** | Workstation Host | [optional] 
**items_event_source_locations** | **list[str]** | Items Event sources | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | EventForwarder name | 
**new_name** | **str** | New EventForwarder name | [optional] 
**targets_event_source_locations** | **list[str]** | Targets Event sources | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_email** | **str** | The user email to identify with when connecting with jwt authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


