# UscList

uscList is a command that lists the secrets of a Universal Secrets Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Name of the Universal Secrets Connector item | 

## Example

```python
from akeyless.models.usc_list import UscList

# TODO update the JSON string below
json = "{}"
# create an instance of UscList from a JSON string
usc_list_instance = UscList.from_json(json)
# print the JSON string representation of the object
print(UscList.to_json())

# convert the object into a dict
usc_list_dict = usc_list_instance.to_dict()
# create an instance of UscList from a dict
usc_list_from_dict = UscList.from_dict(usc_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


