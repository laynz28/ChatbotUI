from flask import Flask, render_template, request
import gradio as gr

app = Flask(__name__)

# Fungsi untuk mengganti (* *) dengan link karakter dari character.ai
def replace_action(*https://c.ai/c/s8monVYz28ehmepyf1PbkP1bl7cj4e7-l5d5RNrdtnc*):
    # Implementasi logika penggantian (* *) dengan link karakter
    # Misalnya, Anda dapat menggunakan regex atau metode penggantian sederhana
    # Di sini, saya contohkan dengan menggantikan (*nama_karakter*) dengan link ke character.ai/nama_karakter
    replaced_text = text.replace("(*)", "[https://c.ai/c/s8monVYz28ehmepyf1PbkP1bl7cj4e7-l5d5RNrdtnc](https://character.ai)")
    return replaced_text

# Fungsi Gradio untuk memproses input dan mengembalikan output
def chatbot(text):
    processed_text = replace_action(text)
    return processed_text

# Gradio UI
iface = gr.Interface(fn=chatbot, inputs="text", outputs="text")
iface.launch(share=True)

if __name__ == '__main__':
    app.run(debug=True)
