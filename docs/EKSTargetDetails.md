# EKSTargetDetails

EKSTargetDetails defines details related to connecting to a EKS (Elastic Container Service) target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eks_access_key_id** | **str** |  | [optional] 
**eks_cluster_ca_certificate** | **str** |  | [optional] 
**eks_cluster_endpoint** | **str** |  | [optional] 
**eks_cluster_name** | **str** |  | [optional] 
**eks_region** | **str** |  | [optional] 
**eks_secret_access_key** | **str** |  | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.eks_target_details import EKSTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EKSTargetDetails from a JSON string
eks_target_details_instance = EKSTargetDetails.from_json(json)
# print the JSON string representation of the object
print(EKSTargetDetails.to_json())

# convert the object into a dict
eks_target_details_dict = eks_target_details_instance.to_dict()
# create an instance of EKSTargetDetails from a dict
eks_target_details_from_dict = EKSTargetDetails.from_dict(eks_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


