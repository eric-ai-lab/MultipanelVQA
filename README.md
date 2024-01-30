# Muffin or Chihuahua? Challenging Large Vision-Language Models with Multipanel VQA

Yue Fan†, Jing Gu†, Kaiwen Zhou†, Qianqi Yan†, Shan Jiang‡, Ching-Chen Kuo‡, Yang Zhao‡, Xinze Guan‡, and Xin Eric Wang†

†Univeristion of California, Santa Cruz, ‡eBay Inc.

<a href='https://arxiv.org/abs/2401.15847'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a> <a href='https://sites.google.com/view/multipanelvqa/home'><img src='https://img.shields.io/badge/Project-Page-green'></a>

![teaser](teaser.png)

Multipanel images, commonly seen as web screenshots, posters, etc., pervade our daily lives. These images, characterized by their composition of multiple subfigures in distinct layouts, effectively convey information to people. Toward building advanced multimodal AI applications, such as agents that understand complex scenes and navigate through webpages, the skill of multipanel visual reasoning is essential, and a comprehensive evaluation of models in this regard is important. Therefore, our paper introduces Multipanel Visual Question Answering (MultipanelVQA), a novel benchmark that specifically challenges models in comprehending multipanel images. The benchmark comprises 6,600 questions and answers related to multipanel images. While these questions are straightforward for average humans, achieving nearly perfect correctness, they pose significant challenges to the state-of-the-art Large Vision Language Models (LVLMs) we tested. In our study, we utilized synthetically curated multipanel images specifically designed to isolate and evaluate the impact of diverse factors on model performance, revealing the sensitivity of LVLMs to various interferences in multipanel images, such as adjacent subfigures and layout complexity. As a result, MultipanelVQA highlights the need and direction for improving LVLMs' ability to understand complex visual-language contexts.

# Data
MultipanelVQA includes both real-world subset and synthetic subset.

You may view/download them at: [real-world subset](https://huggingface.co/datasets/yfan1997/MultipanelVQA_real-world) and [synthetic subset](https://huggingface.co/datasets/yfan1997/MultipanelVQA_synthetic).

Todos:

 - [ ] Release code for evaluation
 - [ ] Release code for generating synthetic subset.
