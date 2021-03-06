# CreateAuthMethodAWSIAM

createAuthMethodAWSIAM is a command that creates a new Auth Method that will be able to authenticate using AWS IAM credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**bound_arn** | **list[str]** | A list of full arns that the access is restricted to | [optional] 
**bound_aws_account_id** | **list[str]** | A list of AWS account-IDs that the access is restricted to | 
**bound_ips** | **list[str]** | A CIDR whitelist of the IPs that the access is restricted to | [optional] 
**bound_resource_id** | **list[str]** | A list of full resource ids that the access is restricted to | [optional] 
**bound_role_id** | **list[str]** | A list of full role ids that the access is restricted to | [optional] 
**bound_role_name** | **list[str]** | A list of full role-name that the access is restricted to | [optional] 
**bound_user_id** | **list[str]** | A list of full user ids that the access is restricted to | [optional] 
**bound_user_name** | **list[str]** | A list of full user-name that the access is restricted to | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**name** | **str** | Auth Method name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**sts_url** | **str** | sts URL | [optional] [default to 'https://sts.amazonaws.com']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


