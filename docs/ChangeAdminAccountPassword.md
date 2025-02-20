# ChangeAdminAccountPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Current password | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**new_password** | **str** | New password | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.change_admin_account_password import ChangeAdminAccountPassword

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAdminAccountPassword from a JSON string
change_admin_account_password_instance = ChangeAdminAccountPassword.from_json(json)
# print the JSON string representation of the object
print(ChangeAdminAccountPassword.to_json())

# convert the object into a dict
change_admin_account_password_dict = change_admin_account_password_instance.to_dict()
# create an instance of ChangeAdminAccountPassword from a dict
change_admin_account_password_from_dict = ChangeAdminAccountPassword.from_dict(change_admin_account_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


