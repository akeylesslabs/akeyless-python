# ValidateCertificateChallenge

ValidateCertificateChallenge validates HTTP-01 challenge and finalizes certificate issuance (Phase 2)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ValidateCertificateChallengeOutput**](ValidateCertificateChallengeOutput.md) |  | [optional] 
**cert_display_id** | **str** | Certificate display ID from Phase 1 | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate name (alternative to cert-display-id) | [optional] 
**timeout** | **int** | Validation timeout in seconds | [optional] [default to 120]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


