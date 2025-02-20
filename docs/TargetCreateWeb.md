# TargetCreateWeb

targetCreateWeb is a command that creates a new web target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**url** | **str** | The url | [optional] 

## Example

```python
from akeyless.models.target_create_web import TargetCreateWeb

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateWeb from a JSON string
target_create_web_instance = TargetCreateWeb.from_json(json)
# print the JSON string representation of the object
print(TargetCreateWeb.to_json())

# convert the object into a dict
target_create_web_dict = target_create_web_instance.to_dict()
# create an instance of TargetCreateWeb from a dict
target_create_web_from_dict = TargetCreateWeb.from_dict(target_create_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


