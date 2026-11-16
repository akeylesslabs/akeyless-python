# TargetCreateAnthropic

targetCreateAnthropic is a command that creates a new anthropic target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anthropic_url** | **str** | Base URL of the Anthropic API | [optional] [default to 'https://api.anthropic.com']
**api_key** | **str** | API key for Anthropic | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**lock_on_read** | **str** | Lock this secret after each successful value read | [optional] 
**lock_ttl** | **str** | Lock TTL in minutes | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**rotate_on_unlock** | **str** | Rotate this secret after it is unlocked | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** | Use the Gateway&#39;s cloud identity (Anthropic Workload Identity Federation) instead of an API key | [optional] 
**wif_azure_audience** | **str** | Identifier URI (api://&lt;app-id&gt;) of the Entra app registration for the Claude API audience, required with the azure source | [optional] 
**wif_federation_rule_id** | **str** | Federation rule ID (fdrl_...), required with use-gw-cloud-identity | [optional] 
**wif_identity_token_source** | **str** | Where the Gateway reads its identity token: file (default), gcp, aws or azure | [optional] 
**wif_organization_id** | **str** | Anthropic organization ID (UUID), required with use-gw-cloud-identity | [optional] 
**wif_service_account_id** | **str** | Claude service account ID (svac_...), required with use-gw-cloud-identity | [optional] 
**wif_workspace_id** | **str** | Workspace ID (wrkspc_...), needed only when the federation rule covers more than one workspace | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


