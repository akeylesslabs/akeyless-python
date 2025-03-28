# TargetUpdateEks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**eks_access_key_id** | **str** | Access Key ID | 
**eks_cluster_ca_cert** | **str** | EKS cluster CA certificate | 
**eks_cluster_endpoint** | **str** | EKS cluster URL endpoint | 
**eks_cluster_name** | **str** | EKS cluster name | 
**eks_region** | **str** | Region | [optional] [default to 'us-east-2']
**eks_secret_access_key** | **str** | Secret Access Key | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.target_update_eks import TargetUpdateEks

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateEks from a JSON string
target_update_eks_instance = TargetUpdateEks.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateEks.to_json())

# convert the object into a dict
target_update_eks_dict = target_update_eks_instance.to_dict()
# create an instance of TargetUpdateEks from a dict
target_update_eks_from_dict = TargetUpdateEks.from_dict(target_update_eks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


