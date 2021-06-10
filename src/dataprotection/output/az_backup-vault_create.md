
## az dataprotection backup-vault create ##

Create a BackupVault resource belonging to a resource group.
### Parameters ###
  - --resource-group -g
  - --vault-name
  - --storage-settings
  - --e-tag
  - --location -l
  - --no-wait
  - --tags
  - --type

### Examples ###

#### Create a backup Vault ####
Command
```
az dataprotection backup-vault create -g sarath-rg --vault-name sarath-vault -l centraluseuap --type SystemAssigned --storage-settings datastore-type="VaultStore" type="LocallyRedundant"
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
