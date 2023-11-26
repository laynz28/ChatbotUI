from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

character = {
    'name': 'Sky',
    'icon': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIHsGvJIRzEGdp4oMicqCWppS3bZoxAsjvLQ&usqp=CAU',  # Ganti dengan URL ikon karakter
    'description': 'an fnf fan girls.'
}

@app.route('/')
def index():
    return render_template('index.html', character=character)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    # Lakukan pemrosesan bahasa alami atau panggil model bahasa di sini
    # Misalnya, kamu bisa menggunakan model GPT

    # Contoh sederhana: balas dengan pesan yang sama dari pengguna
    bot_response = f'Kamu berkata: {user_message}'

    return jsonify({'bot_response': bot_response, 'character': character})

if __name__ == '__main__':
    app.run()
