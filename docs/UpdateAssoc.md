# UpdateAssoc

updateAssoc is a command that updates the sub-claims of an association between role and auth method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** | The association id to be updated | 
**case_sensitive** | **str** | Treat sub claims as case-sensitive [true/false] | [optional] [default to 'true']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**sub_claims** | **dict(str, str)** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


