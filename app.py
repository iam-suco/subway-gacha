from flask import Flask, render_template
import random

app = Flask(__name__)

# メニュー
sandwiches = {
     "ベジーデライト":"ベジ-sb.jpg", "ハム":"ハム-sb.jpg", "たまご":"たまご-sb.jpg", 
     "ツナ":"ツナ-sb.jpg", "アボカドベジー":"アボカド-sb.jpg", "サラダチキン":"サラダチキン-sb.jpg", 
     "チリチキン":"チリチキン-sb.jpg", "BLT":"BLT-sb.jpg", "てり焼きチキン":"てりやき-sb.jpg",
     "えびたま":"えびたま-sb.jpg","チーズサラダチキン":"チーズサラダチキン-sb.jpg", "えびアボカド":"えびアボカド-sb.jpg", 
     "生ハム&マスカルポーネ":"生ハムマスカルポーネ-sb.jpg", "ハムクラブハウス":"ハムクラブハウス-sb.jpg", "アボカドチキン":"アボカドチキン-sb.jpg",
     "スパイシークラブハウス":"スパイシークラブハウス-sb.jpg", "ローストビーフ":"ローストビーフ-sb.jpg"}


# パンの種類・トースト
breads = ["ホワイト", "ウィート", "ハニーオーツ", "セサミ"]
toast_options = ["焼く", "焼かない"]

# 野菜・調整不可（ピザの場合）
veggies = ["レタス", "トマト", "ピーマン", "オニオン", "オリーブ", "ピクルス", "ホットペッパー"]
veggie_amounts = ["標準", "抜き", "少なめ", "多め"]

# トッピング（最大2つ）
toppings = ["ナチュラルチーズ", "クリームタイプチーズ", "マスカルポーネチーズ", "たまご", "ベーコン",
            "ツナ", "えび", "アボカド",  "ハム"]

# ソース（最大9つ）
sauces = [
    "オイル＆ビネガー/塩・胡椒", "シーザー", "野菜クリーミー", "わさび醤油", "チリソース",
    "ハニーマスタード","バジル", "チポトレ", "マヨ"]

# @app.route('/') は「トップページ（/）にアクセスした時にこの関数を動かす」という設定です
@app.route('/')
def index():
    # --- ガチャロジック開始 ---
    
    # メニュー（辞書のキー）からランダムに1つ選び、対応する画像ファイル名を取得
    item_name = random.choice(list(sandwiches.keys()))
    item_image = sandwiches[item_name]
    
    # パンの種類とトーストの有無をランダムに決定
    bread = random.choice(breads)
    toast = random.choice(toast_options)
    
    # 全ての野菜に対して、それぞれの量をランダムに決定（辞書内包表記）
    veggie_custom = {veg: random.choice(veggie_amounts) for veg in veggies}

    # トッピングを追加するかどうかをランダム（50%）で決定
    add_topping = random.choice([True, False])
    if add_topping:
        # トッピングリストから1〜2個を重複なしで選択
        topping_choice = random.sample(toppings, k=random.randint(1, 2))
    else:
        # 追加しない場合は「なし」とする
        topping_choice = ["なし"]

    # ソースを1種類から最大数（今回は9種類）の間でランダムに選ぶ
    num_sauces = random.randint(1, len(sauces))
    sauce_choice = random.sample(sauces, k=num_sauces)
    
    # --- ガチャロジック終了 ---

    # render_templateを使って、用意したHTMLファイル（index.html）を表示します
    # その際、右側の変数（Pythonでの結果）を左側の名前でHTMLへ引き渡します
    return render_template('index.html', 
                           item=item_name,       # 商品名
                           image=item_image,     # 画像ファイル名
                           bread=bread,         # パン
                           toast=toast,         # トースト
                           veggies=veggie_custom, # 野菜のカスタム状況
                           toppings=topping_choice, # 選ばれたトッピング
                           sauces=sauce_choice)  # 選ばれたソース

# このファイルが直接実行された場合、デバッグモードでWebサーバーを起動します
if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))





