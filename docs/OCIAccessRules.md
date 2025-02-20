# OCIAccessRules

OCIAccessRules contains access rules specific to Oracle cloud instance / user authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ocids** | **List[str]** |  | [optional] 
**tenant_ocid** | **str** |  | [optional] 

## Example

```python
from akeyless.models.oci_access_rules import OCIAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of OCIAccessRules from a JSON string
oci_access_rules_instance = OCIAccessRules.from_json(json)
# print the JSON string representation of the object
print(OCIAccessRules.to_json())

# convert the object into a dict
oci_access_rules_dict = oci_access_rules_instance.to_dict()
# create an instance of OCIAccessRules from a dict
oci_access_rules_from_dict = OCIAccessRules.from_dict(oci_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


