#!/usr/bin/env python
import json
import sys
from library.my_own_module import main

# Эмулируем вызов модуля через Ansible
if __name__ == '__main__':
    # Параметры для модуля
    params = {
        'ANSIBLE_MODULE_ARGS': {
            'path': '/tmp/test_file.txt',
            'content': 'Hello from my module!'
        }
    }
    sys.stdin = open('/dev/null', 'r')
    sys.argv = ['', json.dumps(params)]
    main()
