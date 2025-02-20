# CustomerFullAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**street** | **str** |  | [optional] 

## Example

```python
from akeyless.models.customer_full_address import CustomerFullAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFullAddress from a JSON string
customer_full_address_instance = CustomerFullAddress.from_json(json)
# print the JSON string representation of the object
print(CustomerFullAddress.to_json())

# convert the object into a dict
customer_full_address_dict = customer_full_address_instance.to_dict()
# create an instance of CustomerFullAddress from a dict
customer_full_address_from_dict = CustomerFullAddress.from_dict(customer_full_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


