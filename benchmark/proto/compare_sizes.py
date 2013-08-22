#!/usr/bin/env python

from __future__ import division
import sys

import openxc_pb2
import json

def sizeof_fmt(num):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0

total_json_size = 0
total_binary_size = 0

trace_file = sys.argv[1]
for line in open(trace_file):
    raw_message = json.loads(line)
    total_json_size += len(json.dumps(raw_message))
    binary_message = openxc_pb2.RawMessage()
    binary_message.message_id = raw_message['id']
    binary_message.data = int(raw_message['data'], 0)
    total_binary_size += len(binary_message.SerializeToString())

print("For the trace file %s..." % trace_file)
print("Total transferred JSON size is %s" % sizeof_fmt(total_json_size))
print("Total transferred binary size is %s" % sizeof_fmt(total_binary_size))
print("Binary encoding is %f%% smaller than JSON overall" % (
        100 - (total_binary_size / total_json_size * 100)))
