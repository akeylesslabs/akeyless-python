# SAMLAccessRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_ur_is** | **list[str]** | Allowed redirect URIs after the authentication | [optional] 
**bound_attributes** | [**list[SAMLAttribute]**](SAMLAttribute.md) | The attributes that login is restricted to. | [optional] 
**idp_metadata_url** | **str** | IDP metadata url | [optional] 
**idp_metadata_xml** | **str** | IDP metadata XML | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 
**use_dedicated_saml_urls** | **bool** | When true, the login AuthnRequest is signed with this access method&#39;s dedicated SP identity (Entity ID https://&lt;sp&gt;/saml/sp/{access_id} and ACS https://&lt;sp&gt;/saml/acs/{access_id}) instead of the shared global identity. Default false keeps the legacy global identity for backward compatibility. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


