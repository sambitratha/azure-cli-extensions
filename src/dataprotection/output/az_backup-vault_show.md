
## az dataprotection backup-vault show ##

Returns a resource belonging to a resource group
### Parameters ###
  - --resource-group -g
  - --vault-name
  - --ids

### Examples ###

#### Get a backup Vault by resource group and vault name ####
Command
```
az dataprotection backup-vault show -g sarath-rg --vault-name sarath-vault
```
Output
```json
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
  "tags": null,
  "type": "Microsoft.DataProtection/backupVaults"
}
```

#### Get a backup vault by vault id ####
Command
```
az dataprotection backup-vault show --ids /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.DataProtection/BackupVaults/sarath-vault
```
Output
```
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
```
