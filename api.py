from bardapi import Bard
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/get/<string:word>", methods=['GET'])
def getResponse(word):
    bard = Bard()

    i = f'''"{word}"의 정보를 간략하게 아래 형식과 같이 알려줘. (표 말고, 줄바꿈 하여 깔끔하게)
    (해당 단어) (해당 단어의 품사) (해당 단어의 뜻)
    (해당 단어가 해당 뜻으로 쓰인 짧고 쉬운 문장) (그 문장의 한국어 번역)
    
    만약 반의어 또는 유의어가 있다면
    (반의어, 해당 반의어의 뜻, 해당 반의어의 품사)
    (유의어, 해당 유의어의 뜻, 해당 유의어의 품사)
    
    만약 해당 단어의 다른 품사가 있다면
    (해당 단어의 다른 품사, 그 품사일 때의 뜻)

    그리고 각 정보들을 줄바꿈하여 깔끔하게 표시해줘야해'''

    res = bard.get_answer(i)['content']
    return jsonify({'res': res}), 200
