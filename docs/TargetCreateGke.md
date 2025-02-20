# TargetCreateGke


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**gke_account_key** | **str** | GKE Service Account key file path | [optional] 
**gke_cluster_cert** | **str** | GKE cluster CA certificate | [optional] 
**gke_cluster_endpoint** | **str** | GKE cluster URL endpoint | [optional] 
**gke_cluster_name** | **str** | GKE cluster name | [optional] 
**gke_service_account_email** | **str** | GKE service account email | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.target_create_gke import TargetCreateGke

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateGke from a JSON string
target_create_gke_instance = TargetCreateGke.from_json(json)
# print the JSON string representation of the object
print(TargetCreateGke.to_json())

# convert the object into a dict
target_create_gke_dict = target_create_gke_instance.to_dict()
# create an instance of TargetCreateGke from a dict
target_create_gke_from_dict = TargetCreateGke.from_dict(target_create_gke_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


