# AccountCustomFieldCreate

accountCustomFieldCreate is a command that creates a new custom field in the account settings
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | The name of the custom field | 
**object** | **str** | The object to create the custom field | [default to 'ITEM']
**object_type** | **str** | The object type to create the custom field [e.g. STATIC_SECRET,DYNAMIC_SECRET,ROTATED_SECRET] | 
**required** | **bool** | Specify whether the custom field is mandatory | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


