# CustomerFragmentsConfigJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_fragments** | [**List[CustomerFragmentConfig]**](CustomerFragmentConfig.md) |  | [optional] 

## Example

```python
from akeyless.models.customer_fragments_config_json import CustomerFragmentsConfigJson

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFragmentsConfigJson from a JSON string
customer_fragments_config_json_instance = CustomerFragmentsConfigJson.from_json(json)
# print the JSON string representation of the object
print(CustomerFragmentsConfigJson.to_json())

# convert the object into a dict
customer_fragments_config_json_dict = customer_fragments_config_json_instance.to_dict()
# create an instance of CustomerFragmentsConfigJson from a dict
customer_fragments_config_json_from_dict = CustomerFragmentsConfigJson.from_dict(customer_fragments_config_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


