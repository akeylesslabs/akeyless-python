# TargetUpdateLinked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_hosts** | **str** | A comma seperated list of new server hosts and server descriptions joined by semicolon &#39;;&#39; that will be added to the Linked Target hosts. | [optional] 
**description** | **str** | Description of the object | [optional] 
**hosts** | **str** | A comma seperated list of server hosts and server descriptions joined by semicolon &#39;;&#39; (i.e. &#39;server-dev.com;My Dev server,server-prod.com;My Prod server description&#39;) | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**name** | **str** | Linked Target name | 
**new_name** | **str** | New Linked Target name | [optional] 
**parent_target_name** | **str** | The parent Target name | [optional] 
**rm_hosts** | **str** | Comma separated list of existing hosts that will be removed from Linked Target hosts. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Specifies the hosts type, relevant only when working without parent target | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_update_linked import TargetUpdateLinked

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateLinked from a JSON string
target_update_linked_instance = TargetUpdateLinked.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateLinked.to_json())

# convert the object into a dict
target_update_linked_dict = target_update_linked_instance.to_dict()
# create an instance of TargetUpdateLinked from a dict
target_update_linked_from_dict = TargetUpdateLinked.from_dict(target_update_linked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


