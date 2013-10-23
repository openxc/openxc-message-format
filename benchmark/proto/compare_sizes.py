#!/usr/bin/env python

from __future__ import division
import sys
import numbers

import openxc_pb2
import json

def sizeof_fmt(num):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0

total_raw_can_size = 0
total_raw_json_size = 0
total_raw_binary_size = 0
total_translated_json_size = 0
total_translated_binary_size = 0

for trace_file in sys.argv[1:]:
    for line in open(trace_file):
        try:
            json_message = json.loads(line)
        except ValueError:
            continue

        del json_message['timestamp']

        message = openxc_pb2.VehicleMessage()

        if 'id' and 'data' in json_message:
            # rough approx. that CAN messages are 10 bytes - they could be less
            # but most of ours are full 64+11 bits
            total_raw_can_size += 10
            total_raw_json_size += len(json.dumps(json_message))
            message.type = openxc_pb2.VehicleMessage.RAW
            message.raw_message.message_id = json_message['id']
            message.raw_message.data = int(json_message['data'], 0)
            total_raw_binary_size += len(message.SerializeToString())
        else:
            if 'event' in json_message:
                if isinstance(json_message['event'], bool):
                    message.type = openxc_pb2.VehicleMessage.EVENTED_BOOL
                    message.evented_boolean_message.name = json_message['name']
                    message.evented_boolean_message.value = json_message['value']
                    message.evented_boolean_message.event = json_message['event']
                elif isinstance(json_message['event'], numbers.Number):
                    message.type = openxc_pb2.VehicleMessage.EVENTED_NUM
                    message.evented_numeric_message.name = json_message['name']
                    message.evented_numeric_message.value = json_message['value']
                    message.evented_numeric_message.event = json_message['event']
                else:
                    message.type = openxc_pb2.VehicleMessage.EVENTED_STRING
                    message.evented_string_message.name = json_message['name']
                    message.evented_string_message.value = json_message['value']
                    message.evented_numeric_message.event = json_message['event']
            else:
                if isinstance(json_message['value'], bool):
                    message.type = openxc_pb2.VehicleMessage.BOOL
                    message.boolean_message.name = json_message['name']
                    message.boolean_message.value = json_message['value']
                elif isinstance(json_message['value'], numbers.Number):
                    message.type = openxc_pb2.VehicleMessage.NUM
                    message.numeric_message.name = json_message['name']
                    message.numeric_message.value = json_message['value']
                else:
                    message.type = openxc_pb2.VehicleMessage.STRING
                    message.string_message.name = json_message['name']
                    message.string_message.value = json_message['value']
            total_translated_json_size += len(json.dumps(json_message))
            total_translated_binary_size += len(message.SerializeToString())


print("For the %d trace files given..." % len(sys.argv[1:]))
print("Total transferred raw CAN size is %s" % sizeof_fmt(total_raw_can_size))
print("Total transferred raw JSON size is %s" % sizeof_fmt(total_raw_json_size))
print("Total transferred raw binary size is %s" % sizeof_fmt(total_raw_binary_size))
print("Total transferred translated JSON size is %s" %
        sizeof_fmt(total_translated_json_size))
print("Total transferred translated binary size is %s" %
        sizeof_fmt(total_translated_binary_size))

total_json_size = total_raw_json_size + total_translated_json_size
print("Total transferred JSON size is %s" % sizeof_fmt(total_json_size))
total_binary_size = total_raw_binary_size + total_translated_binary_size
print("Total transferred binary size is %s" % sizeof_fmt(total_binary_size))

if total_raw_can_size > 0:
    print("Binary encoding adds %f%% overhead to raw CAN messages" % (
            total_raw_binary_size / total_raw_can_size * 100 - 100))
    print("JSON encoding adds %f%% overhead to raw CAN messages" % (
            total_raw_json_size / total_raw_can_size * 100 - 100))
if total_raw_json_size > 0:
    print("Binary encoding is %f%% smaller than JSON for raw messages" % (
            100 - (total_raw_binary_size / total_raw_json_size * 100)))
if total_translated_json_size > 0:
    print("Binary encoding is %f%% smaller than JSON for translated messages" % (
            100 - (total_translated_binary_size / total_translated_json_size * 100)))
print("Binary encoding is %f%% smaller than JSON overall" % (
        100 - (total_binary_size / total_json_size * 100)))
