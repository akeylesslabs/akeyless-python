# GatewayUpdateLogForwardingElasticsearch

gatewayUpdateLogForwardingElasticsearch is a command that updates log forwarding config (elasticsearch target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Elasticsearch api key relevant only for api_key auth-type | [optional] 
**auth_type** | **str** | Elasticsearch auth type [api_key/password] | [optional] 
**cloud_id** | **str** | Elasticsearch cloud id relevant only for cloud server-type | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**index** | **str** | Elasticsearch index | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**nodes** | **str** | Elasticsearch nodes relevant only for nodes server-type | [optional] 
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**password** | **str** | Elasticsearch password relevant only for password auth-type | [optional] 
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**server_type** | **str** | Elasticsearch server type [cloud/nodes] | [optional] 
**tls_certificate** | **str** | Elasticsearch tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_name** | **str** | Elasticsearch user name relevant only for password auth-type | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_elasticsearch import GatewayUpdateLogForwardingElasticsearch

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingElasticsearch from a JSON string
gateway_update_log_forwarding_elasticsearch_instance = GatewayUpdateLogForwardingElasticsearch.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingElasticsearch.to_json())

# convert the object into a dict
gateway_update_log_forwarding_elasticsearch_dict = gateway_update_log_forwarding_elasticsearch_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingElasticsearch from a dict
gateway_update_log_forwarding_elasticsearch_from_dict = GatewayUpdateLogForwardingElasticsearch.from_dict(gateway_update_log_forwarding_elasticsearch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


