# EmailError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.email_error import EmailError

# TODO update the JSON string below
json = "{}"
# create an instance of EmailError from a JSON string
email_error_instance = EmailError.from_json(json)
# print the JSON string representation of the object
print(EmailError.to_json())

# convert the object into a dict
email_error_dict = email_error_instance.to_dict()
# create an instance of EmailError from a dict
email_error_from_dict = EmailError.from_dict(email_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


