# AtlassianTargetDetails

An Atlassian site (Jira, Confluence or both) credential, on Atlassian Cloud or Data Center. Cloud uses the site URL (https://<site>.atlassian.net) with an OAuth 2.0 service account, a service account API token, or a user API token paired with the account email. Data Center uses a personal access token per product, with its own Jira and Confluence URLs. Read by the SDR Atlassian scanner.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atlassian_auth_type** | **str** |  | [optional] 
**atlassian_automation_key** | **str** | AtlassianAutomationKey is an optional Automation REST API key (Jira settings &gt; System &gt; Automation &gt; API keys). Atlassian&#39;s automation API refuses an account API token, so without this key the scanner reports the automation rules as not read. | [optional] 
**atlassian_ca_certificate** | **str** | AtlassianCACertificate is a base64-encoded PEM CA certificate for a Data Center site signed by a private CA. | [optional] 
**atlassian_client_id** | **str** |  | [optional] 
**atlassian_client_secret** | **str** |  | [optional] 
**atlassian_cloud_id** | **str** |  | [optional] 
**atlassian_confluence_token** | **str** |  | [optional] 
**atlassian_confluence_url** | **str** |  | [optional] 
**atlassian_deployment_type** | **str** | When empty, the deployment type, auth type and products are inferred from the fields above, so targets saved before these fields existed keep working. | [optional] 
**atlassian_email** | **str** |  | [optional] 
**atlassian_jira_token** | **str** |  | [optional] 
**atlassian_jira_url** | **str** |  | [optional] 
**atlassian_products** | **list[str]** |  | [optional] 
**atlassian_token** | **str** |  | [optional] 
**atlassian_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


