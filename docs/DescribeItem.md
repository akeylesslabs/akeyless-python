# DescribeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**bastion_details** | **bool** | Indicate if the item should return with ztb cluster details (url, etc) | [optional] [default to False]
**der_certificate_format** | **bool** | The certificate will be displayed in DER format | [optional] [default to False]
**display_id** | **str** | The display id of the item | [optional] 
**gateway_details** | **bool** | Indicate if the item should return with clusters details (url, etc) | [optional] [default to False]
**item_id** | **int** | Item id of the item | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Item name | 
**services_details** | **bool** | Include all associated services details | [optional] [default to False]
**show_versions** | **bool** | Include all item versions in reply | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.describe_item import DescribeItem

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeItem from a JSON string
describe_item_instance = DescribeItem.from_json(json)
# print the JSON string representation of the object
print(DescribeItem.to_json())

# convert the object into a dict
describe_item_dict = describe_item_instance.to_dict()
# create an instance of DescribeItem from a dict
describe_item_from_dict = DescribeItem.from_dict(describe_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


