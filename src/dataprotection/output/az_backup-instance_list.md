
## az dataprotection backup-instance list ##

Create a BackupVault resource belonging to a resource group.
### Parameters ###
  - --resource-group -g
  - --vault-name

### Examples ###

#### List all backup instances in a backup vault ####
Command
```
az dataprotection backup-instance list -g sarath-rg --vault-name sarath-vault
```
Output
```json
[
  {
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/cliakneema-cliakneema-699bb875-c437-11eb-94be-c8f750f92764",
    "name": "cliakneema-cliakneema-699bb875-c437-11eb-94be-c8f750f92764",
    "properties": {
      "currentProtectionState": "ProtectionError",
      "dataSourceInfo": {
        "datasourceType": "Microsoft.Storage/storageAccounts/blobServices",
        "objectType": "Datasource",
        "resourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/ABC/providers/Microsoft.Storage/storageAccounts/cliakneema",
        "resourceLocation": "akneema",
        "resourceName": "cliakneema",
        "resourceType": "Microsoft.Storage/storageAccounts",
        "resourceUri": ""
      },
      "dataSourceSetInfo": null,
      "friendlyName": "cliakneema",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/blobclipolicy",
        "policyParameters": null,
        "policyVersion": null
      },
      "protectionErrorDetails": {
        "code": "UserErrorMissingRequiredPermissions",
        "details": null,
        "innerError": null,
        "isRetryable": false,
        "isUserError": false,
        "message": "Appropriate permissions to perform the operation is missing.",
        "properties": {
          "ActivityId": "0e684b2f-cf83-47d4-8b67-c5c1397ef0a5-Ibz"
        },
        "recommendedAction": [
          "Grant appropriate permissions to perform this operation as mentioned at https://aka.ms/UserErrorMissingRequiredPermissions and retry the operation."
        ],
        "target": ""
      },
      "protectionStatus": {
        "errorDetails": {
          "code": "UserErrorMissingRequiredPermissions",
          "details": null,
          "innerError": null,
          "isRetryable": false,
          "isUserError": false,
          "message": "Appropriate permissions to perform the operation is missing.",
          "properties": {
            "ActivityId": "0e684b2f-cf83-47d4-8b67-c5c1397ef0a5-Ibz"
          },
          "recommendedAction": [
            "Grant appropriate permissions to perform this operation as mentioned at https://aka.ms/UserErrorMissingRequiredPermissions and retry the operation."
          ],
          "target": ""
        },
        "status": "ProtectionError"
      },
      "provisioningState": "Succeeded"
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "type": "Microsoft.DataProtection/backupVaults/backupInstances"
  },
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
]
```
