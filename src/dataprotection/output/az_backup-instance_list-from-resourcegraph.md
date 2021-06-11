
## az dataprotection backup-instance list-from-resourcegraph ##

List backup instances across subscriptions, resource groups and vaults.
### Parameters ###
  - --resource-groups
  - --vaults
  - --subscriptions
  - --protection-status
  - --datasource-id
  - --datasource-type

### Examples ###

#### List all backup instances of Azure Disk in a vault ####
Command
```
az dataprotection backup-instance list-from-resourcegraph --vaults sarath-vault --datasource-type AzureDisk
```
Output
```json
{
  "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.Compute/disks/clitest",
  "extendedLocation": null,
  "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/clitest-clitest-3165cfe7-a932-11eb-9d24-9cfce85d4fae",
  "identity": null,
  "kind": "",
  "location": "",
  "managedBy": "",
  "name": "clitest-clitest-3165cfe7-a932-11eb-9d24-9cfce85d4fae",
  "plan": null,
  "properties": {
    "currentProtectionState": "ProtectionConfigured",
    "dataSourceInfo": {
      "baseUri": null,
      "datasourceType": "Microsoft.Compute/disks",
      "objectType": "Datasource",
      "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.Compute/disks/clitest",
      "resourceLocation": "centraluseuap",
      "resourceName": "clitest",
      "resourceType": "Microsoft.Compute/disks",
      "resourceUri": ""
    },
    "dataSourceProperties": null,
    "dataSourceSetInfo": null,
    "datasourceAuthCredentials": null,
    "friendlyName": "clitest",
    "objectType": "BackupInstance",
    "policyInfo": {
      "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskPSPolicy2",
      "policyParameters": {
        "dataStoreParametersList": [
          {
            "dataStoreType": "OperationalStore",
            "objectType": "AzureOperationalStoreParameters",
            "resourceGroupId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg"
          }
        ]
      },
      "policyVersion": null
    },
    "protectionErrorDetails": null,
    "protectionStatus": {
      "errorDetails": null,
      "status": "ProtectionConfigured"
    },
    "provisioningState": "Succeeded"
  },
  "protectionState": "ProtectionConfigured",
  "resourceGroup": "sarath-rg",
  "sku": null,
  "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
  "tags": null,
  "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
  "type": "microsoft.dataprotection/backupvaults/backupinstances",
  "vaultName": "sarath-vault",
  "zones": null
}
```

#### List all backup instances in a protection error state in a vault ####
Command
```
az dataprotection backup-instance list-from-resourcegraph --vaults sarath-vault --protection-status ProtectionError
```
Output
```json
[
  {
    "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp4",
    "extendedLocation": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/temp4-temp4-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "identity": null,
    "kind": "",
    "location": "",
    "managedBy": "",
    "name": "temp4-temp4-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "plan": null,
    "properties": {
      "currentProtectionState": "ProtectionError",
      "dataSourceInfo": {
        "baseUri": null,
        "datasourceType": "Microsoft.Compute/disks",
        "objectType": "Datasource",
        "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp4",
        "resourceLocation": "centraluseuap",
        "resourceName": "temp4",
        "resourceType": "Microsoft.Compute/disks",
        "resourceUri": ""
      },
      "dataSourceProperties": null,
      "dataSourceSetInfo": null,
      "datasourceAuthCredentials": null,
      "friendlyName": "temp4",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskDailyPolicy",
        "policyParameters": {
          "dataStoreParametersList": [
            {
              "dataStoreType": "OperationalStore",
              "objectType": null
            }
          ]
        },
        "policyVersion": null
      },
      "protectionErrorDetails": {
        "code": "CloudInternalError",
        "details": null,
        "innerError": null,
        "isRetryable": false,
        "isUserError": false,
        "message": "Microsoft Azure Backup encountered an internal error.",
        "properties": {
          "ActivityId": "5f08710a-bc96-11eb-863b-9cfce85d4fae"
        },
        "recommendedAction": [
          "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
        ],
        "target": ""
      },
      "protectionStatus": {
        "errorDetails": {
          "code": "CloudInternalError",
          "details": null,
          "innerError": null,
          "isRetryable": false,
          "isUserError": false,
          "message": "Microsoft Azure Backup encountered an internal error.",
          "properties": {
            "ActivityId": "5f08710a-bc96-11eb-863b-9cfce85d4fae"
          },
          "recommendedAction": [
            "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
          ],
          "target": ""
        },
        "status": "ProtectionError"
      },
      "provisioningState": "Succeeded"
    },
    "protectionState": "ProtectionError",
    "resourceGroup": "sarath-rg",
    "sku": null,
    "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
    "tags": null,
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "microsoft.dataprotection/backupvaults/backupinstances",
    "vaultName": "sarath-vault",
    "zones": null
  },
  {
    "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp5",
    "extendedLocation": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/temp5-temp5-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "identity": null,
    "kind": "",
    "location": "",
    "managedBy": "",
    "name": "temp5-temp5-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "plan": null,
    "properties": {
      "currentProtectionState": "ProtectionError",
      "dataSourceInfo": {
        "baseUri": null,
        "datasourceType": "Microsoft.Compute/disks",
        "objectType": "Datasource",
        "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp5",
        "resourceLocation": "centraluseuap",
        "resourceName": "temp5",
        "resourceType": "Microsoft.Compute/disks",
        "resourceUri": ""
      },
      "dataSourceProperties": null,
      "dataSourceSetInfo": null,
      "datasourceAuthCredentials": null,
      "friendlyName": "temp5",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskDailyPolicy",
        "policyParameters": {
          "dataStoreParametersList": [
            {
              "dataStoreType": "OperationalStore",
              "objectType": null
            }
          ]
        },
        "policyVersion": null
      },
      "protectionErrorDetails": {
        "code": "CloudInternalError",
        "details": null,
        "innerError": null,
        "isRetryable": false,
        "isUserError": false,
        "message": "Microsoft Azure Backup encountered an internal error.",
        "properties": {
          "ActivityId": "059c9281-bca3-11eb-b183-9cfce85d4fae"
        },
        "recommendedAction": [
          "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
        ],
        "target": ""
      },
      "protectionStatus": {
        "errorDetails": {
          "code": "CloudInternalError",
          "details": null,
          "innerError": null,
          "isRetryable": false,
          "isUserError": false,
          "message": "Microsoft Azure Backup encountered an internal error.",
          "properties": {
            "ActivityId": "059c9281-bca3-11eb-b183-9cfce85d4fae"
          },
          "recommendedAction": [
            "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
          ],
          "target": ""
        },
        "status": "ProtectionError"
      },
      "provisioningState": "Succeeded"
    },
    "protectionState": "ProtectionError",
    "resourceGroup": "sarath-rg",
    "sku": null,
    "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
    "tags": null,
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "microsoft.dataprotection/backupvaults/backupinstances",
    "vaultName": "sarath-vault",
    "zones": null
  }
]
```

#### List all backup instances of Azure Disk across multiple vaults ####

Command 
```
az dataprotection backup-instance list-from-resourcegraph --datasource-type AzureDisk --vaults sarath-vault sarath-vault2
```
Output
```json
[
  {
    "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp5",
    "extendedLocation": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/temp5-temp5-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "identity": null,
    "kind": "",
    "location": "",
    "managedBy": "",
    "name": "temp5-temp5-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "plan": null,
    "properties": {
      "currentProtectionState": "ProtectionError",
      "dataSourceInfo": {
        "baseUri": null,
        "datasourceType": "Microsoft.Compute/disks",
        "objectType": "Datasource",
        "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp5",
        "resourceLocation": "centraluseuap",
        "resourceName": "temp5",
        "resourceType": "Microsoft.Compute/disks",
        "resourceUri": ""
      },
      "dataSourceProperties": null,
      "dataSourceSetInfo": null,
      "datasourceAuthCredentials": null,
      "friendlyName": "temp5",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskDailyPolicy",
        "policyParameters": {
          "dataStoreParametersList": [
            {
              "dataStoreType": "OperationalStore",
              "objectType": null
            }
          ]
        },
        "policyVersion": null
      },
      "protectionErrorDetails": {
        "code": "CloudInternalError",
        "details": null,
        "innerError": null,
        "isRetryable": false,
        "isUserError": false,
        "message": "Microsoft Azure Backup encountered an internal error.",
        "properties": {
          "ActivityId": "059c9281-bca3-11eb-b183-9cfce85d4fae"
        },
        "recommendedAction": [
          "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
        ],
        "target": ""
      },
      "protectionStatus": {
        "errorDetails": {
          "code": "CloudInternalError",
          "details": null,
          "innerError": null,
          "isRetryable": false,
          "isUserError": false,
          "message": "Microsoft Azure Backup encountered an internal error.",
          "properties": {
            "ActivityId": "059c9281-bca3-11eb-b183-9cfce85d4fae"
          },
          "recommendedAction": [
            "Wait for a few minutes and then try the operation again. If the issue persists, please contact Microsoft support."
          ],
          "target": ""
        },
        "status": "ProtectionError"
      },
      "provisioningState": "Succeeded"
    },
    "protectionState": "ProtectionError",
    "resourceGroup": "sarath-rg",
    "sku": null,
    "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
    "tags": null,
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "microsoft.dataprotection/backupvaults/backupinstances",
    "vaultName": "sarath-vault",
    "zones": null
  },
  {
    "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp6",
    "extendedLocation": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/temp6-temp6-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "identity": null,
    "kind": "",
    "location": "",
    "managedBy": "",
    "name": "temp6-temp6-7d67c4b6-bc86-11eb-a650-9cfce85d4fad",
    "plan": null,
    "properties": {
      "currentProtectionState": "ProtectionConfigured",
      "dataSourceInfo": {
        "baseUri": null,
        "datasourceType": "Microsoft.Compute/disks",
        "objectType": "Datasource",
        "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/temp6",
        "resourceLocation": "centraluseuap",
        "resourceName": "temp6",
        "resourceType": "Microsoft.Compute/disks",
        "resourceUri": ""
      },
      "dataSourceProperties": null,
      "dataSourceSetInfo": null,
      "datasourceAuthCredentials": null,
      "friendlyName": "temp6",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskDailyPolicy",
        "policyParameters": {
          "dataStoreParametersList": [
            {
              "dataStoreType": "OperationalStore",
              "objectType": "AzureOperationalStoreParameters",
              "resourceGroupId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg"
            }
          ]
        },
        "policyVersion": null
      },
      "protectionErrorDetails": null,
      "protectionStatus": {
        "errorDetails": null,
        "status": "ProtectionConfigured"
      },
      "provisioningState": "Succeeded"
    },
    "protectionState": "ProtectionConfigured",
    "resourceGroup": "sarath-rg",
    "sku": null,
    "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
    "tags": null,
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "microsoft.dataprotection/backupvaults/backupinstances",
    "vaultName": "sarath-vault",
    "zones": null
  }
]
```

#### List backup instance with a given datasource id ####
Command
```
az dataprotection backup-instance list-from-resourcegraph --datasource-type AzureDisk --datasource-id /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk
```
Output
```json
[
  {
    "datasourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk",
    "extendedLocation": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/sarathdisk-sarathdisk-3df6ac08-9496-4839-8fb5-8b78e594f166",
    "identity": null,
    "kind": "",
    "location": "",
    "managedBy": "",
    "name": "sarathdisk-sarathdisk-3df6ac08-9496-4839-8fb5-8b78e594f166",
    "plan": null,
    "properties": {
      "currentProtectionState": "ProtectionConfigured",
      "dataSourceInfo": {
        "baseUri": null,
        "datasourceType": "Microsoft.Compute/disks",
        "objectType": "Datasource",
        "resourceID": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk",
        "resourceLocation": "centraluseuap",
        "resourceName": "sarathdisk",
        "resourceType": "Microsoft.Compute/disks",
        "resourceUri": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk"
      },
      "dataSourceProperties": null,
      "dataSourceSetInfo": null,
      "datasourceAuthCredentials": null,
      "friendlyName": "sarathdisk",
      "objectType": "BackupInstance",
      "policyInfo": {
        "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskPolicy1",
        "policyParameters": {
          "dataStoreParametersList": [
            {
              "dataStoreType": "OperationalStore",
              "objectType": "AzureOperationalStoreParameters",
              "resourceGroupId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg"
            }
          ]
        },
        "policyVersion": null
      },
      "protectionErrorDetails": null,
      "protectionStatus": {
        "errorDetails": null,
        "status": "ProtectionConfigured"
      },
      "provisioningState": "Succeeded"
    },
    "protectionState": "ProtectionConfigured",
    "resourceGroup": "sarath-rg",
    "sku": null,
    "subscriptionId": "62b829ee-7936-40c9-a1c9-47a93f9f3965",
    "tags": null,
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "microsoft.dataprotection/backupvaults/backupinstances",
    "vaultName": "sarath-vault",
    "zones": null
  }
]
```

