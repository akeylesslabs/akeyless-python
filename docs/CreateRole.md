# CreateRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_access** | **str** | Allow this role to view analytics. Currently only &#39;none&#39;, &#39;own&#39;, &#39;all&#39; values are supported, allowing associated auth methods to view reports produced by the same auth methods. | [optional] 
**audit_access** | **str** | Allow this role to view audit logs. Currently only &#39;none&#39;, &#39;own&#39; and &#39;all&#39; values are supported, allowing associated auth methods to view audit logs produced by the same auth methods. | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**event_center_access** | **str** | Allow this role to view Event Center. Currently only &#39;none&#39;, &#39;own&#39; and &#39;all&#39; values are supported | [optional] 
**event_forwarders_access** | **str** | Allow this role to manage Event Forwarders. Currently only &#39;none&#39; and &#39;all&#39; values are supported. | [optional] 
**gw_analytics_access** | **str** | Allow this role to view gw analytics. Currently only &#39;none&#39;, &#39;own&#39;, &#39;all&#39; values are supported, allowing associated auth methods to view reports produced by the same auth methods. | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Role name | 
**sra_reports_access** | **str** | Allow this role to view SRA Clusters. Currently only &#39;none&#39;, &#39;own&#39;, &#39;all&#39; values are supported. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usage_reports_access** | **str** | Allow this role to view Usage Report. Currently only &#39;none&#39; and &#39;all&#39; values are supported. | [optional] 

## Example

```python
from akeyless.models.create_role import CreateRole

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRole from a JSON string
create_role_instance = CreateRole.from_json(json)
# print the JSON string representation of the object
print(CreateRole.to_json())

# convert the object into a dict
create_role_dict = create_role_instance.to_dict()
# create an instance of CreateRole from a dict
create_role_from_dict = CreateRole.from_dict(create_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


