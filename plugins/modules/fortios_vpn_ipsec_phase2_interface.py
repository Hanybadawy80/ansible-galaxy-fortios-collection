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
module: fortios_vpn_ipsec_phase2_interface
short_description: Configure VPN autokey tunnel in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify vpn_ipsec feature and phase2_interface category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.2.0
version_added: "2.8"
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
        version_added: 2.9
    state:
        description:
            - Indicates whether to create or remove the object.
              This attribute was present already in previous version in a deeper level.
              It has been moved out to this outer level.
        type: str
        required: false
        choices:
            - present
            - absent
        version_added: 2.9
    vpn_ipsec_phase2_interface:
        description:
            - Configure VPN autokey tunnel.
        default: null
        type: dict
        suboptions:
            state:
                description:
                    - B(Deprecated)
                    - Starting with Ansible 2.9 we recommend using the top-level 'state' parameter.
                    - HORIZONTALLINE
                    - Indicates whether to create or remove the object.
                type: str
                required: false
                choices:
                    - present
                    - absent
            add_route:
                description:
                    - Enable/disable automatic route addition.
                type: str
                choices:
                    - phase1
                    - enable
                    - disable
            auto_discovery_forwarder:
                description:
                    - Enable/disable forwarding short-cut messages.
                type: str
                choices:
                    - phase1
                    - enable
                    - disable
            auto_discovery_sender:
                description:
                    - Enable/disable sending short-cut messages.
                type: str
                choices:
                    - phase1
                    - enable
                    - disable
            auto_negotiate:
                description:
                    - Enable/disable IPsec SA auto-negotiation.
                type: str
                choices:
                    - enable
                    - disable
            comments:
                description:
                    - Comment.
                type: str
            dhcp_ipsec:
                description:
                    - Enable/disable DHCP-IPsec.
                type: str
                choices:
                    - enable
                    - disable
            dhgrp:
                description:
                    - Phase2 DH group.
                type: str
                choices:
                    - 1
                    - 2
                    - 5
                    - 14
                    - 15
                    - 16
                    - 17
                    - 18
                    - 19
                    - 20
                    - 21
                    - 27
                    - 28
                    - 29
                    - 30
                    - 31
                    - 32
            dst_addr_type:
                description:
                    - Remote proxy ID type.
                type: str
                choices:
                    - subnet
                    - range
                    - ip
                    - name
                    - subnet6
                    - range6
                    - ip6
                    - name6
            dst_end_ip:
                description:
                    - Remote proxy ID IPv4 end.
                type: str
            dst_end_ip6:
                description:
                    - Remote proxy ID IPv6 end.
                type: str
            dst_name:
                description:
                    - Remote proxy ID name. Source firewall.address.name firewall.addrgrp.name.
                type: str
            dst_name6:
                description:
                    - Remote proxy ID name. Source firewall.address6.name firewall.addrgrp6.name.
                type: str
            dst_port:
                description:
                    - Quick mode destination port (1 - 65535 or 0 for all).
                type: int
            dst_start_ip:
                description:
                    - Remote proxy ID IPv4 start.
                type: str
            dst_start_ip6:
                description:
                    - Remote proxy ID IPv6 start.
                type: str
            dst_subnet:
                description:
                    - Remote proxy ID IPv4 subnet.
                type: str
            dst_subnet6:
                description:
                    - Remote proxy ID IPv6 subnet.
                type: str
            encapsulation:
                description:
                    - ESP encapsulation mode.
                type: str
                choices:
                    - tunnel-mode
                    - transport-mode
            ipv4_df:
                description:
                    - Enable/disable setting and resetting of IPv4 "Don"t Fragment" bit.
                type: str
                choices:
                    - enable
                    - disable
            keepalive:
                description:
                    - Enable/disable keep alive.
                type: str
                choices:
                    - enable
                    - disable
            keylife_type:
                description:
                    - Keylife type.
                type: str
                choices:
                    - seconds
                    - kbs
                    - both
            keylifekbs:
                description:
                    - Phase2 key life in number of bytes of traffic (5120 - 4294967295).
                type: int
            keylifeseconds:
                description:
                    - Phase2 key life in time in seconds (120 - 172800).
                type: int
            l2tp:
                description:
                    - Enable/disable L2TP over IPsec.
                type: str
                choices:
                    - enable
                    - disable
            name:
                description:
                    - IPsec tunnel name.
                required: true
                type: str
            pfs:
                description:
                    - Enable/disable PFS feature.
                type: str
                choices:
                    - enable
                    - disable
            phase1name:
                description:
                    - Phase 1 determines the options required for phase 2. Source vpn.ipsec.phase1-interface.name.
                type: str
            proposal:
                description:
                    - Phase2 proposal.
                type: list
                choices:
                    - null-md5
                    - null-sha1
                    - null-sha256
                    - null-sha384
                    - null-sha512
                    - des-null
                    - des-md5
                    - des-sha1
                    - des-sha256
                    - des-sha384
                    - des-sha512
                    - 3des-null
                    - 3des-md5
                    - 3des-sha1
                    - 3des-sha256
                    - 3des-sha384
                    - 3des-sha512
                    - aes128-null
                    - aes128-md5
                    - aes128-sha1
                    - aes128-sha256
                    - aes128-sha384
                    - aes128-sha512
                    - aes128gcm
                    - aes192-null
                    - aes192-md5
                    - aes192-sha1
                    - aes192-sha256
                    - aes192-sha384
                    - aes192-sha512
                    - aes256-null
                    - aes256-md5
                    - aes256-sha1
                    - aes256-sha256
                    - aes256-sha384
                    - aes256-sha512
                    - aes256gcm
                    - chacha20poly1305
                    - aria128-null
                    - aria128-md5
                    - aria128-sha1
                    - aria128-sha256
                    - aria128-sha384
                    - aria128-sha512
                    - aria192-null
                    - aria192-md5
                    - aria192-sha1
                    - aria192-sha256
                    - aria192-sha384
                    - aria192-sha512
                    - aria256-null
                    - aria256-md5
                    - aria256-sha1
                    - aria256-sha256
                    - aria256-sha384
                    - aria256-sha512
                    - seed-null
                    - seed-md5
                    - seed-sha1
                    - seed-sha256
                    - seed-sha384
                    - seed-sha512
            protocol:
                description:
                    - Quick mode protocol selector (1 - 255 or 0 for all).
                type: int
            replay:
                description:
                    - Enable/disable replay detection.
                type: str
                choices:
                    - enable
                    - disable
            route_overlap:
                description:
                    - Action for overlapping routes.
                type: str
                choices:
                    - use-old
                    - use-new
                    - allow
            single_source:
                description:
                    - Enable/disable single source IP restriction.
                type: str
                choices:
                    - enable
                    - disable
            src_addr_type:
                description:
                    - Local proxy ID type.
                type: str
                choices:
                    - subnet
                    - range
                    - ip
                    - name
                    - subnet6
                    - range6
                    - ip6
                    - name6
            src_end_ip:
                description:
                    - Local proxy ID end.
                type: str
            src_end_ip6:
                description:
                    - Local proxy ID IPv6 end.
                type: str
            src_name:
                description:
                    - Local proxy ID name. Source firewall.address.name firewall.addrgrp.name.
                type: str
            src_name6:
                description:
                    - Local proxy ID name. Source firewall.address6.name firewall.addrgrp6.name.
                type: str
            src_port:
                description:
                    - Quick mode source port (1 - 65535 or 0 for all).
                type: int
            src_start_ip:
                description:
                    - Local proxy ID start.
                type: str
            src_start_ip6:
                description:
                    - Local proxy ID IPv6 start.
                type: str
            src_subnet:
                description:
                    - Local proxy ID subnet.
                type: str
            src_subnet6:
                description:
                    - Local proxy ID IPv6 subnet.
                type: str
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
  - name: Configure VPN autokey tunnel.
    fortios_vpn_ipsec_phase2_interface:
      vdom:  "{{ vdom }}"
      state: "present"
      vpn_ipsec_phase2_interface:
        add_route: "phase1"
        auto_discovery_forwarder: "phase1"
        auto_discovery_sender: "phase1"
        auto_negotiate: "enable"
        comments: "<your_own_value>"
        dhcp_ipsec: "enable"
        dhgrp: "1"
        dst_addr_type: "subnet"
        dst_end_ip: "<your_own_value>"
        dst_end_ip6: "<your_own_value>"
        dst_name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        dst_name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        dst_port: "15"
        dst_start_ip: "<your_own_value>"
        dst_start_ip6: "<your_own_value>"
        dst_subnet: "<your_own_value>"
        dst_subnet6: "<your_own_value>"
        encapsulation: "tunnel-mode"
        ipv4_df: "enable"
        keepalive: "enable"
        keylife_type: "seconds"
        keylifekbs: "24"
        keylifeseconds: "25"
        l2tp: "enable"
        name: "default_name_27"
        pfs: "enable"
        phase1name: "<your_own_value> (source vpn.ipsec.phase1-interface.name)"
        proposal: "null-md5"
        protocol: "31"
        replay: "enable"
        route_overlap: "use-old"
        single_source: "enable"
        src_addr_type: "subnet"
        src_end_ip: "<your_own_value>"
        src_end_ip6: "<your_own_value>"
        src_name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        src_name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        src_port: "40"
        src_start_ip: "<your_own_value>"
        src_start_ip6: "<your_own_value>"
        src_subnet: "<your_own_value>"
        src_subnet6: "<your_own_value>"
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


def filter_vpn_ipsec_phase2_interface_data(json):
    option_list = ['add_route', 'auto_discovery_forwarder', 'auto_discovery_sender',
                   'auto_negotiate', 'comments', 'dhcp_ipsec',
                   'dhgrp', 'dst_addr_type', 'dst_end_ip',
                   'dst_end_ip6', 'dst_name', 'dst_name6',
                   'dst_port', 'dst_start_ip', 'dst_start_ip6',
                   'dst_subnet', 'dst_subnet6', 'encapsulation',
                   'ipv4_df', 'keepalive', 'keylife_type',
                   'keylifekbs', 'keylifeseconds', 'l2tp',
                   'name', 'pfs', 'phase1name',
                   'proposal', 'protocol', 'replay',
                   'route_overlap', 'single_source', 'src_addr_type',
                   'src_end_ip', 'src_end_ip6', 'src_name',
                   'src_name6', 'src_port', 'src_start_ip',
                   'src_start_ip6', 'src_subnet', 'src_subnet6']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_multilists_attributes(data):
    multilist_attrs = [[u'proposal']]

    for attr in multilist_attrs:
        try:
            path = "data['" + "']['".join(elem for elem in attr) + "']"
            current_val = eval(path)
            flattened_val = ' '.join(elem for elem in current_val)
            exec(path + '= flattened_val')
        except BaseException:
            pass

    return data


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


def vpn_ipsec_phase2_interface(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['vpn_ipsec_phase2_interface'] and data['vpn_ipsec_phase2_interface']['state']:
        state = data['vpn_ipsec_phase2_interface']['state']
    else:
        state = True
    vpn_ipsec_phase2_interface_data = data['vpn_ipsec_phase2_interface']
    vpn_ipsec_phase2_interface_data = flatten_multilists_attributes(vpn_ipsec_phase2_interface_data)
    filtered_data = underscore_to_hyphen(filter_vpn_ipsec_phase2_interface_data(vpn_ipsec_phase2_interface_data))

    if state == "present":
        return fos.set('vpn.ipsec',
                       'phase2-interface',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('vpn.ipsec',
                          'phase2-interface',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_vpn_ipsec(data, fos):

    if data['vpn_ipsec_phase2_interface']:
        resp = vpn_ipsec_phase2_interface(data, fos)

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
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "vpn_ipsec_phase2_interface": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "add_route": {"required": False, "type": "str",
                              "choices": ["phase1",
                                          "enable",
                                          "disable"]},
                "auto_discovery_forwarder": {"required": False, "type": "str",
                                             "choices": ["phase1",
                                                         "enable",
                                                         "disable"]},
                "auto_discovery_sender": {"required": False, "type": "str",
                                          "choices": ["phase1",
                                                      "enable",
                                                      "disable"]},
                "auto_negotiate": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "comments": {"required": False, "type": "str"},
                "dhcp_ipsec": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "dhgrp": {"required": False, "type": "str",
                          "choices": ["1",
                                      "2",
                                      "5",
                                      "14",
                                      "15",
                                      "16",
                                      "17",
                                      "18",
                                      "19",
                                      "20",
                                      "21",
                                      "27",
                                      "28",
                                      "29",
                                      "30",
                                      "31",
                                      "32"]},
                "dst_addr_type": {"required": False, "type": "str",
                                  "choices": ["subnet",
                                              "range",
                                              "ip",
                                              "name",
                                              "subnet6",
                                              "range6",
                                              "ip6",
                                              "name6"]},
                "dst_end_ip": {"required": False, "type": "str"},
                "dst_end_ip6": {"required": False, "type": "str"},
                "dst_name": {"required": False, "type": "str"},
                "dst_name6": {"required": False, "type": "str"},
                "dst_port": {"required": False, "type": "int"},
                "dst_start_ip": {"required": False, "type": "str"},
                "dst_start_ip6": {"required": False, "type": "str"},
                "dst_subnet": {"required": False, "type": "str"},
                "dst_subnet6": {"required": False, "type": "str"},
                "encapsulation": {"required": False, "type": "str",
                                  "choices": ["tunnel-mode",
                                              "transport-mode"]},
                "ipv4_df": {"required": False, "type": "str",
                            "choices": ["enable",
                                        "disable"]},
                "keepalive": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "keylife_type": {"required": False, "type": "str",
                                 "choices": ["seconds",
                                             "kbs",
                                             "both"]},
                "keylifekbs": {"required": False, "type": "int"},
                "keylifeseconds": {"required": False, "type": "int"},
                "l2tp": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "name": {"required": True, "type": "str"},
                "pfs": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "phase1name": {"required": False, "type": "str"},
                "proposal": {"required": False, "type": "list",
                             "choices": ["null-md5",
                                         "null-sha1",
                                         "null-sha256",
                                         "null-sha384",
                                         "null-sha512",
                                         "des-null",
                                         "des-md5",
                                         "des-sha1",
                                         "des-sha256",
                                         "des-sha384",
                                         "des-sha512",
                                         "3des-null",
                                         "3des-md5",
                                         "3des-sha1",
                                         "3des-sha256",
                                         "3des-sha384",
                                         "3des-sha512",
                                         "aes128-null",
                                         "aes128-md5",
                                         "aes128-sha1",
                                         "aes128-sha256",
                                         "aes128-sha384",
                                         "aes128-sha512",
                                         "aes128gcm",
                                         "aes192-null",
                                         "aes192-md5",
                                         "aes192-sha1",
                                         "aes192-sha256",
                                         "aes192-sha384",
                                         "aes192-sha512",
                                         "aes256-null",
                                         "aes256-md5",
                                         "aes256-sha1",
                                         "aes256-sha256",
                                         "aes256-sha384",
                                         "aes256-sha512",
                                         "aes256gcm",
                                         "chacha20poly1305",
                                         "aria128-null",
                                         "aria128-md5",
                                         "aria128-sha1",
                                         "aria128-sha256",
                                         "aria128-sha384",
                                         "aria128-sha512",
                                         "aria192-null",
                                         "aria192-md5",
                                         "aria192-sha1",
                                         "aria192-sha256",
                                         "aria192-sha384",
                                         "aria192-sha512",
                                         "aria256-null",
                                         "aria256-md5",
                                         "aria256-sha1",
                                         "aria256-sha256",
                                         "aria256-sha384",
                                         "aria256-sha512",
                                         "seed-null",
                                         "seed-md5",
                                         "seed-sha1",
                                         "seed-sha256",
                                         "seed-sha384",
                                         "seed-sha512"]},
                "protocol": {"required": False, "type": "int"},
                "replay": {"required": False, "type": "str",
                           "choices": ["enable",
                                       "disable"]},
                "route_overlap": {"required": False, "type": "str",
                                  "choices": ["use-old",
                                              "use-new",
                                              "allow"]},
                "single_source": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "src_addr_type": {"required": False, "type": "str",
                                  "choices": ["subnet",
                                              "range",
                                              "ip",
                                              "name",
                                              "subnet6",
                                              "range6",
                                              "ip6",
                                              "name6"]},
                "src_end_ip": {"required": False, "type": "str"},
                "src_end_ip6": {"required": False, "type": "str"},
                "src_name": {"required": False, "type": "str"},
                "src_name6": {"required": False, "type": "str"},
                "src_port": {"required": False, "type": "int"},
                "src_start_ip": {"required": False, "type": "str"},
                "src_start_ip6": {"required": False, "type": "str"},
                "src_subnet": {"required": False, "type": "str"},
                "src_subnet6": {"required": False, "type": "str"}

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

            is_error, has_changed, result = fortios_vpn_ipsec(module.params, fos)
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_vpn_ipsec(module.params, fos)
        fos.logout()

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
