# AssocRoleAuthMethod

assocRoleAuthMethod is a command that creates an association between role and auth method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**am_name** | **str** | The auth method to associate | 
**case_sensitive** | **str** |  | [optional] 
**role_name** | **str** | The role to associate | 
**sub_claims** | **dict(str, str)** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


