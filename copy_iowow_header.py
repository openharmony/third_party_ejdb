#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import argparse
import os
import shutil

def copy_file(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    headers = [
        'basedefs.h',
        'fs/iwdlsnr.h',
        'fs/iwexfile.h',
        'fs/iwfile.h',
        'fs/iwfsmfile.h',
        'iowow.h',
        'json/iwbinn.h',
        'json/iwjson_internal.h',
        'json/iwjson.h',
        'kv/iwkv.h',
        'log/iwlog.h',
        'platform/iwp.h',
        'rdb/iwrdb.h',
        're/iwre.h',
        'tmpl/iwcfg.h',
        'utils/iwarr.h',
        'utils/iwbits.h',
        'utils/iwconv.h',
        'utils/iwhmap.h',
        'utils/iwpool.h',
        'utils/iwstw.h',
        'utils/iwth.h',
        'utils/iwutils.h',
        'utils/iwuuid.h',
        'utils/iwxstr.h',
        'utils/murmur3.h',
        'utils/utf8proc.h',
    ]
    for header in headers:
        src_file = os.path.join(src_dir, header)
        file_tags = header.split('/')
        if (len(file_tags) == 1):
            des_file = os.path.join(dst_dir, header)
        else:
            des_file = os.path.join(dst_dir, file_tags[len(file_tags) - 1])
        shutil.copy2(src_file, des_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-dir', help='source path of iowow header file', required=True)
    parser.add_argument('--dst-dir', help='destion path of iowow header file', required=True)
    args = parser.parse_args()
    print('copy from %s to %s', args.src_dir, args.dst_dir)
    copy_file(args.src_dir, args.dst_dir)
    return 0

if __name__ == '__main__':
    sys.exit(main())
