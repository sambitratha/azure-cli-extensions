
## az dataprotection backup-policy tag create-absolute-criteria ##

Create absolute criteria
### Parameters ###
  - --absolute-criteria

### Examples ###

#### Create absolute criteria ####
Command
```
az dataprotection backup-policy tag create-absolute-criteria --absolute-criteria FirstOfDay
```
Output
```json
{
  "absoluteCriteria": [
    "FirstOfDay"
  ],
  "objectType": "ScheduleBasedBackupCriteria"
}
```
