# UpdateAuthMethodCert

updateAuthMethodCert is a command that updates a new auth method that will be able to authenticate using a client certificate. [Deprecated: Use auth-method-update-cert command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_client_type** | **list[str]** |  | [optional] 
**allowed_cors** | **str** | Comma separated list of allowed CORS domains to be validated as part of the authentication flow. | [optional] 
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_common_names** | **list[str]** | A list of names. At least one must exist in the Common Name. Supports globbing. | [optional] 
**bound_dns_sans** | **list[str]** | A list of DNS names. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_email_sans** | **list[str]** | A list of Email Addresses. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_extensions** | **list[str]** | A list of extensions formatted as \&quot;oid:value\&quot;. Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \&quot;value\&quot;. | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_organizational_units** | **list[str]** | A list of Organizational Units names. At least one must exist in the OU field. | [optional] 
**bound_uri_sans** | **list[str]** | A list of URIs. At least one must exist in the SANs. Supports globbing. | [optional] 
**certificate_data** | **str** | The certificate data in base64, if no file was provided | [optional] 
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
**revoked_cert_ids** | **list[str]** | A list of revoked cert ids | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured, such as common_name or organizational_unit Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


