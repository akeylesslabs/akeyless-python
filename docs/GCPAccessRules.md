# GCPAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | The audience in the JWT | [optional] [default to 'akeyless.io']
**bound_labels** | **Dict[str, str]** | A map of GCP labels formatted as \&quot;key:value\&quot; strings that must be set on authorized GCE instances. TODO: Because GCP labels are not currently ACL&#39;d .... | [optional] 
**bound_projects** | **List[str]** | Human and Machine authentication section Array of GCP project IDs. Only entities belonging to any of the provided projects can authenticate. | [optional] 
**bound_regions** | **List[str]** | List of regions that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored. | [optional] 
**bound_service_accounts** | **List[str]** | List of service accounts the service account must be part of in order to be authenticated | [optional] 
**bound_zones** | **List[str]** | &#x3D;&#x3D;&#x3D; Machine authentication section &#x3D;&#x3D;&#x3D; List of zones that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone. | [optional] 
**service_account** | **str** | ServiceAccount holds the credentials file contents to be used by Akeyless to validate IAM (Human) and GCE (Machine) logins against GCP base64 encoded string | [optional] 
**type** | **str** |  | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.gcp_access_rules import GCPAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of GCPAccessRules from a JSON string
gcp_access_rules_instance = GCPAccessRules.from_json(json)
# print the JSON string representation of the object
print(GCPAccessRules.to_json())

# convert the object into a dict
gcp_access_rules_dict = gcp_access_rules_instance.to_dict()
# create an instance of GCPAccessRules from a dict
gcp_access_rules_from_dict = GCPAccessRules.from_dict(gcp_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


