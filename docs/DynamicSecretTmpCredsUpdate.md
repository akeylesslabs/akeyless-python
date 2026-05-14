# DynamicSecretTmpCredsUpdate

dynamicSecretTmpCredsUpdate is a command that updates dynamic secret temp creds
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host | 
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) Mirrors commands.AgenticRulesParams — kept separate because ResourceDS cannot embed it (different package, different struct layout). | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_ttl_min** | **int** | New TTL in Minutes | 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**tmp_creds_id** | **str** | Tmp Creds ID | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


