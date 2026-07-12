# CreateMcpSecretBearerToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**bearer_token** | **str** | Bearer token value | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Secret name | 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**protection_key** | **str** |  | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**url** | **str** | URL of the service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


