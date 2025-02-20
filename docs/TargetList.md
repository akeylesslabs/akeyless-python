# TargetList

targetList is a command that returns a list of targets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter by auth method name or part of it | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**pagination_token** | **str** | Next page reference | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **List[str]** | The target types list . In case it is empty, all types of targets will be returned. options: [hanadb cassandra aws ssh gke eks mysql mongodb snowflake mssql redshift artifactory azure rabbitmq k8s venafi gcp oracle dockerhub ldap github chef web salesforce postgres] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_list import TargetList

# TODO update the JSON string below
json = "{}"
# create an instance of TargetList from a JSON string
target_list_instance = TargetList.from_json(json)
# print the JSON string representation of the object
print(TargetList.to_json())

# convert the object into a dict
target_list_dict = target_list_instance.to_dict()
# create an instance of TargetList from a dict
target_list_from_dict = TargetList.from_dict(target_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


