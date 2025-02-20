# AWSPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from akeyless.models.aws_payload import AWSPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AWSPayload from a JSON string
aws_payload_instance = AWSPayload.from_json(json)
# print the JSON string representation of the object
print(AWSPayload.to_json())

# convert the object into a dict
aws_payload_dict = aws_payload_instance.to_dict()
# create an instance of AWSPayload from a dict
aws_payload_from_dict = AWSPayload.from_dict(aws_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


