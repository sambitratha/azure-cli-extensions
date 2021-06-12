
## az dataprotection backup-policy retention-rule create-lifecycle ##

Create lifecycle for Azure retention rule.
### Parameters ###
  - --retention-duration-count --count
  - --retention-duration-type --type
  - --source-datastore
  - --copy-option
  - --target-datastore

### Examples ###

#### Create daily lifecycle ####
Command
```
az dataprotection backup-policy retention-rule create-lifecycle --retention-duration-count 12 --retention-duration-type Days --source-datastore OperationalStore
```
Output
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

#### Create weekly lifecycle ####
Command
```
az dataprotection backup-policy retention-rule create-lifecycle --retention-duration-count 12 --retention-duration-type Weeks --source-datastore OperationalStore
```
Output
```json
{
  "deleteAfter": {
    "duration": "P12W",
    "objectType": "AbsoluteDeleteOption"
  },
  "sourceDataStore": {
    "dataStoreType": "OperationalStore",
    "objectType": "DataStoreInfoBase"
  },
  "targetDataStoreCopySettings": null
}
```
