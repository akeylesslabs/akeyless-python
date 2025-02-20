# EmailEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_email** | **str** |  | [optional] 
**to_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.email_entry import EmailEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EmailEntry from a JSON string
email_entry_instance = EmailEntry.from_json(json)
# print the JSON string representation of the object
print(EmailEntry.to_json())

# convert the object into a dict
email_entry_dict = email_entry_instance.to_dict()
# create an instance of EmailEntry from a dict
email_entry_from_dict = EmailEntry.from_dict(email_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


