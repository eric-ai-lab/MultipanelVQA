import sys
import argparse

# Manually set the arguments
sys.argv = ['script_name', '--cfg-path', 'eval_configs/minigptv2_eval.yaml']

import os
import re
import json
import argparse
from collections import defaultdict

import numpy as np
from PIL import Image
from tqdm import tqdm
import torch


from minigpt4.datasets.datasets.vqa_datasets import OKVQAEvalData,VizWizEvalData,IconQAEvalData,GQAEvalData,VSREvalData,HMEvalData
from minigpt4.common.vqa_tools.VQA.PythonHelperTools.vqaTools.vqa import VQA
from minigpt4.common.vqa_tools.VQA.PythonEvaluationTools.vqaEvaluation.vqaEval import VQAEval

from minigpt4.common.eval_utils import prepare_texts, init_model, eval_parser
from minigpt4.conversation.conversation import CONV_VISION_minigptv2
from minigpt4.common.config import Config


def list_of_str(arg):
    return list(map(str, arg.split(',')))

parser = eval_parser()

parser.add_argument("--gpu-id", type=int, default=0, help="specify the gpu to load the model.")
parser.add_argument("--f", type=str, default='')
args = parser.parse_args()
cfg = Config(args)

model, vis_processor = init_model(args)
conv_temp = CONV_VISION_minigptv2.copy()
conv_temp.system = ""
model.eval()



def call_model(image_path, questions):
    questions = ['[vqa]'+questions]
    image = Image.open(image_path).convert('RGB')
    image = vis_processor(image)
    texts = prepare_texts(questions, conv_temp)  # warp the texts with conversation template
    with torch.no_grad():
        answers = model.generate(torch.tensor(np.array([image])), texts, max_new_tokens=256, do_sample=False)
        
    return answers[0]
