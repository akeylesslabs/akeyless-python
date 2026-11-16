# TargetUpdateAtlassian

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atlassian_auth_type** | **str** | Atlassian auth type: oauth, service_account_token or user_api_token on cloud, pat on data center | [optional] 
**atlassian_automation_key** | **str** | Optional Automation REST API key (Jira settings &gt; System &gt; Automation &gt; API keys); the automation API refuses an account token, so without it the automation rules are reported as not read | [optional] 
**atlassian_ca_certificate** | **str** | CA certificate (base64-encoded PEM) of a Data Center site signed by a private CA | [optional] 
**atlassian_client_id** | **str** | Atlassian OAuth 2.0 service account client ID | [optional] 
**atlassian_client_secret** | **str** | Atlassian OAuth 2.0 service account client secret | [optional] 
**atlassian_cloud_id** | **str** | Atlassian Cloud ID of the site (resolved from the site URL when empty) | [optional] 
**atlassian_confluence_token** | **str** | Confluence Data Center personal access token | [optional] 
**atlassian_confluence_url** | **str** | Confluence Data Center base URL | [optional] 
**atlassian_deployment_type** | **str** | Atlassian deployment type: cloud or data_center (inferred from the URL when empty) | [optional] 
**atlassian_email** | **str** | Atlassian account email paired with a user API token | [optional] 
**atlassian_jira_token** | **str** | Jira Data Center personal access token | [optional] 
**atlassian_jira_url** | **str** | Jira Data Center base URL | [optional] 
**atlassian_products** | **list[str]** | Atlassian products to connect to on cloud: jira, confluence or both (default both) | [optional] 
**atlassian_token** | **str** | Atlassian Cloud service account API token or user API token | [optional] 
**atlassian_url** | **str** | Atlassian Cloud site base URL (https://&lt;site&gt;.atlassian.net) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**lock_on_read** | **str** | Lock this secret after each successful value read | [optional] 
**lock_ttl** | **str** | Lock TTL in minutes | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**rotate_on_unlock** | **str** | Rotate this secret after it is unlocked | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


