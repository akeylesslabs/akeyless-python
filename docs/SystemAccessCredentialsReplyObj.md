# SystemAccessCredentialsReplyObj

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**auth_creds** | **str** | Temporary credentials for accessing Auth | [optional] 
**csrf_token** | **str** | CSRF token for synchronizer-token pattern (only populated for WebUI clients) | [optional] 
**expiry** | **int** | Credentials expiration date | [optional] 
**kfm_creds** | **str** | Temporary credentials for accessing the KFMs instances | [optional] 
**need_mfa_app_first_config** | **bool** | If the user didn&#39;t complete to configure the MFA app | [optional] 
**recovery_key_id** | **str** | RecoveryKeyID identifies the DPoP-bound recovery key for WebUI session recovery. | [optional] 
**required_mfa** | **str** |  | [optional] 
**sub_claims** | **dict(str, list[str])** | SubClaims carries the IdP-verified RBAC claims for offline placeholder creds (empty UAM JWT); parsed from the ID token at callback time. | [optional] 
**token** | **str** | Credentials tmp token | [optional] 
**uam_creds** | **str** | Temporary credentials for accessing the UAM service | [optional] 
**unique_id** | **str** | UniqueId is set only on Gateway-minted offline placeholder creds (empty UAM JWT), carrying the IdP unique identifier so usage-time RBAC can resolve identity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


