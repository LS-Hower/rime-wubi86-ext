# -*- coding: utf-8 -*-

# 2023-06-05  dict_parser.py

from code_ranges import code_ranges
import re
import sys



line_form = re.compile("((.(\t[a-y]{3,4})+\n?)|(#.*))?")
dictnames = code_ranges.keys()

def prefix_u(codepoint: int) -> str:

    """将码点转换成 U+XXXX 的形式."""

    return "U+%.4X" % codepoint




def parse(dictname: str) -> dict[str, list[str]]:

    """接受词典名称 (类似于 "extc");
    读取 .txt 文件;
    返回从单字映射到五笔码 (列表) 的 dict.
    """

    if dictname not in dictnames:
        print(f"dictionary name '{dictname}' is not valid;", file=sys.stderr)
        print(f"must be one of {dictnames}", file=sys.stderr)
        exit(1)

    retdict = {}
    expected_codepoint = code_ranges[dictname][0]
    max_codepoint = code_ranges[dictname][1]
    line_number = 0

    with open(f"{dictname}.txt", encoding='utf-8', mode='r') as src:

        while ln := src.readline():

            line_number += 1

            if not line_form.match(ln):
                print(f"invalid form at line {line_number}", file=sys.stderr)
                print(f"\"{ln}\"", file=sys.stderr)
                exit(1)

            ln = ln.strip()

            # 忽略空行和以井号开头的行
            if ln[0] == '#' or not ln:
                continue

            codepoint = ord(ln[0])

            if codepoint > max_codepoint:
                print(f"wrong character {prefix_u(codepoint)} at line {line_number}", file=sys.stderr)
                print(f"\"{ln}\"", file=sys.stderr)
                print(f"max codepoint of {dictname} is {prefix_u(max_codepoint)}", file=sys.stderr)
                exit(1)

            if codepoint != expected_codepoint:
                print(f"wrong character {prefix_u(codepoint)} at line {line_number}", file=sys.stderr)
                print(f"\"{ln}\"", file=sys.stderr)
                print(f"should be {prefix_u(expected_codepoint)}", file=sys.stderr)
                exit(1)

            parts = ln.split("\t")
            character = parts[0]
            codes = parts[1:]

            if len(codes) > 1 and len(codes) != len(set(codes)):
                print(f"duplicate code at line {line_number}", file=sys.stderr)
                print(f"\"{ln}\"", file=sys.stderr)
                exit(1)

            retdict[character] = codes
            expected_codepoint += 1

        # 检查最后一个字的码点
        if expected_codepoint - 1 != max_codepoint:
            print(f"incomplete file content, stopped at {prefix_u(codepoint)}", file=sys.stderr)
            print(f"\"{ln}\"", file=sys.stderr)
            print(f"max codepoint of {dictname} should be {prefix_u(max_codepoint)}", file=sys.stderr)
            exit(1)

    return retdict







