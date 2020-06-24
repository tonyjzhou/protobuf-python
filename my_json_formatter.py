#!/usr/bin/env python

import sys

from google.protobuf import json_format

import addressbook_pb2

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book1 = addressbook_pb2.AddressBook()

# Read the existing address book.
with open(sys.argv[1], "rb") as f:
    address_book1.ParseFromString(f.read())

json_string = json_format.MessageToJson(address_book1)
print(json_string)

address_book2 = json_format.Parse(json_string, addressbook_pb2.AddressBook())


def write_address_book(output_file, proto_object):
    global f
    with open(output_file, "wb") as f:
        f.write(proto_object.SerializeToString())


write_address_book("address_book1", address_book1)
write_address_book("address_book2", address_book2)
