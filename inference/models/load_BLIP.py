import torch
from lavis.models import load_model_and_preprocess
from PIL import Image
import argparse
model_type = "6"#  choices=["1", "2", "3", "4"])

device = 'cuda:0'

if model_type == '1':
    model_type = "pretrain_flant5xl"
    name = "blip2_t5"
elif model_type == '2':
    model_type = "vicuna7b"
    name = "blip2_vicuna_instruct"
elif model_type == '5':
    model_type = "flant5xl"
    name = "blip2_t5_instruct"
elif model_type == '6': 
    model_type = "flant5xxl"
    name = "blip2_t5_instruct"
print("model_type", model_type)
print("name", name)
model, vis_processors, _ = load_model_and_preprocess(name=name, model_type=model_type, is_eval=True, device=device)
    
def call_model(image_file, prompt):
    # prepare the image
    raw_image = Image.open(image_file).convert("RGB")
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    answer = model.generate({"image": image, "prompt": prompt})[0]
    
    return answer
