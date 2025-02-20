# DescribeSubClaimsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from akeyless.models.describe_sub_claims_output import DescribeSubClaimsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeSubClaimsOutput from a JSON string
describe_sub_claims_output_instance = DescribeSubClaimsOutput.from_json(json)
# print the JSON string representation of the object
print(DescribeSubClaimsOutput.to_json())

# convert the object into a dict
describe_sub_claims_output_dict = describe_sub_claims_output_instance.to_dict()
# create an instance of DescribeSubClaimsOutput from a dict
describe_sub_claims_output_from_dict = DescribeSubClaimsOutput.from_dict(describe_sub_claims_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


