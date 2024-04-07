import json, os
from tqdm import tqdm
import multiprocessing
import sys

from utils.get_gpt4 import gpt4

from tqdm import tqdm
import time

def process_data(data, model, image, question):
    output = model(image, question)
    return output

def test_each_multipanel(data, model, img_path, output_dir=None, set_name=None, parallel=False):
    for i in tqdm(range(0, len(data))):
        image = img_path + data[i]['composited_gallery']

        if 'model' in data[i].keys():
            number_Response_error = 0
            for ii in range(len(data[i]['model'])):
                if 'Response Err' in data[i]['model'][ii]:
                    number_Response_error += 1
            if  number_Response_error == 0 and all([data[i]['model'][ii] != None for ii in range(len(data[i]['model']))]):
                continue

        data[i]['model'] = []
        if parallel:
            pool = multiprocessing.Pool(processes=10)
            results = []
            for j in range(len(data[i]['qa'])):
                prompt = data[i]['qa'][j]['question']
                question = prompt
                results.append(pool.apply_async(process_data, (data, model, image, question)))
            pool.close()
            pool.join()
            for result in results:
                output = result.get()
                data[i]['model'].append(output)
        else:
            for j in range(len(data[i]['qa'])):
                prompt = data[i]['qa'][j]['question']
                question = prompt
                output = model(image, question)
                if not output_dir is None:
                    count = 0
                    while 'Response Err' in output:
                        output = model(image, question)
                        count += 1
                        time.sleep(300) 
                        print(count, ' Retry: Response Err, get ', output)
                data[i]['model'].append(output)

        if output_dir is not None:
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "gallery_" + set_name + "_set.json")
            json.dump(data, open(output_file, 'w', encoding="utf8"), indent='\t', separators=(',', ': '))

    correct = 0
    total = 0
    for i in tqdm(range(0,len(data))):
        data[i]['model_correct'] = [False]*len(data[i]['qa'])
        for j in range(len(data[i]['qa'])):
            answer = data[i]['qa'][j]['answer'].lower().replace('.','')
            question = data[i]['qa'][j]['question']
            
            # Define the texts to compare
            output = data[i]['model'][j]
            text1 = output.replace('</s>','').replace(')', '').replace('.', '').replace(',', '').lower().strip()
            text2 = answer.replace(')', '').replace('.', '').replace(',', '').lower().strip()
            if j == 2:
                prompt="For question: "+question+"\nGround truth answer: "+text2+"\nModel predicted answer: "+text1+"\nBased on the question and the ground truth answer, is the model's predicted answer correct? If multi-choice provided, think about which choice is selected by the model, is it correct? (please answer yes/no)\n"
            else:
                prompt="For question: "+question+"\nCompare the following answers:\nText 1: "+text1+"\nText 2: "+text2+"\nDoes the first one contain all key information in the second one? (yes/no)\nAnswer:"
            # print()
            if text1 == text2 or (text1 in ['yes', 'no'] and text1 in text2.split(' '))or (text2 in ['yes', 'no'] and text2 in text1.split(' ')):
                is_equivalent = "yes"
            elif text1 in ['yes', 'no'] and not text1 in text2.split(' '): # our GT answer is alwasy very concise
                # print('[1]:')
                is_equivalent = "no"
            elif text2 in 'abcd' and text1 in 'abcd' and text2!=text1:
                # print('[2]:')
                is_equivalent = "no"
            else:
                # Get the model's response
                is_equivalent = gpt4(prompt).lower()
                # print('GPT:')
            # print('prompt',prompt)
            print('is_equivalent', is_equivalent)
        # Check if the texts are equivalent
            if "yes" in is_equivalent :
                correct += 1
                data[i]['model_correct'][j] = True
            else:
                data[i]['model_correct'][j] = False
        total += 1
                
        

    return correct, total, correct/total, data