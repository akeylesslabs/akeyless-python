# RevokeCertificate

RevokeCertificate is a command that revokes a certificate and adds it to the crl
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | The item id of the certificate to revoke | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate item name to revoke | [optional] 
**serial_number** | **str** | The serial number of the certificate to revoke | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Certificate version to revoke. Required if item-id or name are used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


