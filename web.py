import gradio as gr
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import openai

openai.api_key = "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"

# Load GPT-3 model using transformers library
model_name = 'gpt-3'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def chatbot(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    response = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(response[0], skip_special_tokens=True)

iface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="Chai Chatbot",
    description="Short description of the Chai character.",
    interpretation="The Magical Chatbot",
    icon="icon.png"  # Replace with the filename of your icon
)

iface.launch(share=true)
