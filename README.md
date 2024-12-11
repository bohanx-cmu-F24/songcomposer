This repository is base on the implementation of SongComposer.

## Original Works
<p align="left" style="font-size: em; margin-top: 0.5em">
<a href="https://arxiv.org/pdf/2402.17645"><img src="https://img.shields.io/badge/arXiv-<color>"></a>
<a href="https://github.com/pjlab-songcomposer/songcomposer"><img src="https://img.shields.io/badge/Code-red"></a>
<a href="https://pjlab-songcomposer.github.io"><img src="https://img.shields.io/badge/Demo-yellow"></a>
</p>

## 🛠️ Usage
### Requirements

- python 3.9 and above
- pytorch 2.0 and above
- CUDA 12.0 and above are recommended (this is for GPU users)


### Quickstart

inference.ipynb contains a simple example on how to generate music by running corresponding cells.

Note: The inference provided by SongComposer only prints the music. That's why we can only intercept the printing IO. 


### Inference

We have provide a notebook (`inference.ipynb`) for the inference stage. 

##   Parsing results.

You can use `extract_lines` from `generator.py` to parse raw text from the model to transferable result by `filetune/util.py`:

`finetune/util.py/gen_midi`: Generate midi from standard data output. 
`finetune/util.py/tuple2dict`: Generate 

### Data Processing

Run `data_processing.py` will generate you all the data needed used our experiment, including conducting t-tests. 

You can customize your own tests by changing `generate_data.json`.

Data follows this pattern: 

``` 
{
  "Name of the emotion": [
    "List of parsed dictionary
  ]
} 
```