# AwsStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | creds | [optional] 
**access_key_secret** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from akeyless.models.aws_storage import AwsStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AwsStorage from a JSON string
aws_storage_instance = AwsStorage.from_json(json)
# print the JSON string representation of the object
print(AwsStorage.to_json())

# convert the object into a dict
aws_storage_dict = aws_storage_instance.to_dict()
# create an instance of AwsStorage from a dict
aws_storage_from_dict = AwsStorage.from_dict(aws_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


