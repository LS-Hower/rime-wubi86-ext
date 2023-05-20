#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从 multicode.txt 读取内容，转储成 JSON
# multicode.txt 的形式是这样的：
'''
wubi86.exte.dict.yaml

𬅊	svmw	swfw
𬅲	fqkw	fwkw
𬅵	vuhw	qguw	wfuw

wubi86.extf.dict.yaml

𬻉	gnft	ynft	gvhf	yvhf	gntf	yntf
𬻞	mggg	mngg
𬻟	fkgo	dkoi	gkug
'''


import json
import datetime


IN_FILE_NAME = "multicode.txt"
OUT_FILE_NAME = "multicode.json"

file_data = {
    'name': OUT_FILE_NAME,
    'version': datetime.datetime.now().strftime("%Y.%m.%d"),
    'multicode': {},
}

with open(IN_FILE_NAME, encoding='utf-8', mode='r') as in_file:

    while line := in_file.readline():

        strs = line.split()
        strs_cnt = len(strs)

        if strs_cnt == 0:
            # 是空行
            pass
        elif strs_cnt == 1:
            # 是标明码表文件名的行
            curr_fname = strs[0]
            file_data['multicode'][curr_fname] = {}
        else:
            # 是写着字和多码的行
            file_data['multicode'][curr_fname][strs[0]] = strs[1:]

with open(OUT_FILE_NAME, encoding='utf-8', mode='w') as out_file:
    json.dump(file_data, out_file,
              indent='\t', ensure_ascii=False, sort_keys=False)
