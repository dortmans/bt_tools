#!/usr/bin/python3
#
# Copyright (c) 2021 Eric Dortmans
#
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

# This tool converts a behavior tree XML file to a PNG image. Run bt2img.py -h
# for instructions

import argparse
import xml.etree.ElementTree

skip_nodes = [
    'Wait',
    'AlwaysRunning'
]


def main():
    args = parse_command_line()
    print("\nXML BT file: {file}".format(file=args.behavior_tree))
    xml_tree = xml.etree.ElementTree.parse(args.behavior_tree)
    tree_nodes_model = find_tree_nodes_model(xml_tree)
    generate_code(tree_nodes_model)


def parse_command_line():
    parser = argparse.ArgumentParser(
        description='Convert a behavior tree XML file to an image')
    parser.add_argument('--behavior_tree', required=True,
                        help='the behavior tree XML file to parse')
    parser.add_argument('--code_out', required=True,
                        help='The name of the output code file.')

    return parser.parse_args()


def find_tree_nodes_model(xml_tree):
    tree_nodes_model = xml_tree.find('TreeNodesModel')
    return tree_nodes_model


def generate_code(tree_nodes_model):
    # for node in tree_nodes_model:
    #     id = node.get('ID')
    #     tag = node.tag
    #     if id in skip_nodes:
    #         pass
    #     if tag == 'SubTree':
    #         pass
    #     if tag == 'Condition':
    #         print("Condition({id})".format(id=id))
    #     if tag == 'Action':
    #         print("Action({id})".format(id=id))
    conditions = tree_nodes_model.findall('Condition')
    actions = tree_nodes_model.findall('Action')
    for condition in conditions:
        id = condition.get('ID')
        if id in skip_nodes:
             continue
        print("Condition({id})".format(id=id))
    for action in actions:
        id = action.get('ID')
        if id in skip_nodes:
             continue
        print("Action({id})".format(id=id))


if __name__ == '__main__':
    main()
