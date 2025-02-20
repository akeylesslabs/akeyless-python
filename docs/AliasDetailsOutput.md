# AliasDetailsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** |  | [optional] 
**tenant_tag** | **str** |  | [optional] 

## Example

```python
from akeyless.models.alias_details_output import AliasDetailsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AliasDetailsOutput from a JSON string
alias_details_output_instance = AliasDetailsOutput.from_json(json)
# print the JSON string representation of the object
print(AliasDetailsOutput.to_json())

# convert the object into a dict
alias_details_output_dict = alias_details_output_instance.to_dict()
# create an instance of AliasDetailsOutput from a dict
alias_details_output_from_dict = AliasDetailsOutput.from_dict(alias_details_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


