
## az dataprotection backup-instance show ##

 Gets a backup instance with name in a backup vault.
### Parameters ###
  - --resource-group -g
  - --vault-name
  - --backup-instance-name --name -n
  - --ids

### Examples ###

#### Get a backup instance by name ####
Command
```
az dataprotection backup-instance show -g sarath-rg --vault-name sarath-vault -n sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056
```
Output
```json
{
  "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056",
  "name": "sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056",
  "properties": {
    "currentProtectionState": "ProtectionConfigured",
    "dataSourceInfo": {
      "datasourceType": "Microsoft.Storage/storageAccounts/blobServices",
      "objectType": "Datasource",
      "resourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathblobtestsa",
      "resourceLocation": "centraluseuap",
      "resourceName": "sarathblobtestsa",
      "resourceType": "Microsoft.Storage/storageAccounts",
      "resourceUri": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathblobtestsa"
    },
    "dataSourceSetInfo": null,
    "friendlyName": "sarathblobtestsa",
    "objectType": "BackupInstance",
    "policyInfo": {
      "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/blobpolicy",
      "policyParameters": {
        "dataStoreParametersList": [
          {
            "dataStoreType": "OperationalStore",
            "objectType": "AzureOperationalStoreParameters",
            "resourceGroupId": ""
          }
        ]
      },
      "policyVersion": ""
    },
    "protectionErrorDetails": null,
    "protectionStatus": {
      "errorDetails": null,
      "status": "ProtectionConfigured"
    },
    "provisioningState": "Succeeded"
  },
  "resourceGroup": "sarath-rg",
  "systemData": null,
  "type": "Microsoft.DataProtection/backupVaults/backupInstances"
}
```

#### Get backup instance by Id ####
Command
```
az dataprotection backup-instance show --ids /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056
```
Output
```
{
  "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056",
  "name": "sarathblobtestsa-sarathblobtestsa-85dc45aa-a0d5-4650-b3cf-38725792d056",
  "properties": {
    "currentProtectionState": "ProtectionConfigured",
    "dataSourceInfo": {
      "datasourceType": "Microsoft.Storage/storageAccounts/blobServices",
      "objectType": "Datasource",
      "resourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathblobtestsa",
      "resourceLocation": "centraluseuap",
      "resourceName": "sarathblobtestsa",
      "resourceType": "Microsoft.Storage/storageAccounts",
      "resourceUri": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathblobtestsa"
    },
    "dataSourceSetInfo": null,
    "friendlyName": "sarathblobtestsa",
    "objectType": "BackupInstance",
    "policyInfo": {
      "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/blobpolicy",
      "policyParameters": {
        "dataStoreParametersList": [
          {
            "dataStoreType": "OperationalStore",
            "objectType": "AzureOperationalStoreParameters",
            "resourceGroupId": ""
          }
        ]
      },
      "policyVersion": ""
    },
    "protectionErrorDetails": null,
    "protectionStatus": {
      "errorDetails": null,
      "status": "ProtectionConfigured"
    },
    "provisioningState": "Succeeded"
  },
  "resourceGroup": "sarath-rg",
  "systemData": null,
  "type": "Microsoft.DataProtection/backupVaults/backupInstances"
}
```
