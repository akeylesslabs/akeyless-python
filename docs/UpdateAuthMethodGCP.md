# UpdateAuthMethodGCP

updateAuthMethodGCP is a command that updates a new auth method that will be able to authenticate using GCP IAM Service Account credentials or GCE instance credentials. [Deprecated: Use auth-method-update-gcp command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience to verify in the JWT received by the client | [default to 'akeyless.io']
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_labels** | **List[str]** | A comma-separated list of GCP labels formatted as \&quot;key:value\&quot; strings that must be set on authorized GCE instances. TODO: Because GCP labels are not currently ACL&#39;d .... | [optional] 
**bound_projects** | **List[str]** | &#x3D;&#x3D;&#x3D; Human and Machine authentication section &#x3D;&#x3D;&#x3D; Array of GCP project IDs. Only entities belonging to any of the provided projects can authenticate. | [optional] 
**bound_regions** | **List[str]** | List of regions that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored. | [optional] 
**bound_service_accounts** | **List[str]** | List of service accounts the service account must be part of in order to be authenticated. | [optional] 
**bound_zones** | **List[str]** | &#x3D;&#x3D;&#x3D; Machine authentication section &#x3D;&#x3D;&#x3D; List of zones that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone. | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**service_account_creds_data** | **str** | ServiceAccount credentials data instead of giving a file path, base64 encoded | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Type of the GCP Access Rules | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value which is a \&quot;sub claim\&quot; name that contains details uniquely identifying that resource. This \&quot;sub claim\&quot; is used to distinguish between different identities. | [optional] 

## Example

```python
from akeyless.models.update_auth_method_gcp import UpdateAuthMethodGCP

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthMethodGCP from a JSON string
update_auth_method_gcp_instance = UpdateAuthMethodGCP.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthMethodGCP.to_json())

# convert the object into a dict
update_auth_method_gcp_dict = update_auth_method_gcp_instance.to_dict()
# create an instance of UpdateAuthMethodGCP from a dict
update_auth_method_gcp_from_dict = UpdateAuthMethodGCP.from_dict(update_auth_method_gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


