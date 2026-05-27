# GatewayCreateProducerSnowflake

GatewayCreateProducerSnowflakeCmd is a command that creates a Snowflake producer [Deprecated: Use dynamic-secret-create-snowflake command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**account_password** | **str** | Database Password | [optional] 
**account_username** | **str** | Database Username | [optional] 
**auth_mode** | **str** | The authentication mode for the temporary user [password/key] | [optional] [default to 'password']
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**db_name** | **str** | Database name | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) Mirrors commands.AgenticRulesParams — kept separate because ResourceDS cannot embed it (different package, different struct layout). | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_algo** | **str** |  | [optional] 
**name** | **str** | Dynamic secret name | 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**private_key** | **str** | RSA Private key (base64 encoded) | [optional] 
**private_key_passphrase** | **str** | The Private key passphrase | [optional] 
**role** | **str** | User role | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_capital_letters** | **str** | Specifies whether the generated temporary password must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z). [true/false] | [optional] 
**use_lower_letters** | **str** | Specifies whether the generated temporary password must contain at least one lowercase character from the ISO basic Latin alphabet (a to z). [true/false] | [optional] 
**use_numbers** | **str** | Specifies whether the generated temporary password must contain at least one numeric character (0 to 9). [true/false] | [optional] 
**use_special_characters** | **str** |  | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '24h']
**warehouse** | **str** | Warehouse name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


