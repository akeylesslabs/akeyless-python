# ShareItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**action** | **str** | Action to be performed on the item [start/stop/describe] | 
**emails** | **List[str]** | List of emails to start/stop sharing the secret with | [optional] 
**item_name** | **str** | Item name | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**share_type** | **str** | Share type [email/token] | [optional] [default to 'email']
**shared_token_id** | **List[str]** | Shared token ids in order to stop sharing a secret | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | TTL of the Availability of the shared secret in seconds | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**view_once** | **bool** | ViewOnlyOnce Shared secrets can only be viewed once [true/false] | [optional] [default to False]

## Example

```python
from akeyless.models.share_item import ShareItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShareItem from a JSON string
share_item_instance = ShareItem.from_json(json)
# print the JSON string representation of the object
print(ShareItem.to_json())

# convert the object into a dict
share_item_dict = share_item_instance.to_dict()
# create an instance of ShareItem from a dict
share_item_from_dict = ShareItem.from_dict(share_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


