
## az dataprotection backup-instance validate-for-restore ##

Validates if Restore can be triggered for a DataSource.
### Parameters ###
  - --backup-instance-name --name -n
  - --restore-request-object
  - --resource-group -g
  - --vault-name 
  - --ids

### Examples ###

#### Create a backup Vault ####
Command
```
az dataprotection backup-instance validate-for-restore --ids /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/clitest-clitest-3165cfe7-a932-11eb-9d24-9cfce85d4fae --restore-request-object restore_request.json
```
Sample restore_request.json file
```json
{
  "object_type": "AzureBackupRecoveryPointBasedRestoreRequest",
  "recovery_point_id": "77594ce0470849e79b86a6875b726dca",
  "restore_target_info": {
    "datasource_info": {
      "datasource_type": "Microsoft.Compute/disks",
      "object_type": "Datasource",
      "resource_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/clitest-restore",
      "resource_location": "centraluseuap",
      "resource_name": "clitest-restore",
      "resource_type": "Microsoft.Compute/disks",
      "resource_uri": ""
    },
    "object_type": "RestoreTargetInfo",
    "recovery_option": "FailIfExists",
    "restore_location": "centraluseuap"
  },
  "source_data_store_type": "OperationalStore"
}
```
Output
```json

```
