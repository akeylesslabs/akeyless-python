# UpdateAuthMethodAWSIAM

updateAuthMethodAWSIAM is a command that updates a new Auth Method that will be able to authenticate using AWS IAM credentials. [Deprecated: Use auth-method-update-aws-iam command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_arn** | **list[str]** | A list of full arns that the access is restricted to | [optional] 
**bound_aws_account_id** | **list[str]** | A list of AWS account-IDs that the access is restricted to | 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_resource_id** | **list[str]** | A list of full resource ids that the access is restricted to | [optional] 
**bound_role_id** | **list[str]** | A list of full role ids that the access is restricted to | [optional] 
**bound_role_name** | **list[str]** | A list of full role-name that the access is restricted to | [optional] 
**bound_user_id** | **list[str]** | A list of full user ids that the access is restricted to | [optional] 
**bound_user_name** | **list[str]** | A list of full user-name that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **list[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**sts_url** | **str** | sts URL | [optional] [default to 'https://sts.amazonaws.com']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value which is a \&quot;sub claim\&quot; name that contains details uniquely identifying that resource. This \&quot;sub claim\&quot; is used to distinguish between different identities. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


