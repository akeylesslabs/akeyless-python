# DescribeAssoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** | The association id | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.describe_assoc import DescribeAssoc

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeAssoc from a JSON string
describe_assoc_instance = DescribeAssoc.from_json(json)
# print the JSON string representation of the object
print(DescribeAssoc.to_json())

# convert the object into a dict
describe_assoc_dict = describe_assoc_instance.to_dict()
# create an instance of DescribeAssoc from a dict
describe_assoc_from_dict = DescribeAssoc.from_dict(describe_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


