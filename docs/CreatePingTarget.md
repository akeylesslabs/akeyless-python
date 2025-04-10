# CreatePingTarget

createPingTarget is a command that creates a new target. [Deprecated: Use target-create-ping command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_port** | **str** | Ping Federate administrative port | [optional] [default to '9999']
**authorization_port** | **str** | Ping Federate authorization port | [optional] [default to '9031']
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**password** | **str** | Ping Federate privileged user password | [optional] 
**ping_url** | **str** | Ping URL | [optional] 
**privileged_user** | **str** | Ping Federate privileged user | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


