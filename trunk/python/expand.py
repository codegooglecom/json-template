#!/usr/bin/python -S
#
# Copyright (C) 2009 Andy Chu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Expand a JSON template, given a data dictionary.

Usage:
  expand.py 'a is {a}' '{"a": 1}'
"""

__author__ = 'Andy Chu'


import os
import sys

if __name__ == '__main__':
  sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

from pan.core import json
from python import jsontemplate


class UsageError(Exception):
  pass


def main(argv):
  """Returns an exit code."""
  if len(argv) != 2:
    raise UsageError(__doc__)

  template_str = argv[0]
  dictionary = argv[1]
  dictionary = json.loads(dictionary)
  t = jsontemplate.FromString(template_str)
  sys.stdout.write(t.expand(dictionary))
  return 0


if __name__ == '__main__':
  try:
    sys.exit(main(sys.argv[1:]))
  except UsageError, e:
    print >> sys.stderr, e.args[0]
    sys.exit(1)
