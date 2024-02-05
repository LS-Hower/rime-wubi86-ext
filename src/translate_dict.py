# -*- coding: utf-8 -*-

# 2023-06-05  translate_dict.py

import sys
import os
from datetime import datetime

from code_ranges import code_ranges
import dict_parser




head = """# Rime 词典: wubi86.%s
# 编码：utf-8
#
# 作者：

---
name: wubi86.%s
version: "%s"
sort: by_weight
columns:
  - text
  - code
  - weight
encoder:
  exclude_patterns:
    - '^z.*$'
  rules:
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaBaCaCb"
    - length_in_range: [4, 10]
      formula: "AaBaCaZa"
...

"""




if len(sys.argv) != 2 or sys.argv[1] not in code_ranges:
    print("need one command line argument for dictionary name", file=sys.stderr)
    print(f"(one of {code_ranges.keys()})", file=sys.stderr)
    exit(1)

script, dictname = sys.argv

dst_file_name = f"wubi86.{dictname}.dict.yaml"


# 选择是否覆盖
if os.path.exists(dst_file_name):

    print(f"File {dst_file_name} already exists.")
    print("Input 'y' to overwrite it.")
    response = input()

    if response.lower() != 'y':
        print("Stopped.")
        exit(1)

# 读取
start, end, codes = dict_parser.parse(dictname)

with open(dst_file_name, encoding='utf-8', mode='w') as dst:

    # 写入头部的信息
    print(head % (dictname, dictname, datetime.now().strftime("%Y.%m.%d")), end='', file=dst)

    # 写入
    for offset, codelist in enumerate(codes):
        for code in codelist:
            print(f"{chr(start+offset)}\t{code}\t0", file=dst)
