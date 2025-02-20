# TargetUpdateSectigo

targetUpdateSectigo is a command that updates an existing Sectigo target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_profile_id** | **int** | Certificate Profile ID in Sectigo account | 
**customer_uri** | **str** | Customer Uri of the Sectigo account | 
**description** | **str** | Description of the object | [optional] 
**external_requester** | **str** | External Requester - a comma separated list of emails | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**organization_id** | **int** | Organization ID in Sectigo account | 
**password** | **str** | Password of the Sectigo account user | 
**timeout** | **str** | Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h. | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Username of the Sectigo account | 

## Example

```python
from akeyless.models.target_update_sectigo import TargetUpdateSectigo

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateSectigo from a JSON string
target_update_sectigo_instance = TargetUpdateSectigo.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateSectigo.to_json())

# convert the object into a dict
target_update_sectigo_dict = target_update_sectigo_instance.to_dict()
# create an instance of TargetUpdateSectigo from a dict
target_update_sectigo_from_dict = TargetUpdateSectigo.from_dict(target_update_sectigo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


