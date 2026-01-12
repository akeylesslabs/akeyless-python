# CreateRole

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_access** | **str** | Allow this role to view analytics. Currently only &#39;none&#39;, &#39;own&#39;, &#39;all&#39; values are supported, allowing associated auth methods to view reports produced by the same auth methods. | [optional] 
**audit_access** | **str** | Allow this role to view audit logs. Currently only &#39;none&#39;, &#39;own&#39;, &#39;scoped&#39; and &#39;all&#39; values are supported, allowing associated auth methods to view audit logs produced by the same auth methods. | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**event_center_access** | **str** | Allow this role to view Event Center. Currently only &#39;none&#39;, &#39;scoped&#39; and &#39;all&#39; values are supported | [optional] 
**event_forwarders_access** | **str** | Allow this role to manage Event Forwarders. Currently only &#39;none&#39; and &#39;all&#39; values are supported. | [optional] 
**event_forwarders_name** | **list[str]** | Allow this role to manage the following Event Forwarders. | [optional] 
**gw_analytics_access** | **str** | Allow this role to view gw analytics. Currently only &#39;none&#39;, &#39;scoped&#39;, &#39;all&#39; values are supported, allowing associated auth methods to view reports produced by the same auth methods. | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Role name | 
**reverse_rbac_access** | **str** | Allow this role to view Reverse RBAC. Supported values: &#39;scoped&#39;, &#39;all&#39;. | [optional] 
**sra_reports_access** | **str** | Allow this role to view SRA Clusters. Currently only &#39;none&#39;, &#39;scoped&#39;, &#39;all&#39; values are supported. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usage_reports_access** | **str** | Allow this role to view Usage Report. Currently only &#39;none&#39; and &#39;all&#39; values are supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


