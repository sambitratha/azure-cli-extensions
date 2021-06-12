
## az dataprotection backup-policy retention-rule set ##

Add new retention rule or update existing retention rule
### Parameters ###
  - --lifecycles
  - --name
  - --policy

### Examples ###

#### Add new daily retention rule to existing policy ####
Command
```
az dataprotection backup-policy retention-rule set --policy policy.json --lifecycles lifecycle.json --name Daily
```
Here's how a sample policy.json file looks like
```json
{
  "datasourceTypes": [
    "Microsoft.Compute/disks"
  ],
  "name": "DiskPolicy1",
  "objectType": "BackupPolicy",
  "policyRules": [
    {
      "backupParameters": {
        "backupType": "Incremental",
        "objectType": "AzureBackupParams"
      },
      "dataStore": {
        "dataStoreType": "OperationalStore",
        "objectType": "DataStoreInfoBase"
      },
      "name": "BackupHourly",
      "objectType": "AzureBackupRule",
      "trigger": {
        "objectType": "ScheduleBasedTriggerContext",
        "schedule": {
          "repeatingTimeIntervals": [
            "R/2020-04-05T13:00:00+00:00/PT4H"
          ]
        },
        "taggingCriteria": [
          {
            "isDefault": true,
            "tagInfo": {
              "id": "Default_",
              "tagName": "Default"
            },
            "taggingPriority": 99
          }
        ]
      }
    },
    {
      "isDefault": true,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P7D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          }
        }
      ],
      "name": "Default",
      "objectType": "AzureRetentionRule"
    }
  ]
}
```
Here's how a sample lifecycle.json file looks like
```json
{
  "deleteAfter": {
    "duration": "P12D",
    "objectType": "AbsoluteDeleteOption"
  },
  "sourceDataStore": {
    "dataStoreType": "OperationalStore",
    "objectType": "DataStoreInfoBase"
  },
  "targetDataStoreCopySettings": null
}
```
Output
```json
{
  "datasourceTypes": [
    "Microsoft.Compute/disks"
  ],
  "name": "DiskPolicy1",
  "objectType": "BackupPolicy",
  "policyRules": [
    {
      "backupParameters": {
        "backupType": "Incremental",
        "objectType": "AzureBackupParams"
      },
      "dataStore": {
        "dataStoreType": "OperationalStore",
        "objectType": "DataStoreInfoBase"
      },
      "name": "BackupHourly",
      "objectType": "AzureBackupRule",
      "trigger": {
        "objectType": "ScheduleBasedTriggerContext",
        "schedule": {
          "repeatingTimeIntervals": [
            "R/2020-04-05T13:00:00+00:00/PT4H"
          ]
        },
        "taggingCriteria": [
          {
            "isDefault": true,
            "tagInfo": {
              "id": "Default_",
              "tagName": "Default"
            },
            "taggingPriority": 99
          }
        ]
      }
    },
    {
      "isDefault": true,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P7D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          }
        }
      ],
      "name": "Default",
      "objectType": "AzureRetentionRule"
    },
    {
      "isDefault": false,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P12D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          },
          "targetDataStoreCopySettings": null
        }
      ],
      "name": "Daily",
      "objectType": "AzureRetentionRule"
    }
  ]
}
```

#### Update existing daily retention rule of a policy ####
Command
```
az dataprotection backup-policy retention-rule set --policy policy.json --lifecycles lifecycle.json --name Daily
```
Here's how a sample policy.json file looks like
```json
{
  "datasourceTypes": [
    "Microsoft.Compute/disks"
  ],
  "name": "DiskPolicy1",
  "objectType": "BackupPolicy",
  "policyRules": [
    {
      "backupParameters": {
        "backupType": "Incremental",
        "objectType": "AzureBackupParams"
      },
      "dataStore": {
        "dataStoreType": "OperationalStore",
        "objectType": "DataStoreInfoBase"
      },
      "name": "BackupHourly",
      "objectType": "AzureBackupRule",
      "trigger": {
        "objectType": "ScheduleBasedTriggerContext",
        "schedule": {
          "repeatingTimeIntervals": [
            "R/2020-04-05T13:00:00+00:00/PT4H"
          ]
        },
        "taggingCriteria": [
          {
            "isDefault": true,
            "tagInfo": {
              "id": "Default_",
              "tagName": "Default"
            },
            "taggingPriority": 99
          }
        ]
      }
    },
    {
      "isDefault": true,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P7D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          }
        }
      ],
      "name": "Default",
      "objectType": "AzureRetentionRule"
    },
    {
      "isDefault": false,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P12D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          },
          "targetDataStoreCopySettings": null
        }
      ],
      "name": "Daily",
      "objectType": "AzureRetentionRule"
    }
  ]
}
```
Here's how a sample lifecycle.json file looks like
```json
{
  "deleteAfter": {
    "duration": "P20D",
    "objectType": "AbsoluteDeleteOption"
  },
  "sourceDataStore": {
    "dataStoreType": "OperationalStore",
    "objectType": "DataStoreInfoBase"
  },
  "targetDataStoreCopySettings": null
}
```
Output
```json
{
  "datasourceTypes": [
    "Microsoft.Compute/disks"
  ],
  "name": "DiskPolicy1",
  "objectType": "BackupPolicy",
  "policyRules": [
    {
      "backupParameters": {
        "backupType": "Incremental",
        "objectType": "AzureBackupParams"
      },
      "dataStore": {
        "dataStoreType": "OperationalStore",
        "objectType": "DataStoreInfoBase"
      },
      "name": "BackupHourly",
      "objectType": "AzureBackupRule",
      "trigger": {
        "objectType": "ScheduleBasedTriggerContext",
        "schedule": {
          "repeatingTimeIntervals": [
            "R/2020-04-05T13:00:00+00:00/PT4H"
          ]
        },
        "taggingCriteria": [
          {
            "isDefault": true,
            "tagInfo": {
              "id": "Default_",
              "tagName": "Default"
            },
            "taggingPriority": 99
          }
        ]
      }
    },
    {
      "isDefault": true,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P7D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          }
        }
      ],
      "name": "Default",
      "objectType": "AzureRetentionRule"
    },
    {
      "isDefault": false,
      "lifecycles": [
        {
          "deleteAfter": {
            "duration": "P20D",
            "objectType": "AbsoluteDeleteOption"
          },
          "sourceDataStore": {
            "dataStoreType": "OperationalStore",
            "objectType": "DataStoreInfoBase"
          },
          "targetDataStoreCopySettings": null
        }
      ],
      "name": "Daily",
      "objectType": "AzureRetentionRule"
    }
  ]
}
```
This command will update the deleteAfter duration field of daily retention rule from P12D to P20D (updated daily retention duration)
