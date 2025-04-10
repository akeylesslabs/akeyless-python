# EsmUpdate

esmUpdate is a command that updates a secret in an External Secrets Manager
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_value** | **bool** | Use this option if the external secret value is a base64 encoded binary | [optional] 
**description** | **str** | Description of the external secret | [optional] 
**esm_name** | **str** | Name of the External Secrets Manager item | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**secret_id** | **str** | The external secret id (or name, for AWS, Azure or K8s targets) to update | 
**tags** | **dict(str, str)** | Tags for the external secret | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**value** | **str** | Value of the external secret item, either text or base64 encoded binary | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


