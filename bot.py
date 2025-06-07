import csv
import random
import tweepy
import time

# ==== X APIキーをここに入力 ====
API_KEY = '自分のAPIキー'
API_SECRET = '自分のAPIシークレット'
ACCESS_TOKEN = '自分のアクセストークン'
ACCESS_SECRET = '自分のアクセストークンシークレット'

# ==== Xの認証処理 ====
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# ==== 単語リストの読み込み ====
word_list = []
with open('words.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        word_list.append(row)

# ==== 投稿を作る関数 ====
def make_post():
    word = random.choice(word_list)
    noun = word['名詞']
    particle1 = word['てにをは（前）']
    verb = word['動詞']
    particle2 = word['てにをは（後）']
    adjective = word['形容詞']
    post = f"{noun}{particle1}{verb}{particle2}{adjective}"
    return post

# ==== メインループ ====
while True:
    post = make_post()
    print(post)  # デバッグ用。うまくできたか見る
    api.update_status(post)  # Xに投稿！
    time.sleep(1800)  # 30分待つ (1800秒)
