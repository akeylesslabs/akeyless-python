# RollbackSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Secret name | 
**old_version** | **int** | Old secret version to rollback to | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rollback_secret import RollbackSecret

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSecret from a JSON string
rollback_secret_instance = RollbackSecret.from_json(json)
# print the JSON string representation of the object
print(RollbackSecret.to_json())

# convert the object into a dict
rollback_secret_dict = rollback_secret_instance.to_dict()
# create an instance of RollbackSecret from a dict
rollback_secret_from_dict = RollbackSecret.from_dict(rollback_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


