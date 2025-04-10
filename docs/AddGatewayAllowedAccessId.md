# AddGatewayAllowedAccessId

Responses:  default: errorResponse 200: addGatewayAllowedAccessIdResponse
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access id that will be able to access to gateway | 
**cluster_name** | **str** | The name of the updated cluster, e.g. acc-abcd12345678/p-123456789012/defaultCluster | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**sub_claims** | **dict(str, str)** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


