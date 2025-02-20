# GKETargetDetails

GKETargetDetails defines details related to connecting to a GKE (Google Kubernetes Engine) target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gke_cluster_ca_certificate** | **str** |  | [optional] 
**gke_cluster_endpoint** | **str** |  | [optional] 
**gke_cluster_name** | **str** |  | [optional] 
**gke_service_account_key** | **str** |  | [optional] 
**gke_service_account_name** | **str** |  | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.gke_target_details import GKETargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GKETargetDetails from a JSON string
gke_target_details_instance = GKETargetDetails.from_json(json)
# print the JSON string representation of the object
print(GKETargetDetails.to_json())

# convert the object into a dict
gke_target_details_dict = gke_target_details_instance.to_dict()
# create an instance of GKETargetDetails from a dict
gke_target_details_from_dict = GKETargetDetails.from_dict(gke_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


