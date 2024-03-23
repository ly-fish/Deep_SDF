#! /usr/bin/bash

python preprocess_data.py --data_dir data \
--source [...]/ShapeNetCore.v2/ \
--name ShapeNetV2 \
--split examples/splits/sv2_sofas_train.json \
--skip