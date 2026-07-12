# UpdateMcpSecretOAuthAuthCode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** |  | [optional] 
**last_version** | **int** |  | [optional] 
**name** | **str** | Secret name | 
**oauth_client_id** | **str** | OAuth client ID | [optional] 
**oauth_client_secret** | **str** | OAuth client secret | [optional] 
**oauth_redirect_uri** | **str** | OAuth redirect URI | [optional] 
**oauth_refresh_token** | **str** | OAuth refresh token | [optional] 
**oauth_scopes** | **list[str]** | OAuth scopes | [optional] 
**oauth_token_url** | **str** | OAuth token URL | [optional] 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**url** | **str** | URL of the service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


