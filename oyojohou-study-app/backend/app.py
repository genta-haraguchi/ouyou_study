"""
応用情報 学習帳 - バックエンドAPI

OpenAI API キーを安全に保管し、フロントエンドからの要約リクエストを
中継するシンプルな Flask サーバー。
"""

import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # 開発中はすべてのオリジンを許可。本番では origins=[...] で絞ること

# OpenAI クライアントの初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "あなたは応用情報技術者試験の家庭教師です。"
    "ユーザーから渡される解説文や画像内容を、"
    "後で見返したときに本質がパッと思い出せる「覚えやすい1文（30〜60文字）」に要約してください。"
    "要約のみを出力し、前置きや説明は一切不要です。"
)


@app.route("/api/health", methods=["GET"])
def health():
    """サーバーが動いているか確認用"""
    return jsonify({"status": "ok"})


@app.route("/api/summarize", methods=["POST"])
def summarize():
    """
    解説文 or 画像を受け取り、1文要約を返す。

    リクエスト形式:
      テキストの場合: { "text": "解説文..." }
      画像の場合:     { "image": "base64文字列", "media_type": "image/jpeg" }
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "リクエストボディがありません"}), 400

    try:
        # 入力タイプによってメッセージを組み立てる
        if data.get("image"):
            # 画像入力モード（GPT-4o の Vision 機能を使用）
            image_b64 = data["image"]
            media_type = data.get("media_type", "image/jpeg")

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "画像内の解説や問題を1文に要約してください。"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{media_type};base64,{image_b64}"
                            },
                        },
                    ],
                },
            ]

        elif data.get("text"):
            # テキスト入力モード
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": data["text"]},
            ]

        else:
            return jsonify({"error": "text または image を指定してください"}), 400

        # OpenAI API 呼び出し
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 安くて速い。精度を上げたいなら "gpt-4o" に変更
            messages=messages,
            max_tokens=200,
            temperature=0.3,
        )

        summary = response.choices[0].message.content.strip()
        return jsonify({"summary": summary})

    except Exception as e:
        # 本番では詳細なエラーをユーザーに返さないこと
        print(f"エラー発生: {e}")
        return jsonify({"error": "要約処理中にエラーが発生しました"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
