
## az dataprotection backup-instance restore trigger ##

Triggers restore for a BackupInstance
### Parameters ###
  - --backup-instance-name --name -n
  - --resource-group -g
  - --vault-name
  - --ids
  - --restore-request-object

### Examples ###

#### Trigger restore ####
Command
```
az dataprotection backup-instance restore trigger --ids /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/clitest-clitest-3165cfe7-a932-11eb-9d24-9cfce85d4fae --restore-request-object restore_request.json
```
Sample restore_request.json input
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
{
  "jobId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.DataProtection/BackupVaults/sarath-vault/backupJobs/3b651af9-43eb-4f49-9374-6c8cfcaefc78",
  "objectType": "OperationJobExtendedInfo"
}
```
