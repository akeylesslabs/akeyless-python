# CacheConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_enable** | **bool** |  | [optional] 
**cache_encryption_key** | **str** |  | [optional] 
**cache_ttl** | **str** |  | [optional] 
**new_proactive_cache_enable** | **bool** |  | [optional] 
**proactive_cache_dump_interval** | **str** |  | [optional] 
**proactive_cache_enable** | **bool** |  | [optional] 
**proactive_cache_minimum_fetching_time** | **str** |  | [optional] 

## Example

```python
from akeyless.models.cache_config_part import CacheConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of CacheConfigPart from a JSON string
cache_config_part_instance = CacheConfigPart.from_json(json)
# print the JSON string representation of the object
print(CacheConfigPart.to_json())

# convert the object into a dict
cache_config_part_dict = cache_config_part_instance.to_dict()
# create an instance of CacheConfigPart from a dict
cache_config_part_from_dict = CacheConfigPart.from_dict(cache_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


