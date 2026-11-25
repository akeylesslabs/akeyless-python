# DynamicSecretUpdateAliCloud

dynamicSecretUpdateAliCloud is a command that updates AliCloud dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alicloud_access_key_id** | **str** | AliCloud RAM access key ID | [optional] 
**alicloud_access_mode** | **str** |  | [optional] 
**alicloud_access_secret_key** | **str** | AliCloud RAM access key secret | [optional] 
**alicloud_external_id** | **str** | The external ID in the trust policy of the AliCloud roles (relevant only for assume_role mode) | [optional] 
**alicloud_region** | **str** | AliCloud region. Selects the regional STS endpoint. If empty, the global STS endpoint is used | [optional] 
**alicloud_role_arns** | **str** | AliCloud role ARNs allowed in the Assume Role operation (relevant only for assume_role mode) | [optional] 
**alicloud_session_policy** | **str** | Session policy document (JSON) that limits the assumed role session (relevant only for assume_role mode) | [optional] 
**alicloud_set_source_identity** | **bool** | Send the requester&#39;s identity as the SourceIdentity of the assumed role session, so it shows in ActionTrail (relevant only for assume_role mode). Needs sts:SetSourceIdentity in both the producer identity&#39;s policy and the role trust policy | [optional] [default to False]
**alicloud_site** | **str** | The Alibaba Cloud site of the account: international or china. It selects the console sign-in host of the RAM user | [optional] [default to 'international']
**alicloud_user_console_access** | **bool** | Enable AliCloud RAM user console access (relevant only for ram_user mode) | [optional] [default to False]
**alicloud_user_groups** | **str** | AliCloud user groups (relevant only for ram_user mode) | [optional] 
**alicloud_user_inline_policy** | **str** | RAM policy document (JSON) for a custom policy created for each RAM user (relevant only for ram_user mode) | [optional] 
**alicloud_user_policies** | **str** | AliCloud policies attached to the RAM user, in the form &lt;System|Custom&gt;:&lt;PolicyName&gt; (relevant only for ram_user mode) | [optional] 
**alicloud_user_programmatic_access** | **bool** | Enable AliCloud RAM user programmatic access (relevant only for ram_user mode) | [optional] [default to True]
**ara_enabled** | **bool** | Enable or disable Agentic Runtime Authority rule enforcement for this item. Mirrors commands.AgenticRulesParams.AraEnabled. | [optional] 
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**enable_agentic_runtime_authority** | **bool** | EnableAra is the documented spelling of AraEnabled; --ara-enabled shipped first and stays as an undocumented alias. | [optional] 
**enable_ai_quorum** | **bool** | Turns on AI Quorum checks for this item. | [optional] 
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) Mirrors commands.AgenticRulesParams — kept separate because ResourceDS cannot embed it (different package, different struct layout). | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**skip_dry_run** | **bool** | If set, dry-run will be skipped [true/false] | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_capital_letters** | **str** | Specifies whether the generated temporary password must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z). [true/false] | [optional] 
**use_lower_letters** | **str** | Specifies whether the generated temporary password must contain at least one lowercase character from the ISO basic Latin alphabet (a to z). [true/false] | [optional] 
**use_numbers** | **str** | Specifies whether the generated temporary password must contain at least one numeric character (0 to 9). [true/false] | [optional] 
**use_special_characters** | **str** |  | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


