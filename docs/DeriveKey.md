# DeriveKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**alg** | **str** | Kdf algorithm | [default to 'pbkdf2']
**hash_function** | **str** | HashFunction the hash function to use (relevant for pbkdf2) | [optional] [default to 'sha256']
**iter** | **int** | IterationCount the number of iterations | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_len** | **int** | KeyLength the byte length of the generated key | 
**mem** | **int** | MemorySizeInKb the memory paramter in kb (relevant for argon2id) | [optional] [default to 16384]
**name** | **str** | Static Secret full name | 
**parallelism** | **int** | Parallelism the number of threads to use (relevant for argon2id) | [optional] [default to 1]
**salt** | **str** | Salt Base64 encoded salt value. If not provided, the salt will be generated as part of the operation. The salt should be securely-generated random bytes, minimum 64 bits, 128 bits is recommended | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


