# TargetCreateLinked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**hosts** | **str** | A comma seperated list of server hosts and server descriptions joined by semicolon &#39;;&#39; (i.e. &#39;server-dev.com;My Dev server,server-prod.com;My Prod server description&#39;) | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Target name | 
**parent_target_name** | **str** | The parent Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Specifies the hosts type, relevant only when working without parent target | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_create_linked import TargetCreateLinked

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateLinked from a JSON string
target_create_linked_instance = TargetCreateLinked.from_json(json)
# print the JSON string representation of the object
print(TargetCreateLinked.to_json())

# convert the object into a dict
target_create_linked_dict = target_create_linked_instance.to_dict()
# create an instance of TargetCreateLinked from a dict
target_create_linked_from_dict = TargetCreateLinked.from_dict(target_create_linked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


