
## az dataprotection backup-policy tag create-generic-criteria ##

Create generic criteria.
### Parameters ###
  - --days-of-month
  - --days-of-week
  - --months-of-year
  - --weeks-of-month
### Examples ###

#### Create weekly tag criteria ####
Command
```
az dataprotection backup-policy tag create-generic-criteria --days-of-week Sunday Monday
```
Output
```json
{
  "days_of_month": null,
  "days_of_the_week": [
    "Sunday",
    "Monday"
  ],
  "months_of_year": null,
  "object_type": "ScheduleBasedBackupCriteria",
  "weeks_of_the_month": null
}
```

#### Create yearly tag criteria ####
Command
```
az dataprotection backup-policy tag create-generic-criteria --days-of-week Sunday Monday --weeks-of-month First Fourth --months-of-year April May
```
Output
```json
{
  "days_of_month": null,
  "days_of_the_week": [
    "Sunday",
    "Monday"
  ],
  "months_of_year": [
    "April",
    "May"
  ],
  "object_type": "ScheduleBasedBackupCriteria",
  "weeks_of_the_month": [
    "First",
    "Fourth"
  ]
}
```
