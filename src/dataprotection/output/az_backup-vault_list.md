
## az dataprotection backup-vault list ##

Gets list of backup vault in a subscription or in a resource group.
### Parameters ###
  - --resource-group -g

### Examples ###

#### Gets list of vaults in a resource group ####
Command
```
az dataprotection backup-vault list -g sarath-rg
```
Output
```json
Command group 'dataprotection' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
[
  {
    "eTag": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/cli-test-vault2",
    "identity": {
      "principalId": "5a6b810f-a30b-443a-ac0b-0c814f386663",
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "type": "SystemAssigned"
    },
    "location": "centraluseuap",
    "name": "cli-test-vault2",
    "properties": {
      "provisioningState": "Succeeded",
      "storageSettings": [
        {
          "datastoreType": "VaultStore",
          "type": "LocallyRedundant"
        }
      ]
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "tags": null,
    "type": "Microsoft.DataProtection/backupVaults"
  },
  {
    "eTag": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.DataProtection/BackupVaults/sarath-vault",
    "identity": {
      "principalId": "2ca1d5f7-38b3-4b61-aa45-8147d7e0edbc",
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "type": "SystemAssigned"
    },
    "location": "centraluseuap",
    "name": "sarath-vault",
    "properties": {
      "provisioningState": "Succeeded",
      "storageSettings": [
        {
          "datastoreType": "VaultStore",
          "type": "LocallyRedundant"
        }
      ]
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "tags": {
      "A": "b"
    },
    "type": "Microsoft.DataProtection/backupVaults"
  }
]
```
#### Get a list of vaults in a subscription
Command
```
az dataprotection backup-vault list
```
Output
```json
[
  {
    "eTag": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/cli-test-vault",
    "identity": {
      "principalId": "e5e3fcd6-e641-4895-aa09-e08f4f1d336e",
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "type": "SystemAssigned"
    },
    "location": "centraluseuap",
    "name": "cli-test-vault",
    "properties": {
      "provisioningState": "Succeeded",
      "storageSettings": [
        {
          "datastoreType": "VaultStore",
          "type": "LocallyRedundant"
        }
      ]
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "tags": null,
    "type": "Microsoft.DataProtection/backupVaults"
  },
  {
    "eTag": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/cli-test-vault2",
    "identity": {
      "principalId": "5a6b810f-a30b-443a-ac0b-0c814f386663",
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "type": "SystemAssigned"
    },
    "location": "centraluseuap",
    "name": "cli-test-vault2",
    "properties": {
      "provisioningState": "Succeeded",
      "storageSettings": [
        {
          "datastoreType": "VaultStore",
          "type": "LocallyRedundant"
        }
      ]
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "tags": null,
    "type": "Microsoft.DataProtection/backupVaults"
  },
  {
    "eTag": null,
    "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.DataProtection/BackupVaults/sarath-vault",
    "identity": {
      "principalId": "2ca1d5f7-38b3-4b61-aa45-8147d7e0edbc",
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "type": "SystemAssigned"
    },
    "location": "centraluseuap",
    "name": "sarath-vault",
    "properties": {
      "provisioningState": "Succeeded",
      "storageSettings": [
        {
          "datastoreType": "VaultStore",
          "type": "LocallyRedundant"
        }
      ]
    },
    "resourceGroup": "sarath-rg",
    "systemData": null,
    "tags": {
      "A": "b"
    },
    "type": "Microsoft.DataProtection/backupVaults"
  }
]
```
