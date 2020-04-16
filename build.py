#!/usr/bin/env python
# -*- coding: utf-8 -*-


#from bincrafters import build_template_default
from bincrafters import build_shared

if __name__ == "__main__":

    #builder = build_template_default.get_builder(shared_option_name=False, pure_c=False)
    builder = build_shared.get_builder()
    builder.add_common_builds(pure_c=False)
    builder.run()
    