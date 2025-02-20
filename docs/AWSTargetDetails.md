# AWSTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_key_id** | **str** |  | [optional] 
**aws_region** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**aws_session_token** | **str** |  | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.aws_target_details import AWSTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AWSTargetDetails from a JSON string
aws_target_details_instance = AWSTargetDetails.from_json(json)
# print the JSON string representation of the object
print(AWSTargetDetails.to_json())

# convert the object into a dict
aws_target_details_dict = aws_target_details_instance.to_dict()
# create an instance of AWSTargetDetails from a dict
aws_target_details_from_dict = AWSTargetDetails.from_dict(aws_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


