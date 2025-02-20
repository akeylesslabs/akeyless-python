# GenCustomerFragment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**hsm_key_label** | **str** | The label of the hsm key to use for customer fragment operations (relevant for hsm_wrapped/hsm_protected customer fragments) | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Customer fragment name | [optional] 
**type** | **str** | Customer fragment type [standard/hsm_wrapped/hsm_secured] | [optional] [default to 'standard']

## Example

```python
from akeyless.models.gen_customer_fragment import GenCustomerFragment

# TODO update the JSON string below
json = "{}"
# create an instance of GenCustomerFragment from a JSON string
gen_customer_fragment_instance = GenCustomerFragment.from_json(json)
# print the JSON string representation of the object
print(GenCustomerFragment.to_json())

# convert the object into a dict
gen_customer_fragment_dict = gen_customer_fragment_instance.to_dict()
# create an instance of GenCustomerFragment from a dict
gen_customer_fragment_from_dict = GenCustomerFragment.from_dict(gen_customer_fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


