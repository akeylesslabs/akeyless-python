# ConfigHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins** | **str** |  | [optional] 
**cache** | **str** |  | [optional] 
**customer_fragements** | **str** |  | [optional] 
**general** | **str** |  | [optional] 
**k8s_auths** | **str** |  | [optional] 
**kmip** | **str** |  | [optional] 
**ldap** | **str** |  | [optional] 
**leadership** | **str** |  | [optional] 
**log_forwarding** | **str** |  | [optional] 
**m_queue** | **str** |  | [optional] 
**migration_status** | **str** |  | [optional] 
**migrations** | **str** |  | [optional] 
**producers** | **object** |  | [optional] 
**producers_status** | **str** |  | [optional] 
**rotators** | **object** |  | [optional] 
**saml** | **str** |  | [optional] 
**universal_identity** | **str** |  | [optional] 

## Example

```python
from akeyless.models.config_hash import ConfigHash

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigHash from a JSON string
config_hash_instance = ConfigHash.from_json(json)
# print the JSON string representation of the object
print(ConfigHash.to_json())

# convert the object into a dict
config_hash_dict = config_hash_instance.to_dict()
# create an instance of ConfigHash from a dict
config_hash_from_dict = ConfigHash.from_dict(config_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


