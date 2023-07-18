import random
from flask import Flask

app = Flask(__name__)

def generate_fortune():
    fortunes = {
        "大吉": 10,
        "吉": 30,
        "中吉": 25,
        "小吉": 15,
        "凶": 20
    }

    outcomes = {
        "願望": ["叶うでしょう", "なかなか叶わないかもしれません", "途中で諦めずに頑張りましょう"],
        "健康": ["元気に過ごせるでしょう", "ちょっと調子が崩れるかもしれません", "健康には気をつけましょう"],
        "失物": ["見つかるでしょう", "なかなか見つからないかもしれません", "探し続けてみましょう"],
        "旅行": ["楽しい旅行ができるでしょう", "予定が変わるかもしれません", "旅行の計画をしっかり立てましょう"],
        "商売": ["成功するでしょう", "売り上げが少し減るかもしれません", "努力を惜しまず頑張りましょう"],
        "学問": ["順調に進展するでしょう", "少し苦労するかもしれません", "諦めずに頑張りましょう"],
        "争事": ["円満に解決するでしょう", "少しトラブルが起きるかもしれません", "冷静な判断を心がけましょう"],
        "恋愛": ["素敵な出会いがあるでしょう", "恋の運気は少し低めかもしれません", "自分に自信を持ちましょう"],
        "平泉運": ["順調な運勢です", "ちょっと停滞気味かもしれません", "前向きな気持ちで過ごしましょう"]
    }

    fortune = random.choices(list(fortunes.keys()), weights=list(fortunes.values()), k=1)[0]
    outcome = random.choice(list(outcomes.keys()))
    message = random.choice(outcomes[outcome])

    return fortune, outcome, message

@app.route('/')
def show_omikuji():
    fortune, outcome, message = generate_fortune()

    html = """
    <html>
    <head>
        <title>おみくじアプリ</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }

            .omikuji-paper {
                width: 400px;
                margin: 50px auto;
                background-color: #fef8e6;
                border: 2px solid #d4af37;
                padding: 20px;
                text-align: center;
            }

            h1 {
                font-size: 24px;
                margin-top: 0;
            }

            h2 {
                font-size: 20px;
                margin-bottom: 0;
            }
        </style>
    </head>
    <body>
        <div class="omikuji-paper">
            <h1>今日の運勢は「{}」です。</h1>
            <h2>{}の運勢は「{}」です。<br>{}。</h2>
        </div>
    </body>
    </html>
    """.format(fortune, outcome, message, message)

    return html

if __name__ == '__main__':
    app.run()