# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_dataprotection.action import (
    AddStorageSettings,
    AddBackupPolicy,
    AddDataSourceInfo,
    AddDataSourceSetInfo,
    AddPolicyParameters
)


def load_arguments(self, _):

    with self.argument_context('dataprotection backup-vault show') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-vault create') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('e_tag', type=str, help='Optional ETag.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('type_', options_list=['--type'], type=str, help='The identityType which can be either '
                   'SystemAssigned or None', arg_group='Identity')
        c.argument('storage_settings', action=AddStorageSettings, nargs='+', help='Storage Settings')

    with self.argument_context('dataprotection backup-vault update') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('tags', tags_type)
        c.argument('type_', options_list=['--type'], type=str, help='The identityType which can be either '
                   'SystemAssigned or None', arg_group='Identity')

    with self.argument_context('dataprotection backup-vault delete') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-vault list-in-resource-group') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-vault wait') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-policy list') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-policy show') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_policy_name', options_list=['--name', '-n', '--backup-policy-name'], type=str, help='Backup '
                   'policy name', id_part='child_name_1')

    with self.argument_context('dataprotection backup-policy create') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_policy_name', options_list=['--name', '-n', '--backup-policy-name'], type=str, help='Backup '
                   'policy name')
        c.argument('backup_policy', action=AddBackupPolicy, nargs='+', help='Rule based backup policy',
                   arg_group='Properties')

    with self.argument_context('dataprotection backup-policy delete') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_policy_name', options_list=['--name', '-n', '--backup-policy-name'], type=str, help='Backup '
                   'policy name', id_part='child_name_1')

    with self.argument_context('dataprotection backup-instance list') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('dataprotection backup-instance show') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')

    with self.argument_context('dataprotection backup-instance create') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance')
        c.argument('friendly_name', type=str, help='Gets or sets the Backup Instance friendly name.')
        c.argument('data_source_info', action=AddDataSourceInfo, nargs='+', help='Gets or sets the data source '
                   'information.')
        c.argument('data_source_set_info', action=AddDataSourceSetInfo, nargs='+', help='Gets or sets the data source '
                   'set information.')
        c.argument('object_type', type=str, help='')
        c.argument('policy_id', type=str, help='', arg_group='Policy Info')
        c.argument('policy_parameters', action=AddPolicyParameters, nargs='+', help='Policy parameters for the backup '
                   'instance', arg_group='Policy Info')

    with self.argument_context('dataprotection backup-instance delete') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')

    with self.argument_context('dataprotection backup-instance adhoc-backup') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')
        c.argument('rule_name', type=str, help='Specify backup policy rule name.', arg_group='Backup Rule Options')
        c.argument('retention_tag_override', type=str, help='Specify retention override tag.', arg_group='Backup Rule '
                   'Options Trigger Option')

    with self.argument_context('dataprotection backup-instance restore trigger') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')
        c.argument('parameters', type=validate_file_or_dict, help='Request body for operation Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('dataprotection backup-instance validate-for-backup') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('friendly_name', type=str, help='Gets or sets the Backup Instance friendly name.',
                   arg_group='Backup Instance')
        c.argument('data_source_info', action=AddDataSourceInfo, nargs='+', help='Gets or sets the data source '
                   'information.', arg_group='Backup Instance')
        c.argument('data_source_set_info', action=AddDataSourceSetInfo, nargs='+', help='Gets or sets the data source '
                   'set information.', arg_group='Backup Instance')
        c.argument('object_type', type=str, help='', arg_group='Backup Instance')
        c.argument('policy_id', type=str, help='', arg_group='Backup Instance Policy Info')
        c.argument('policy_parameters', action=AddPolicyParameters, nargs='+', help='Policy parameters for the backup '
                   'instance', arg_group='Backup Instance Policy Info')

    with self.argument_context('dataprotection backup-instance validate-for-restore') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')
        c.argument('restore_request_object', type=validate_file_or_dict, help='Gets or sets the restore request '
                   'object. Expected value: json-string/@json-file.')

    with self.argument_context('dataprotection backup-instance wait') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', options_list=['--name', '-n', '--backup-instance-name'], type=str,
                   help='The name of the backup instance', id_part='child_name_1')

    with self.argument_context('dataprotection recovery-point list') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', type=str, help='The name of the backup instance')
        c.argument('filter_', options_list=['--filter'], type=str, help='OData filter options.')
        c.argument('skip_token', type=str, help='skipToken Filter.')

    with self.argument_context('dataprotection recovery-point show') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instance_name', type=str, help='The name of the backup instance', id_part='child_name_1')
        c.argument('recovery_point_id', type=str, help='Recovery point id.', id_part='child_name_2')

    with self.argument_context('dataprotection job list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vault_name', type=str, help='The name of the backup vault.')

    with self.argument_context('dataprotection job show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('job_id', type=str, help='The Job ID. This is a GUID-formatted string (e.g. '
                   '00000000-0000-0000-0000-000000000000).', id_part='child_name_1')

    with self.argument_context('dataprotection restorable-time-range find') as c:
        c.argument('vault_name', type=str, help='The name of the backup vault.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('backup_instances', type=str, help='Backup instance name.', id_part='child_name_1')
        c.argument('source_data_store_type', arg_type=get_enum_type(['OperationalStore', 'VaultStore',
                                                                     'ArchiveStore']), help='Specify the '
                                                                                            'source data store.')
        c.argument('start_time', type=str, help='Start time for the List Restore Ranges request')
        c.argument('end_time', type=str, help='End time for the List Restore Ranges request')
