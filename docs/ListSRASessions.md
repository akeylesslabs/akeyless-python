# ListSRASessions

listSRASessions is a command that returns sra sessions of the given user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**resource_type** | **List[str]** | session resource type. In case it is empty, all resources type will be returned. options: [mysql, k8s, ssh, mongodb, mssql, postgres, aws, eks, gke, rdp] | [optional] 
**status_type** | **List[str]** | session status type. In case it is empty, only active sessions will be returned. options: [connecting, connected, failed, completed, terminated] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_sra_sessions import ListSRASessions

# TODO update the JSON string below
json = "{}"
# create an instance of ListSRASessions from a JSON string
list_sra_sessions_instance = ListSRASessions.from_json(json)
# print the JSON string representation of the object
print(ListSRASessions.to_json())

# convert the object into a dict
list_sra_sessions_dict = list_sra_sessions_instance.to_dict()
# create an instance of ListSRASessions from a dict
list_sra_sessions_from_dict = ListSRASessions.from_dict(list_sra_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


