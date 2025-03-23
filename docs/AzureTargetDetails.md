# AzureTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_resource_group_name** | **str** |  | [optional] 
**azure_resource_name** | **str** |  | [optional] 
**azure_subscription_id** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 
**azure_username** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.azure_target_details import AzureTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetDetails from a JSON string
azure_target_details_instance = AzureTargetDetails.from_json(json)
# print the JSON string representation of the object
print(AzureTargetDetails.to_json())

# convert the object into a dict
azure_target_details_dict = azure_target_details_instance.to_dict()
# create an instance of AzureTargetDetails from a dict
azure_target_details_from_dict = AzureTargetDetails.from_dict(azure_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


