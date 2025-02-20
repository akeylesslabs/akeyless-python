# CreateDynamicSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the dynamic secret values (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Dynamic secret name | 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_dynamic_secret import CreateDynamicSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDynamicSecret from a JSON string
create_dynamic_secret_instance = CreateDynamicSecret.from_json(json)
# print the JSON string representation of the object
print(CreateDynamicSecret.to_json())

# convert the object into a dict
create_dynamic_secret_dict = create_dynamic_secret_instance.to_dict()
# create an instance of CreateDynamicSecret from a dict
create_dynamic_secret_from_dict = CreateDynamicSecret.from_dict(create_dynamic_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


