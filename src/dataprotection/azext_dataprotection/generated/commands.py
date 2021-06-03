# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_dataprotection.generated._client_factory import (
    cf_backup_vault,
    cf_backup_policy,
    cf_backup_instance,
    cf_recovery_point,
    cf_job,
    cf_restorable_time_range,
)


dataprotection_backup_vault = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._backup_vaults_operations#BackupVaultsOperations.{}',
    client_factory=cf_backup_vault,
)


dataprotection_backup_policy = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._backup_policies_operations#BackupPoliciesOperations.{}',
    client_factory=cf_backup_policy,
)


dataprotection_backup_instance = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._backup_instances_operations#BackupInstancesOperations.{}',
    client_factory=cf_backup_instance,
)


dataprotection_recovery_point = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._recovery_points_operations#RecoveryPointsOperations.{}',
    client_factory=cf_recovery_point,
)


dataprotection_job = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._jobs_operations#JobsOperations.{}',
    client_factory=cf_job,
)


dataprotection_restorable_time_range = CliCommandType(
    operations_tmpl='azext_dataprotection.vendored_sdks.dataprotection.operations._restorable_time_ranges_operations#RestorableTimeRangesOperations.{}',
    client_factory=cf_restorable_time_range,
)


def load_command_table(self, _):

    with self.command_group(
        'dataprotection backup-vault', dataprotection_backup_vault, client_factory=cf_backup_vault
    ) as g:
        g.custom_show_command('show', 'dataprotection_backup_vault_show')
        g.custom_command('create', 'dataprotection_backup_vault_create', supports_no_wait=True)
        g.custom_command('update', 'dataprotection_backup_vault_update', supports_no_wait=True)
        g.custom_command('delete', 'dataprotection_backup_vault_delete', confirmation=True)
        g.custom_command('list-in-resource-group', 'dataprotection_backup_vault_list_in_resource_group')
        g.custom_command('list-in-subscription', 'dataprotection_backup_vault_list_in_subscription')
        g.custom_wait_command('wait', 'dataprotection_backup_vault_show')

    with self.command_group(
        'dataprotection backup-policy', dataprotection_backup_policy, client_factory=cf_backup_policy
    ) as g:
        g.custom_command('list', 'dataprotection_backup_policy_list')
        g.custom_show_command('show', 'dataprotection_backup_policy_show')
        g.custom_command('create', 'dataprotection_backup_policy_create')
        g.custom_command('delete', 'dataprotection_backup_policy_delete', confirmation=True)

    with self.command_group(
        'dataprotection backup-instance', dataprotection_backup_instance, client_factory=cf_backup_instance
    ) as g:
        g.custom_command('list', 'dataprotection_backup_instance_list')
        g.custom_show_command('show', 'dataprotection_backup_instance_show')
        g.custom_command('create', 'dataprotection_backup_instance_create', supports_no_wait=True)
        g.custom_command('delete', 'dataprotection_backup_instance_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('adhoc-backup', 'dataprotection_backup_instance_adhoc_backup', supports_no_wait=True)
        g.custom_command('restore trigger', 'dataprotection_backup_instance_restore_trigger', supports_no_wait=True)
        g.custom_command(
            'validate-for-backup', 'dataprotection_backup_instance_validate_for_backup', supports_no_wait=True
        )
        g.custom_command(
            'validate-for-restore', 'dataprotection_backup_instance_validate_for_restore', supports_no_wait=True
        )
        g.custom_wait_command('wait', 'dataprotection_backup_instance_show')

    with self.command_group(
        'dataprotection recovery-point', dataprotection_recovery_point, client_factory=cf_recovery_point
    ) as g:
        g.custom_command('list', 'dataprotection_recovery_point_list')
        g.custom_show_command('show', 'dataprotection_recovery_point_show')

    with self.command_group('dataprotection job', dataprotection_job, client_factory=cf_job) as g:
        g.custom_command('list', 'dataprotection_job_list')
        g.custom_show_command('show', 'dataprotection_job_show')

    with self.command_group(
        'dataprotection restorable-time-range',
        dataprotection_restorable_time_range,
        client_factory=cf_restorable_time_range,
    ) as g:
        g.custom_command('find', 'dataprotection_restorable_time_range_find')

    with self.command_group('dataprotection', is_experimental=True):
        pass
