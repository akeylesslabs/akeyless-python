# CustomerFragmentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**fragment_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key_label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from akeyless.models.customer_fragment_config import CustomerFragmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFragmentConfig from a JSON string
customer_fragment_config_instance = CustomerFragmentConfig.from_json(json)
# print the JSON string representation of the object
print(CustomerFragmentConfig.to_json())

# convert the object into a dict
customer_fragment_config_dict = customer_fragment_config_instance.to_dict()
# create an instance of CustomerFragmentConfig from a dict
customer_fragment_config_from_dict = CustomerFragmentConfig.from_dict(customer_fragment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


