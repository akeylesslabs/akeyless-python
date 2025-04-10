# SSHCertificateIssueDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_domains** | **list[str]** | Relevant for host certificate | [optional] 
**allowed_user_key_lengths** | **dict(str, int)** |  | [optional] 
**allowed_users** | **list[str]** | Relevant for user certificate | [optional] 
**cert_type** | **int** |  | [optional] 
**critical_options** | **dict(str, str)** |  | [optional] 
**extensions** | **dict(str, str)** |  | [optional] 
**externally_provided_user_sub_claim_key** | **str** | ExternallyProvidedUserSubClaimKey is the claim key name where the user name should be taken from | [optional] 
**is_externally_provided_user** | **bool** | IsExternallyProvidedUser is true if allow users should be taken from claims and not from AllowedUsers | [optional] 
**principals** | **list[str]** |  | [optional] 
**static_key_id** | **str** | In case it is empty, the key ID will be combination of user identifiers and a random string | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


