# UpdateAssoc

updateAssoc is a command that updates the sub-claims of an association between role and auth method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** | The association id to be updated | 
**case_sensitive** | **str** | Treat sub claims as case-sensitive [true/false] | [optional] [default to 'true']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**sub_claims** | **Dict[str, str]** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_assoc import UpdateAssoc

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssoc from a JSON string
update_assoc_instance = UpdateAssoc.from_json(json)
# print the JSON string representation of the object
print(UpdateAssoc.to_json())

# convert the object into a dict
update_assoc_dict = update_assoc_instance.to_dict()
# create an instance of UpdateAssoc from a dict
update_assoc_from_dict = UpdateAssoc.from_dict(update_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


