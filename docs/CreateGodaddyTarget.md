# CreateGodaddyTarget

createGodaddyTarget is a command that creates a new target. [Deprecated: Use target-create-godaddy command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Key of the api credentials to the Godaddy account | 
**description** | **str** | Description of the object | [optional] 
**imap_fqdn** | **str** | ImapFQDN of the IMAP service, FQDN or IPv4 address. Must be FQDN if the IMAP is using TLS | 
**imap_password** | **str** | ImapPassword to access the IMAP service | 
**imap_port** | **str** | ImapPort of the IMAP service | [optional] [default to '993']
**imap_username** | **str** | ImapUsername to access the IMAP service | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**secret** | **str** | Secret of the api credentials to the Godaddy account | 
**timeout** | **str** | Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h. | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_godaddy_target import CreateGodaddyTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGodaddyTarget from a JSON string
create_godaddy_target_instance = CreateGodaddyTarget.from_json(json)
# print the JSON string representation of the object
print(CreateGodaddyTarget.to_json())

# convert the object into a dict
create_godaddy_target_dict = create_godaddy_target_instance.to_dict()
# create an instance of CreateGodaddyTarget from a dict
create_godaddy_target_from_dict = CreateGodaddyTarget.from_dict(create_godaddy_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


