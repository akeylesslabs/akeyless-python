# DescribeSubClaims

describe-sub-claims Get the sub-claims associated with the provided token or authentication profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.describe_sub_claims import DescribeSubClaims

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeSubClaims from a JSON string
describe_sub_claims_instance = DescribeSubClaims.from_json(json)
# print the JSON string representation of the object
print(DescribeSubClaims.to_json())

# convert the object into a dict
describe_sub_claims_dict = describe_sub_claims_instance.to_dict()
# create an instance of DescribeSubClaims from a dict
describe_sub_claims_from_dict = DescribeSubClaims.from_dict(describe_sub_claims_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


