# K8SAuthsConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_auths** | [**List[K8SAuth]**](K8SAuth.md) |  | [optional] 

## Example

```python
from akeyless.models.k8_s_auths_config_part import K8SAuthsConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of K8SAuthsConfigPart from a JSON string
k8_s_auths_config_part_instance = K8SAuthsConfigPart.from_json(json)
# print the JSON string representation of the object
print(K8SAuthsConfigPart.to_json())

# convert the object into a dict
k8_s_auths_config_part_dict = k8_s_auths_config_part_instance.to_dict()
# create an instance of K8SAuthsConfigPart from a dict
k8_s_auths_config_part_from_dict = K8SAuthsConfigPart.from_dict(k8_s_auths_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


