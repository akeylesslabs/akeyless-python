# UidListChildren

uidListChildren is a command that lists child token ids of Akeyless Universal Identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** | The universal identity auth method name, required only when uid-token is not provided | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.uid_list_children import UidListChildren

# TODO update the JSON string below
json = "{}"
# create an instance of UidListChildren from a JSON string
uid_list_children_instance = UidListChildren.from_json(json)
# print the JSON string representation of the object
print(UidListChildren.to_json())

# convert the object into a dict
uid_list_children_dict = uid_list_children_instance.to_dict()
# create an instance of UidListChildren from a dict
uid_list_children_from_dict = UidListChildren.from_dict(uid_list_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


