# GatewayUpdateProducerArtifactory

gatewayUpdateProducerArtifactory is a command that updates artifactory producer [Deprecated: Use dynamic-secret-update-artifactory command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactory_admin_name** | **str** | Artifactory Admin Name | [optional] 
**artifactory_admin_pwd** | **str** | Artifactory Admin password | [optional] 
**artifactory_token_audience** | **str** | Token Audience | 
**artifactory_token_scope** | **str** | Token Scope | 
**base_url** | **str** | Base URL | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_update_producer_artifactory import GatewayUpdateProducerArtifactory

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerArtifactory from a JSON string
gateway_update_producer_artifactory_instance = GatewayUpdateProducerArtifactory.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerArtifactory.to_json())

# convert the object into a dict
gateway_update_producer_artifactory_dict = gateway_update_producer_artifactory_instance.to_dict()
# create an instance of GatewayUpdateProducerArtifactory from a dict
gateway_update_producer_artifactory_from_dict = GatewayUpdateProducerArtifactory.from_dict(gateway_update_producer_artifactory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


