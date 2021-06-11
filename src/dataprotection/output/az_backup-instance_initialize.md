
## az dataprotection backup-instance initialize ##

Initialize JSON request body for configuring  backup of a resource.
### Parameters ###
  - --datasource-id
  - --datasource-location -l
  - --datasource-type
  - --policy-id

### Examples ###

#### Initialize backup instance request for Azure Disk ####
Command
```
az dataprotection backup-instance initialize --datasource-id /subscriptions/38304e13-357e-405e-9e9a-220351dcce8c/resourcegGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk -l southeastasia --datasource-type AzureDisk --policy-id /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskPolicy
```
Output
```json
{
  "backup_instance_name": "sarathdisk-sarathdisk-b815f593-ca93-11eb-86f3-9cfce85d4fae",
  "properties": {
    "data_source_info": {
      "datasource_type": "Microsoft.Compute/disks",
      "object_type": "Datasource",
      "resource_id": "/subscriptions/38304e13-357e-405e-9e9a-220351dcce8c/resourcegGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk",
      "resource_location": "southeastasia",
      "resource_name": "sarathdisk",
      "resource_type": "Microsoft.Compute/disks",
      "resource_uri": ""
    },
    "data_source_set_info": null,
    "object_type": "BackupInstance",
    "policy_info": {
      "policy_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskPolicy",
      "policy_parameters": {
        "data_store_parameters_list": [
          {
            "data_store_type": "OperationalStore",
            "object_type": "AzureOperationalStoreParameters",
            "resource_group_id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}"
          }
        ]
      }
    }
  }
}
```

#### Initialize backup instance request for Azure Blob ####
Command
```
az dataprotection backup-instance initialize --datasource-id /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathsa -l centraluseuap --datasource-type AzureBlob --policy-id /subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/blobpolicy
```
Output
```json
{
  "backup_instance_name": "sarathsa-sarathsa-fb6b6ac5-ca93-11eb-b683-9cfce85d4fae",
  "properties": {
    "data_source_info": {
      "datasource_type": "Microsoft.Storage/storageAccounts/blobServices",
      "object_type": "Datasource",
      "resource_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.Storage/storageAccounts/sarathsa",
      "resource_location": "centraluseuap",
      "resource_name": "sarathsa",
      "resource_type": "Microsoft.Storage/storageAccounts",
      "resource_uri": ""
    },
    "data_source_set_info": null,
    "object_type": "BackupInstance",
    "policy_info": {
      "policy_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/blobpolicy",
      "policy_parameters": null
    }
  }
}
```
