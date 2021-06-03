manifest = '''
{
  "isProxyResource": false,
  "resourceType": "Microsoft.Storage/storageAccounts",
  "parentResourceType": "Microsoft.Storage/storageAccounts",
  "datasourceType": "Microsoft.Storage/storageAccounts/blobServices",
  "allowedRestoreModes": [ "PointInTimeBased" ],
  "allowedRestoreTargetTypes": [ "OriginalLocation" ],
  "itemLevelRecoveyEnabled": true,
  "policySettings": {
    "supportedRetentionTags": [],
    "supportedDatastoreTypes": [ "OperationalStore" ],
    "disableAddRetentionRule": true,
    "disableCustomRetentionTag": true,
    "backupScheduleSupported": false,
    "supportedBackupFrequency": [],
    "defaultPolicy": {
      "policyRules": [
        {
          "lifecycles": [
            {
              "deleteAfter": {
                "objectType": "AbsoluteDeleteOption",
                "duration": "P30D"
              },
              "sourceDataStore": {
                "dataStoreType": "OperationalStore",
                "objectType": "DataStoreInfoBase"
              }
            }
          ],
          "isDefault": true,
          "name": "Default",
          "objectType": "AzureRetentionRule"
        }
      ],
      "name": "BlobPolicy1",
      "datasourceTypes": [
        "Microsoft.Storage/storageAccounts/blobServices"
      ],
      "objectType": "BackupPolicy"
    }
  }
}'''
