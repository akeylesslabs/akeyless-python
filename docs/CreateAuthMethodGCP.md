# CreateAuthMethodGCP

createAuthMethodGCP is a command that creates a new auth method that will be able to authenticate using GCP IAM Service Account credentials or GCE instance credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience to verify in the JWT received by the client | [optional] [default to 'akeyless.io']
**bound_ips** | **list[str]** | A CIDR whitelist of the IPs that the access is restricted to | [optional] 
**bound_labels** | **list[str]** | A comma-separated list of GCP labels formatted as \&quot;key:value\&quot; strings that must be set on authorized GCE instances. TODO: Because GCP labels are not currently ACL&#39;d .... | [optional] 
**bound_projects** | **list[str]** | &#x3D;&#x3D;&#x3D; Human and Machine authentication section &#x3D;&#x3D;&#x3D; Array of GCP project IDs. Only entities belonging to any of the provided projects can authenticate. | [optional] 
**bound_regions** | **list[str]** | List of regions that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored. | [optional] 
**bound_service_accounts** | **list[str]** | &#x3D;&#x3D;&#x3D; Human authentication section &#x3D;&#x3D;&#x3D; List of service accounts the service account must be part of in order to be authenticated. | [optional] 
**bound_zones** | **list[str]** | &#x3D;&#x3D;&#x3D; Machine authentication section &#x3D;&#x3D;&#x3D; List of zones that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone. | [optional] 
**name** | **str** | Auth Method name | 
**service_account_data** | **str** | ServiceAccount credentials data instead of giving a file path, base64 encoded | [optional] 
**service_account_file** | **str** | ServiceAccount credentials file path to be used by Akeyless to validate IAM (Human) and GCE (Machine) logins with GCP | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Type of the GCP Access Rules | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


