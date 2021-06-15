
## az dataprotection backup-instance restore initialize-for-data-recovery ##

Initialize restore request object to recover all backed up data in a backup vault.
### Parameters ###
  - --datasource-type
  - --restore-location
  - --source-datastore
  - --target-resource-id
  - --point-in-time
  - --recovery-point-id

### Examples ###

#### Create a backup Vault ####
Command
```
az dataprotection backup-instance restore initialize-for-data-recovery --datasource-type AzureDisk --restore-location centraluseuap --source-datastore OperationalStore --target-resource-id /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Compute/clitest-restore --recovery-point-id 77594ce0470849e79b86a6875b726dca
```
Output
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
