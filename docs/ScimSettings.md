# ScimSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_access_id** | **str** | Access ID of the API Key auth method the IdP uses as the SCIM bearer. | [optional] 
**default_identity_type** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**gateway_url** | **str** | URL of the gateway that serves the SCIM endpoint to the IdP, for the private endpoint. | [optional] 
**provisioned_access_id** | **str** | ProvisionedAccessId and ProvisionedType are set on the bearer itself, not on the auth method it provisions. They point back to the SAML or OIDC auth method the bearer provisions, so the gateway can find that auth method from the bearer. | [optional] 
**provisioned_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


