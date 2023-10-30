from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.debug = True

# 問題番号、問題、解答、状態を格納しているcsvファイル
FILE = '/home/m1496/anki01/mondai01.csv'
# keyに問題番号を持ち、問題、解答、状態のリストをvalueに持つディクショナリ―を作成
data = {}
# 問題番号を持つリスト
num  = []
# 現在の問題番号を示すインデックス
i = 0

# 初期ページ
@app.route('/', methods=["GET"])
def index():
    # csvファイルからデータを読み込み、dataに保存する
    with open(FILE, 'r') as f:
        for line in list(f):
            s = line.split(',')
            global data
            data.update({s[0] : [s[1], s[2], s[3].strip('\n')]})
        global num
        num = list(data.keys())
        random.shuffle(num) # リストのキーをシャッフルする
    return render_template('question.html', no=num[i], question=data[num[i]][0])

# 問題ページ
@app.route('/question', methods=["GET"])
def question():
    global i
    if i < len(num) - 1:
        i += 1
    else:
        i = 0
    return render_template('question.html', no=num[i], question=data[num[i]][0])

# 解答ページ
@app.route('/answer', methods=["GET"])
def answer():
    return render_template('answer.html', no=num[i], ans=data[num[i]][1])
