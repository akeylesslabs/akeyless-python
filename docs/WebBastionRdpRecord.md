# WebBastionRdpRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**AwsStorage**](AwsStorage.md) |  | [optional] 
**azure** | [**AzureStorage**](AzureStorage.md) |  | [optional] 
**storage_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.web_bastion_rdp_record import WebBastionRdpRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WebBastionRdpRecord from a JSON string
web_bastion_rdp_record_instance = WebBastionRdpRecord.from_json(json)
# print the JSON string representation of the object
print(WebBastionRdpRecord.to_json())

# convert the object into a dict
web_bastion_rdp_record_dict = web_bastion_rdp_record_instance.to_dict()
# create an instance of WebBastionRdpRecord from a dict
web_bastion_rdp_record_from_dict = WebBastionRdpRecord.from_dict(web_bastion_rdp_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


