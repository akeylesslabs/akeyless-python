# GatewayUpdateProducerDockerhub

gatewayUpdateProducerDockerhub is a command that updates a DOCKERHUB producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerhub_password** | **str** | DockerhubPassword is either the user&#39;s password access token to manage the repository | [optional] 
**dockerhub_token_scopes** | **str** | Access token scopes list (comma seperated) to give the dynamic secret valid options are in \&quot;repo:admin\&quot;, \&quot;repo:write\&quot;, \&quot;repo:read\&quot;, \&quot;repo:public_read\&quot; | [optional] 
**dockerhub_username** | **str** | DockerhubUsername is the name of the user in dockerhub | [optional] 
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


