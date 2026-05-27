# GatewayCreateProducerRedis

gatewayCreateProducerRedis is a command that creates Redis producer [Deprecated: Use dynamic-secret-create-redis command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_rules** | **str** | A JSON array list of redis ACL rules to attach to the created user. For available rules see the ACL CAT command https://redis.io/commands/acl-cat By default the user will have permissions to read all keys &#39;[\&quot;~*\&quot;, \&quot;+@read\&quot;]&#39; | [optional] 
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**host** | **str** | Redis Host | [optional] [default to '127.0.0.1']
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) Mirrors commands.AgenticRulesParams — kept separate because ResourceDS cannot embed it (different package, different struct layout). | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**password** | **str** | Redis Password | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**port** | **str** | Redis Port | [optional] [default to '6379']
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**ssl_certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_capital_letters** | **str** | Specifies whether the generated temporary password must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z). [true/false] | [optional] 
**use_lower_letters** | **str** | Specifies whether the generated temporary password must contain at least one lowercase character from the ISO basic Latin alphabet (a to z). [true/false] | [optional] 
**use_numbers** | **str** | Specifies whether the generated temporary password must contain at least one numeric character (0 to 9). [true/false] | [optional] 
**use_special_characters** | **str** |  | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Redis Username | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


