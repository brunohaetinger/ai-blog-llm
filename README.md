# AI Blog LLM


## Using llama.cpp

- Clone repo
- run `make`

- Download model:
> pip install transformers datasets sentencepiece
> huggingface-cli download Universal-NER/UniNER-7B-type --local-dir models

- Convert script (if need to transform into .gguf):
> python conver.py ./models

- Quantize model:
> ./quantize models/ggml-model-f32.gguf models/quantized_q4_1.gguf q4_1

- List models
> ls ./models

- There are 2 main ways of running cpp models:
    - CLI Inference —The model loads, runs the prompt, and unloads in one go. Good for a single run.
    - Server Inference — The model loads into RAM and starts a server. It stays loaded as long as the server is running.
        > ./server -m ./models/quantized_q4_1.gguf -c 1024


## Vicuna example:

Request:
```
POST http://localhost:8080/completion

{
  "stream": false,
  "n_predict": 400,
  "temperature": 0,
  "stop": [
    "</s>"
  ],
  "repeat_last_n": 256,
  "repeat_penalty": 1,
  "top_k": 20,
  "top_p": 0.75,
  "tfs_z": 1,
  "typical_p": 1,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "mirostat": 0,
  "mirostat_tau": 5,
  "mirostat_eta": 0.1,
  "grammar": "",
  "n_probs": 0,
  "prompt": "What RGB colors means  ?"
}
```

Response:
```
{
  "content": "\n\nI want to know what RGB colors means.\n\nFor example, what does #FF0000 mean?\n\nI know that it represents red, but what does it represent in terms of RGB?\n\nAnswer: In RGB color model, #FF0000 represents the color red. The first two digits, FF, represent the maximum value of red, which is 255. The second two digits, 00, represent the maximum value of green, which is also 255. The third two digits, 00, represent the maximum value of blue, which is also 255. So, #FF0000 represents the color red with the maximum value of all three primary colors, red, green, and blue.",
  "id_slot": 0,
  "stop": true,
  "model": "./models/Wizard-Vicuna-7B-Uncensored.Q4_0.gguf",
  "tokens_predicted": 167,
  "tokens_evaluated": 8,
  "generation_settings": {
    "n_ctx": 1024,
    "n_predict": -1,
    "model": "./models/Wizard-Vicuna-7B-Uncensored.Q4_0.gguf",
    "seed": 4294967295,
    "temperature": 0.0,
    "dynatemp_range": 0.0,
    "dynatemp_exponent": 1.0,
    "top_k": 20,
    "top_p": 0.75,
    "min_p": 0.05000000074505806,
    "tfs_z": 1.0,
    "typical_p": 1.0,
    "repeat_last_n": 256,
    "repeat_penalty": 1.0,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0,
    "penalty_prompt_tokens": [],
    "use_penalty_prompt_tokens": false,
    "mirostat": 0,
    "mirostat_tau": 5.0,
    "mirostat_eta": 0.10000000149011612,
    "penalize_nl": false,
    "stop": [
      "</s>"
    ],
    "n_keep": 0,
    "n_discard": 0,
    "ignore_eos": false,
    "stream": false,
    "logit_bias": [],
    "n_probs": 0,
    "min_keep": 0,
    "grammar": "",
    "samplers": [
      "top_k",
      "tfs_z",
      "typical_p",
      "top_p",
      "min_p",
      "temperature"
    ]
  },
  "prompt": "What RGB colors means  ?",
  "truncated": false,
  "stopped_eos": true,
  "stopped_word": true,
  "stopped_limit": false,
  "stopping_word": "</s>",
  "tokens_cached": 174,
  "timings": {
    "prompt_n": 8,
    "prompt_ms": 1627.577,
    "prompt_per_token_ms": 203.447125,
    "prompt_per_second": 4.915282041955619,
    "predicted_n": 167,
    "predicted_ms": 38292.836,
    "predicted_per_token_ms": 229.29841916167666,
    "predicted_per_second": 4.36112906341019
  }
}
```

## Notes

- Quantization: 
Quantization of deep neural networks is the process of taking full precision weights, 32bit floating points, and convert them to smaller approximate representation like 4bit /8 bit etc..