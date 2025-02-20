# AwsS3LogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_id** | **str** |  | [optional] 
**aws_access_key** | **str** |  | [optional] 
**aws_auth_type** | **str** |  | [optional] 
**aws_region** | **str** |  | [optional] 
**aws_role_arn** | **str** |  | [optional] 
**aws_use_gateway_cloud_identity** | **bool** | deprecated | [optional] 
**bucket_name** | **str** |  | [optional] 
**log_folder** | **str** |  | [optional] 

## Example

```python
from akeyless.models.aws_s3_log_forwarding_config import AwsS3LogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3LogForwardingConfig from a JSON string
aws_s3_log_forwarding_config_instance = AwsS3LogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(AwsS3LogForwardingConfig.to_json())

# convert the object into a dict
aws_s3_log_forwarding_config_dict = aws_s3_log_forwarding_config_instance.to_dict()
# create an instance of AwsS3LogForwardingConfig from a dict
aws_s3_log_forwarding_config_from_dict = AwsS3LogForwardingConfig.from_dict(aws_s3_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


