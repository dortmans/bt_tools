#!/bin/bash

../scripts/bt2code.py \
  --behavior_tree no_nodes.xml \
  --code_out no_nodes \

../scripts/bt2code.py \
  --behavior_tree test_bt.xml \
  --code_out test_bt \

../scripts/bt2code.py \
  --behavior_tree generic.xml \
  --code_out generic \

