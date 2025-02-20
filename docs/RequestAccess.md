# RequestAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **List[str]** | List of the required capabilities options: [read, update, delete] | 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Item name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Item type | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.request_access import RequestAccess

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAccess from a JSON string
request_access_instance = RequestAccess.from_json(json)
# print the JSON string representation of the object
print(RequestAccess.to_json())

# convert the object into a dict
request_access_dict = request_access_instance.to_dict()
# create an instance of RequestAccess from a dict
request_access_from_dict = RequestAccess.from_dict(request_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


