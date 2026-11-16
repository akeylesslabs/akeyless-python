# ProvisionCertificateOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail_message** | **str** |  | [optional] 
**success_message** | **str** |  | [optional] 
**association_id** | **str** | AssociationID and TargetName identify the row of a Results entry. | [optional] 
**host_names** | **list[str]** |  | [optional] 
**provisioned_at** | **datetime** |  | [optional] 
**results** | [**list[ProvisionCertificateOutput]**](ProvisionCertificateOutput.md) | Results holds one entry per row. It is set only when several rows were handled; the top-level fields then summarize them. | [optional] 
**target_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


