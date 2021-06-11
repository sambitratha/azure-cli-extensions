
## az dataprotection backup-instance create ##

Configure backup for a resource in a backup vault.
### Parameters ###
  - --resource-group -g
  - --vault-name
  - --backup-instance
  - --no-wait

### Examples ###

#### Configure backup of a resource ####
Command
```
az dataprotection backup-instance create -g sarath-rg --vault-name sarath-vault --backup-instance backup_instance.json
```
Output
```json
{
  "id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupInstances/sarathdisk-sarathdisk-b815f593-ca93-11eb-86f3-9cfce85d4fae",
  "name": "sarathdisk-sarathdisk-b815f593-ca93-11eb-86f3-9cfce85d4fae",
  "properties": {
    "currentProtectionState": "ProtectionConfigured",
    "dataSourceInfo": {
      "datasourceType": "Microsoft.Compute/disks",
      "objectType": "Datasource",
      "resourceId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk",
      "resourceLocation": "southeastasia",
      "resourceName": "sarathdisk",
      "resourceType": "Microsoft.Compute/disks",
      "resourceUri": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk"
    },
    "dataSourceSetInfo": null,
    "friendlyName": "sarathdisk",
    "objectType": "BackupInstance",
    "policyInfo": {
      "policyId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg/providers/Microsoft.DataProtection/backupVaults/sarath-vault/backupPolicies/DiskPolicy",
      "policyParameters": {
        "dataStoreParametersList": [
          {
            "dataStoreType": "OperationalStore",
            "objectType": "AzureOperationalStoreParameters",
            "resourceGroupId": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegroups/sarath-rg"
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
  "resourceGroup": "sarath-rg",
  "systemData": null,
  "type": "Microsoft.DataProtection/backupVaults/backupInstances"
}
```

##### Sample input file backup_instance.json #####
```json
{
  "backup_instance_name": "sarathdisk-sarathdisk-b815f593-ca93-11eb-86f3-9cfce85d4fae",
  "properties": {
    "data_source_info": {
      "datasource_type": "Microsoft.Compute/disks",
      "object_type": "Datasource",
      "resource_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourcegGroups/sarath-rg/providers/Microsoft.Compute/disks/sarathdisk",
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
            "resource_group_id": "/subscriptions/62b829ee-7936-40c9-a1c9-47a93f9f3965/resourceGroups/sarath-rg"
          }
        ]
      }
    }
  }
}
```
