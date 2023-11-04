import gradio as gr
import openai

openai.api_key = "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"

def chatbot(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=150
    )
    return response.choices[0].text

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
