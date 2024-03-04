# GatewayUpdateProducerGithub

gatewayUpdateProducerGithub is a command that updates github producer [Deprecated: Use dynamic-secret-update-github command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**github_app_id** | **int** | Github app id | [optional] 
**github_app_private_key** | **str** | App private key | [optional] 
**github_base_url** | **str** | Base URL | [optional] [default to 'https://api.github.com/']
**installation_id** | **int** | Github app installation id | [optional] 
**installation_organization** | **str** | Optional, instead of installation id, set a GitHub organization name | [optional] 
**installation_repository** | **str** | Optional, instead of installation id, set a GitHub repository &#39;&lt;owner&gt;/&lt;repo-name&gt; | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_permissions** | **list[str]** | Optional - installation token&#39;s allowed permissions | [optional] 
**token_repositories** | **list[str]** | Optional - installation token&#39;s allowed repositories | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


