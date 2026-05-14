# GatewayDeleteProducer

gatewayDeleteProducer is a command that deletes producer [Deprecated: Use dynamic-secret-delete command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) Mirrors commands.AgenticRulesParams — kept separate because ResourceDS cannot embed it (different package, different struct layout). | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


