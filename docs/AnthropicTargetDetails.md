# AnthropicTargetDetails

AnthropicTargetDetails defines details related to connecting to an Anthropic provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anthropic_url** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**use_gw_cloud_identity** | **bool** | UseGatewayCloudIdentity authenticates with Anthropic Workload Identity Federation instead of ApiKey: the Gateway exchanges its own identity token for a short-lived Anthropic access token. ApiKey must be empty. See go/src/targets/llm/anthropic_wif_client.go. | [optional] 
**wif_azure_audience** | **str** | WIFAzureAudience is the identifier URI (api://&lt;app-id&gt;) of the Entra app registration that represents the Claude API audience. Required with the azure source, empty with every other source. | [optional] 
**wif_federation_rule_id** | **str** | WIFFederationRuleID is the federation rule ID (fdrl_...). | [optional] 
**wif_identity_token_source** | **str** | WIFIdentityTokenSource selects where the Gateway takes its identity token: file (default, projected Kubernetes or SPIFFE token), gcp (Google Cloud metadata server), aws (STS web identity token) or azure (Microsoft Entra ID). | [optional] 
**wif_organization_id** | **str** | WIFOrganizationID is the UUID of the Anthropic organization. | [optional] 
**wif_service_account_id** | **str** | WIFServiceAccountID is the Claude service account ID (svac_...). | [optional] 
**wif_workspace_id** | **str** | WIFWorkspaceID is the optional workspace ID (wrkspc_...). Required by Anthropic only when the rule is enabled for more than one workspace. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


