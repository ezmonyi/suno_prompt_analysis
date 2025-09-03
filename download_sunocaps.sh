#!/bin/bash
curl -L -o ./sunocaps.zip\
  https://www.kaggle.com/api/v1/datasets/download/miguelcivit/sunocaps

curl -L -o suno1m.json\
  https://huggingface.co/datasets/sleeping-ai/SUNO-1M/resolve/main/metadata_uuid.jsonl 