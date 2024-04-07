from models.load_LLaVA import *
import os, sys

from utils.load_data import load_data

# load data
import json
from utils.infer_on_data import *

set_name = "VQAv2"
img_path = "/data3/yue/synthetic_images"
meta_data_path = "/data3/yue/synthetic_data"
output_dir = "/data3/yue/screen_read_output/gpt4v"

# sys.path.append('/data3/yue')

val_data_path,img_prefix = load_data(set_name)
val_data = json.load(open(os.path.join(meta_data_path, val_data_path), 'rb'))

correct, total, acc, single_subimage_correct_ratio, val_data_new = \
    test_each_multipanel(val_data, call_model, img_path + '/' + img_prefix)
print("Correct: ", correct, " Total: ", total, " Accuracy: ", acc)
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "eval_results_" + set_name + "_set.json")
print("Saved to: ",output_file)
json.dump(val_data_new, open(output_file, 'w', encoding="utf8"), indent='\t', separators=(',', ': '))

