#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import json

lang = "syntaxes/gstlaunch.tmLanguage.json"
elements="elements"

with open(elements) as fp:
    join_elements = " | ".join(
        element.strip()
        for element in 
        fp.read().split("\n")
    )

with open(lang, "r") as fp:
    lang_data = json.load(fp)

ref = "(?x)\n  (?<!\\.) \\b(\n  {}  \n  )\\b\n"
lang_data["repository"]["element"]["patterns"][0]["match"] = ref.format(join_elements)

with open(lang, "w") as fp:
    json.dump(lang_data, fp, indent=2)
