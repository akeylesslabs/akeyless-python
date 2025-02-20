# APIKeyAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**key** | **str** | The public key value of the API-key. | [optional] 
**modification_date** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.api_key_access_rules import APIKeyAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyAccessRules from a JSON string
api_key_access_rules_instance = APIKeyAccessRules.from_json(json)
# print the JSON string representation of the object
print(APIKeyAccessRules.to_json())

# convert the object into a dict
api_key_access_rules_dict = api_key_access_rules_instance.to_dict()
# create an instance of APIKeyAccessRules from a dict
api_key_access_rules_from_dict = APIKeyAccessRules.from_dict(api_key_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


