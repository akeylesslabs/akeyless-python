# GwClusterIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_allowed** | **bool** |  | [optional] 
**allowed** | **bool** |  | [optional] 
**allowed_access_ids** | **List[str]** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**cluster_url** | **str** |  | [optional] 
**current_gw** | **bool** |  | [optional] 
**customer_fragment_ids** | **List[str]** | Deprecated - use CustomerFragments instead | [optional] 
**customer_fragments** | [**List[CfInfo]**](CfInfo.md) |  | [optional] 
**default_protection_key_id** | **int** |  | [optional] 
**default_secret_location** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_kerberos_auth_enabled** | **bool** |  | [optional] 
**is_ldap_auth_enabled** | **bool** |  | [optional] 
**serverless_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gw_cluster_identity import GwClusterIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of GwClusterIdentity from a JSON string
gw_cluster_identity_instance = GwClusterIdentity.from_json(json)
# print the JSON string representation of the object
print(GwClusterIdentity.to_json())

# convert the object into a dict
gw_cluster_identity_dict = gw_cluster_identity_instance.to_dict()
# create an instance of GwClusterIdentity from a dict
gw_cluster_identity_from_dict = GwClusterIdentity.from_dict(gw_cluster_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


