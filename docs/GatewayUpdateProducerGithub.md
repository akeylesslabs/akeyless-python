# GatewayUpdateProducerGithub

gatewayUpdateProducerGithub is a command that updates github producer [Deprecated: Use dynamic-secret-update-github command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**github_app_id** | **int** | Github app id | [optional] 
**github_app_private_key** | **str** | App private key | [optional] 
**github_base_url** | **str** | Base URL | [optional] [default to 'https://api.github.com/']
**installation_id** | **int** | GitHub application installation id | [optional] 
**installation_organization** | **str** | Optional, mutually exclusive with installation id, GitHub organization name | [optional] 
**installation_repository** | **str** | Optional, mutually exclusive with installation id, GitHub repository &#39;&lt;owner&gt;/&lt;repo-name&gt;&#39; | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_permissions** | **List[str]** | Optional - installation token&#39;s allowed permissions | [optional] 
**token_repositories** | **List[str]** | Optional - installation token&#39;s allowed repositories | [optional] 
**token_ttl** | **str** | Token TTL | [optional] [default to '60m']
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_producer_github import GatewayUpdateProducerGithub

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerGithub from a JSON string
gateway_update_producer_github_instance = GatewayUpdateProducerGithub.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerGithub.to_json())

# convert the object into a dict
gateway_update_producer_github_dict = gateway_update_producer_github_instance.to_dict()
# create an instance of GatewayUpdateProducerGithub from a dict
gateway_update_producer_github_from_dict = GatewayUpdateProducerGithub.from_dict(gateway_update_producer_github_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


