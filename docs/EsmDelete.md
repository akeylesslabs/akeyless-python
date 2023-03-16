# EsmDelete

esmDelete is a command that deletes a secret from an External Secrets Manager
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esm_name** | **str** | Name of the External Secrets Manager item | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**secret_id** | **str** | The external secret id (or name, for AWS, Azure or K8s targets) to delete | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


