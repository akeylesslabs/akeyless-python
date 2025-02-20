# ElasticsearchLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elasticsearch_api_key** | **str** |  | [optional] 
**elasticsearch_auth_type** | **str** |  | [optional] 
**elasticsearch_cloud_id** | **str** |  | [optional] 
**elasticsearch_enable_tls** | **bool** |  | [optional] 
**elasticsearch_index** | **str** |  | [optional] 
**elasticsearch_nodes** | **str** |  | [optional] 
**elasticsearch_password** | **str** |  | [optional] 
**elasticsearch_server_type** | **str** |  | [optional] 
**elasticsearch_tls_certificate** | **str** |  | [optional] 
**elasticsearch_user_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.elasticsearch_log_forwarding_config import ElasticsearchLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticsearchLogForwardingConfig from a JSON string
elasticsearch_log_forwarding_config_instance = ElasticsearchLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(ElasticsearchLogForwardingConfig.to_json())

# convert the object into a dict
elasticsearch_log_forwarding_config_dict = elasticsearch_log_forwarding_config_instance.to_dict()
# create an instance of ElasticsearchLogForwardingConfig from a dict
elasticsearch_log_forwarding_config_from_dict = ElasticsearchLogForwardingConfig.from_dict(elasticsearch_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


