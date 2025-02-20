# AliasDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_alias** | **str** | Account alias | 
**auth_method_name** | **str** | Auth method name | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]

## Example

```python
from akeyless.models.alias_details import AliasDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AliasDetails from a JSON string
alias_details_instance = AliasDetails.from_json(json)
# print the JSON string representation of the object
print(AliasDetails.to_json())

# convert the object into a dict
alias_details_dict = alias_details_instance.to_dict()
# create an instance of AliasDetails from a dict
alias_details_from_dict = AliasDetails.from_dict(alias_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


