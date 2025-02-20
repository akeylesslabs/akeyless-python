# TargetUpdateGodaddy


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
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**secret** | **str** | Secret of the api credentials to the Godaddy account | 
**timeout** | **str** | Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h. | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_update_godaddy import TargetUpdateGodaddy

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateGodaddy from a JSON string
target_update_godaddy_instance = TargetUpdateGodaddy.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateGodaddy.to_json())

# convert the object into a dict
target_update_godaddy_dict = target_update_godaddy_instance.to_dict()
# create an instance of TargetUpdateGodaddy from a dict
target_update_godaddy_from_dict = TargetUpdateGodaddy.from_dict(target_update_godaddy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


