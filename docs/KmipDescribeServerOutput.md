# KmipDescribeServerOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**ca_cert** | **List[int]** |  | [optional] 
**certificate_issue_date** | **datetime** |  | [optional] 
**certificate_ttl_in_seconds** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**root** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_describe_server_output import KmipDescribeServerOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipDescribeServerOutput from a JSON string
kmip_describe_server_output_instance = KmipDescribeServerOutput.from_json(json)
# print the JSON string representation of the object
print(KmipDescribeServerOutput.to_json())

# convert the object into a dict
kmip_describe_server_output_dict = kmip_describe_server_output_instance.to_dict()
# create an instance of KmipDescribeServerOutput from a dict
kmip_describe_server_output_from_dict = KmipDescribeServerOutput.from_dict(kmip_describe_server_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


