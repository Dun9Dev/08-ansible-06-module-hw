#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a file on remote host with specified content

version_added: "1.0.0"

description:
    - This module creates a text file on the remote host at specified path with specified content.

options:
    path:
        description: Path to the file to create.
        required: true
        type: str
    content:
        description: Content to write to the file.
        required: true
        type: str

author:
    - Your Name (@Dun9Dev)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/test.txt
    content: "Hello, World!"
'''

RETURN = r'''
path:
    description: Path to the created file.
    type: str
    returned: always
content:
    description: Content written to the file.
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    
    # Check if file exists and has the same content
    file_exists = os.path.exists(path)
    file_content_matches = False
    
    if file_exists:
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
                if existing_content == content:
                    file_content_matches = True
        except:
            pass

    result['path'] = path
    result['content'] = content

    if module.check_mode:
        module.exit_json(**result)

    if not file_exists or not file_content_matches:
        try:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {str(e)}", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
