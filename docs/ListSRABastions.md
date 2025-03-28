# ListSRABastions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_urls_only** | **bool** | Filter the response to show only bastions allowed URLs | [optional] [default to False]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_sra_bastions import ListSRABastions

# TODO update the JSON string below
json = "{}"
# create an instance of ListSRABastions from a JSON string
list_sra_bastions_instance = ListSRABastions.from_json(json)
# print the JSON string representation of the object
print(ListSRABastions.to_json())

# convert the object into a dict
list_sra_bastions_dict = list_sra_bastions_instance.to_dict()
# create an instance of ListSRABastions from a dict
list_sra_bastions_from_dict = ListSRABastions.from_dict(list_sra_bastions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


