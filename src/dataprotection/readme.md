### az dataprotection module ###

Dataprotection module used to create backup vaults and manage backup instances in vaults. Use this module to protect Azure disk and Azure blobs in a backup vault.

--------------------------------------------------------------------------------
#### Backup vault create, list, show, delete ####
|Command Name | Description | Link to documentation
| :--- | :--- | :----:|
| az dataprotection backup-vault create | Create a backup vault in a resource group | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-vault_create.md)
| az dataprotection backup-vault show | Gets a backup vault by name or id | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-vault_show.md)
| az dataprotection backup-vault list | Gets list of backup vault in a subscription or in a resource group. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-vault_list.md)
| az dataprotection backup-vault delete | Deletes a BackupVault resource from the resource group. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-vault_delete.md)

--------------------------------------------------------------------------------------
#### Backup instances create, list, show, delete ####
|Command Name | Description | Link to documentation
| :--- | :--- | :----:|
| az dataprotection backup-instance create | Configure backup for a resource in a backup vault. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-instance_create.md)
| az dataprotection backup-instance show | Gets a backup instance with name in a backup vault. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-instance_show.md)
| az dataprotection backup-instance list | Create a BackupVault resource belonging to a resource group. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-instance_list.md)
| az dataprotection backup-instance delete | Delete a backup instance in a backup vault. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-instance_delete.md)
| az dataprotection backup-instance list-from-resourcegraph | List backup instances across subscriptions, resource groups and vaults. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-instance_list-from-resourcegraph.md)

-----------------------------------------------------------------
#### Backup policy ####
##### Get default policy, create backup policy, list policy, delete policy #####
|Command Name | Description | Link to documentation
| :--- | :--- | :----:|
| az dataprotection backup-policy get-default-policy-template | Get default policy template for a given datasource type. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_get-default-policy-template.md)

##### Create, update, remove retention rule in a backup policy #####
|Command Name | Description | Link to documentation
| :--- | :--- | :----:|
| az dataprotection backup-policy retention-rule create-lifecycle | Create lifecycle for Azure retention rule. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_retention-rule_create-lifecycle.md)
| az dataprotection backup-policy retention-rule set | Add new retention rule or update existing retention rule. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_retention-rule_set.md)
| az dataprotection backup-policy retention-rule remove | Remove existing retention rule in a existing backup policy. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_retention-rule_remove.md)

##### Create, update, remove tag criteria in a backup policy #####
|Command Name | Description | Link to documentation
| :--- | :--- | :----:|
| az dataprotection backup-policy tag create-absolute-criteria | Create absolute criteria. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_tag_create-absolute-criteria.md)
| az dataprotection backup-policy tag create-generic-criteria | Create generic criteria. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_tag_create-generic-criteria.md)
| az dataprotection backup-policy tag set | Add new tag or update existing tag of a backup policy. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_tag_set.md)
| az dataprotection backup-policy tag remove | Remove existing tag from a backup policy. | [Link](https://github.com/sambitratha/azure-cli-extensions/blob/documentation/src/dataprotection/output/az_backup-policy_tag_remove.md)

