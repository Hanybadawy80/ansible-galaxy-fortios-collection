#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_switch_controller_snmp_community
short_description: Configure FortiSwitch SNMP v1/v2c communities globally in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify switch_controller feature and snmp_community category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.4.0
version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Jie Xue (@JieX19)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
requirements:
    - ansible>=2.9.0
options:
    host:
        description:
            - FortiOS or FortiGate IP address.
        type: str
        required: false
    username:
        description:
            - FortiOS or FortiGate username.
        type: str
        required: false
    password:
        description:
            - FortiOS or FortiGate password.
        type: str
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS protocol.
        type: bool
        default: true
    ssl_verify:
        description:
            - Ensures FortiGate certificate must be verified by a proper CA.
        type: bool
        default: true
    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    switch_controller_snmp_community:
        description:
            - Configure FortiSwitch SNMP v1/v2c communities globally.
        default: null
        type: dict
        suboptions:
            events:
                description:
                    - SNMP notifications (traps) to send.
                type: str
                choices:
                    - cpu-high
                    - mem-low
                    - log-full
                    - intf-ip
                    - ent-conf-change
            hosts:
                description:
                    - Configure IPv4 SNMP managers (hosts).
                type: list
                suboptions:
                    id:
                        description:
                            - Host entry ID.
                        required: true
                        type: int
                    ip:
                        description:
                            - IPv4 address of the SNMP manager (host).
                        type: str
            id:
                description:
                    - SNMP community ID.
                required: true
                type: int
            name:
                description:
                    - SNMP community name.
                type: str
            query_v1_port:
                description:
                    - SNMP v1 query port .
                type: int
            query_v1_status:
                description:
                    - Enable/disable SNMP v1 queries.
                type: str
                choices:
                    - disable
                    - enable
            query_v2c_port:
                description:
                    - SNMP v2c query port .
                type: int
            query_v2c_status:
                description:
                    - Enable/disable SNMP v2c queries.
                type: str
                choices:
                    - disable
                    - enable
            status:
                description:
                    - Enable/disable this SNMP community.
                type: str
                choices:
                    - disable
                    - enable
            trap_v1_lport:
                description:
                    - SNMP v2c trap local port .
                type: int
            trap_v1_rport:
                description:
                    - SNMP v2c trap remote port .
                type: int
            trap_v1_status:
                description:
                    - Enable/disable SNMP v1 traps.
                type: str
                choices:
                    - disable
                    - enable
            trap_v2c_lport:
                description:
                    - SNMP v2c trap local port .
                type: int
            trap_v2c_rport:
                description:
                    - SNMP v2c trap remote port .
                type: int
            trap_v2c_status:
                description:
                    - Enable/disable SNMP v2c traps.
                type: str
                choices:
                    - disable
                    - enable
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure FortiSwitch SNMP v1/v2c communities globally.
    fortios_switch_controller_snmp_community:
      vdom:  "{{ vdom }}"
      state: "present"
      switch_controller_snmp_community:
        events: "cpu-high"
        hosts:
         -
            id:  "5"
            ip: "<your_own_value>"
        id:  "7"
        name: "default_name_8"
        query_v1_port: "9"
        query_v1_status: "disable"
        query_v2c_port: "11"
        query_v2c_status: "disable"
        status: "disable"
        trap_v1_lport: "14"
        trap_v1_rport: "15"
        trap_v1_status: "disable"
        trap_v2c_lport: "17"
        trap_v2c_rport: "18"
        trap_v2c_status: "disable"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    ssl_verify = data['ssl_verify']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password, verify=ssl_verify)


def filter_switch_controller_snmp_community_data(json):
    option_list = ['events', 'hosts', 'id',
                   'name', 'query_v1_port', 'query_v1_status',
                   'query_v2c_port', 'query_v2c_status', 'status',
                   'trap_v1_lport', 'trap_v1_rport', 'trap_v1_status',
                   'trap_v2c_lport', 'trap_v2c_rport', 'trap_v2c_status']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def switch_controller_snmp_community(data, fos):
    vdom = data['vdom']
    state = data['state']
    switch_controller_snmp_community_data = data['switch_controller_snmp_community']
    filtered_data = underscore_to_hyphen(filter_switch_controller_snmp_community_data(switch_controller_snmp_community_data))

    if state == "present":
        return fos.set('switch-controller',
                       'snmp-community',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('switch-controller',
                          'snmp-community',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_switch_controller(data, fos):

    if data['switch_controller_snmp_community']:
        resp = switch_controller_snmp_community(data, fos)

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    fields = {
        "host": {"required": False, "type": "str"},
        "username": {"required": False, "type": "str"},
        "password": {"required": False, "type": "str", "default": "", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "ssl_verify": {"required": False, "type": "bool", "default": True},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "switch_controller_snmp_community": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "events": {"required": False, "type": "str",
                           "choices": ["cpu-high",
                                       "mem-low",
                                       "log-full",
                                       "intf-ip",
                                       "ent-conf-change"]},
                "hosts": {"required": False, "type": "list",
                          "options": {
                              "id": {"required": True, "type": "int"},
                              "ip": {"required": False, "type": "str"}
                          }},
                "id": {"required": True, "type": "int"},
                "name": {"required": False, "type": "str"},
                "query_v1_port": {"required": False, "type": "int"},
                "query_v1_status": {"required": False, "type": "str",
                                    "choices": ["disable",
                                                "enable"]},
                "query_v2c_port": {"required": False, "type": "int"},
                "query_v2c_status": {"required": False, "type": "str",
                                     "choices": ["disable",
                                                 "enable"]},
                "status": {"required": False, "type": "str",
                           "choices": ["disable",
                                       "enable"]},
                "trap_v1_lport": {"required": False, "type": "int"},
                "trap_v1_rport": {"required": False, "type": "int"},
                "trap_v1_status": {"required": False, "type": "str",
                                   "choices": ["disable",
                                               "enable"]},
                "trap_v2c_lport": {"required": False, "type": "int"},
                "trap_v2c_rport": {"required": False, "type": "int"},
                "trap_v2c_status": {"required": False, "type": "str",
                                    "choices": ["disable",
                                                "enable"]}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    # legacy_mode refers to using fortiosapi instead of HTTPAPI
    legacy_mode = 'host' in module.params and module.params['host'] is not None and \
                  'username' in module.params and module.params['username'] is not None and \
                  'password' in module.params and module.params['password'] is not None

    if not legacy_mode:
        if module._socket_path:
            connection = Connection(module._socket_path)
            fos = FortiOSHandler(connection)

            is_error, has_changed, result = fortios_switch_controller(module.params, fos)
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_switch_controller(module.params, fos)
        fos.logout()

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
