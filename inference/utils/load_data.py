# load data
import json

def load_data(set_name):

    if set_name == 'MegicBrush':
        val_data_path = 'meta_data_MegicBrush.json'
        img_prefix = 'magicbrush__'
    elif set_name == 'VQAv2':
        val_data_path = 'meta_data_VQAv2.json'
        img_prefix = 'VQA__'
    elif set_name == 'MegicBrush_enlarged':
        val_data_path = 'meta_data_MegicBrush.json'
        img_prefix = 'magicbrush_enlarged_images_'
    elif set_name == 'VQAv2_enlarged':
        val_data_path = 'meta_data_VQAv2.json'
        img_prefix = 'VQA_enlarged_images_'
    elif set_name == 'MegicBrush_with_background':
        val_data_path = 'meta_data_MegicBrush.json'
        img_prefix = 'magicbrush_with_background_images_'
    elif set_name == 'VQAv2_with_background':
        val_data_path = 'meta_data_VQAv2.json'
        img_prefix = 'VQA_with_background_images_'
    elif set_name == 'MegicBrush_with_text':
        val_data_path = 'meta_data_MegicBrush.json'
        img_prefix = 'magicbrush_with_text_hint_images_'
    elif set_name == 'VQAv2_with_text':
        val_data_path = 'meta_data_VQAv2.json'
        img_prefix = 'VQA_with_text_hint_images_'
    elif set_name == 'MegicBrush_visually_different':
        val_data_path = 'meta_data_MegicBrush.json'
        img_prefix = 'magicbrush_visually_different_images_'
    elif set_name == 'VQAv2_visually_different':
        val_data_path = 'meta_data_VQAv2.json'
        img_prefix = 'VQA_visually_different_images_'
    
    elif set_name == 'real-world':
        val_data_path = 'meta_data_real-world.json'
        img_prefix = ''
        
    return val_data_path, img_prefix