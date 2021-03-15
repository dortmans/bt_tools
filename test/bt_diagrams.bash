#!/bin/bash

../scripts/bt2img.py \
	--display \
  --behavior_tree test_bt.xml \
  --image_out test_bt \
  --legend test_bt_legend \

../scripts/bt2img.py \
	--display \
  --behavior_tree generic.xml \
  --image_out generic \
  --legend generic_legend \
