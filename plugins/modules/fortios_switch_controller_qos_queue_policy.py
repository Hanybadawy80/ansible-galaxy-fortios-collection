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
module: fortios_switch_controller_qos_queue_policy
short_description: Configure FortiSwitch QoS egress queue policy in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify switch_controller_qos feature and queue_policy category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.2.0
version_added: "2.9"
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
    switch_controller_qos_queue_policy:
        description:
            - Configure FortiSwitch QoS egress queue policy.
        default: null
        type: dict
        suboptions:
            cos_queue:
                description:
                    - COS queue configuration.
                type: list
                suboptions:
                    description:
                        description:
                            - Description of the COS queue.
                        type: str
                    drop_policy:
                        description:
                            - COS queue drop policy.
                        type: str
                        choices:
                            - taildrop
                            - weighted-random-early-detection
                    max_rate:
                        description:
                            - Maximum rate (0 - 4294967295 kbps, 0 to disable).
                        type: int
                    max_rate_percent:
                        description:
                            - Maximum rate (% of link speed).
                        type: int
                    min_rate:
                        description:
                            - Minimum rate (0 - 4294967295 kbps, 0 to disable).
                        type: int
                    min_rate_percent:
                        description:
                            - Minimum rate (% of link speed).
                        type: int
                    name:
                        description:
                            - Cos queue ID.
                        required: true
                        type: str
                    weight:
                        description:
                            - Weight of weighted round robin scheduling.
                        type: int
            name:
                description:
                    - QoS policy name
                required: true
                type: str
            rate_by:
                description:
                    - COS queue rate by kbps or percent.
                type: str
                choices:
                    - kbps
                    - percent
            schedule:
                description:
                    - COS queue scheduling.
                type: str
                choices:
                    - strict
                    - round-robin
                    - weighted
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
  - name: Configure FortiSwitch QoS egress queue policy.
    fortios_switch_controller_qos_queue_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      switch_controller_qos_queue_policy:
        cos_queue:
         -
            description: "<your_own_value>"
            drop_policy: "taildrop"
            max_rate: "6"
            max_rate_percent: "7"
            min_rate: "8"
            min_rate_percent: "9"
            name: "default_name_10"
            weight: "11"
        name: "default_name_12"
        rate_by: "kbps"
        schedule: "strict"
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


def filter_switch_controller_qos_queue_policy_data(json):
    option_list = ['cos_queue', 'name', 'rate_by',
                   'schedule']
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


def switch_controller_qos_queue_policy(data, fos):
    vdom = data['vdom']
    state = data['state']
    switch_controller_qos_queue_policy_data = data['switch_controller_qos_queue_policy']
    filtered_data = underscore_to_hyphen(filter_switch_controller_qos_queue_policy_data(switch_controller_qos_queue_policy_data))

    if state == "present":
        return fos.set('switch-controller.qos',
                       'queue-policy',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('switch-controller.qos',
                          'queue-policy',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_switch_controller_qos(data, fos):

    if data['switch_controller_qos_queue_policy']:
        resp = switch_controller_qos_queue_policy(data, fos)

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
        "switch_controller_qos_queue_policy": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "cos_queue": {"required": False, "type": "list",
                              "options": {
                                  "description": {"required": False, "type": "str"},
                                  "drop_policy": {"required": False, "type": "str",
                                                  "choices": ["taildrop",
                                                              "weighted-random-early-detection"]},
                                  "max_rate": {"required": False, "type": "int"},
                                  "max_rate_percent": {"required": False, "type": "int"},
                                  "min_rate": {"required": False, "type": "int"},
                                  "min_rate_percent": {"required": False, "type": "int"},
                                  "name": {"required": True, "type": "str"},
                                  "weight": {"required": False, "type": "int"}
                              }},
                "name": {"required": True, "type": "str"},
                "rate_by": {"required": False, "type": "str",
                            "choices": ["kbps",
                                        "percent"]},
                "schedule": {"required": False, "type": "str",
                             "choices": ["strict",
                                         "round-robin",
                                         "weighted"]}

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

            is_error, has_changed, result = fortios_switch_controller_qos(module.params, fos)
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_switch_controller_qos(module.params, fos)
        fos.logout()

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
