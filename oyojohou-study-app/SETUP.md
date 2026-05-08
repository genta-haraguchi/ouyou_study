# セットアップガイド

このプロジェクトをローカル環境で動かすまでの手順です。

## 前提環境

- Node.js 18+ （[ダウンロード](https://nodejs.org/)）
- Python 3.10+ （[ダウンロード](https://www.python.org/)）
- Git （[ダウンロード](https://git-scm.com/)）
- OpenAI API キー（[取得方法](https://platform.openai.com/api-keys)）

## ステップ1: プロジェクトを配置

```bash
unzip oyojohou-study-app.zip
cd oyojohou-study-app
```

## ステップ2: バックエンド（Flask）をセットアップ

```bash
cd backend

# Python 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows の場合:
venv\Scripts\activate
# Mac / Linux の場合:
source venv/bin/activate

# 依存パッケージをインストール
pip install -r requirements.txt

# .env ファイルを作成（API キー用）
cp .env.example .env

# .env をテキストエディタで開いて、API キーを記入
# （Windows ユーザーは Notepad、Mac ユーザーは TextEdit 等で OK）
```

**`.env` ファイルの編集**:
```
OPENAI_API_KEY=sk-...（あなたの OpenAI API キー）
```

## ステップ3: フロントエンド（React）をセットアップ

別のターミナルを開いて:

```bash
cd frontend

# 依存パッケージをインストール
npm install

# 開発サーバーを起動
npm run dev
```

出力で `http://localhost:5173` と表示されるので、ブラウザでアクセス。

## ステップ4: バックエンドサーバーを起動

最初のターミナル（仮想環境が有効になっているところ）で:

```bash
# backend ディレクトリにいることを確認
cd backend
python app.py
```

出力で `Running on http://localhost:5000` と表示されれば成功。

## ステップ5: 動作確認

ブラウザで以下にアクセス:

1. **フロント**: `http://localhost:5173`
2. **バックエンド**: `http://localhost:5000/api/health`

どちらも OK が返れば、セットアップ完了！

## トラブルシューティング

### `venv: command not found`
Python がインストールされていないか、PATH が通っていません。
```bash
python --version  # Python のバージョン確認
```

### `npm: command not found`
Node.js がインストールされていません。[ダウンロード](https://nodejs.org/)してインストール。

### ポート 5000 が既に使われている
別のアプリが使用中です。以下で確認:
```bash
# Windows:
netstat -ano | findstr :5000
# Mac/Linux:
lsof -i :5000
```

別のポートで起動:
```python
# app.py の最後の行を変更
app.run(host="0.0.0.0", port=5001, debug=True)  # 5000 を 5001 に
```

### OpenAI API のエラー
- API キーが間違っていないか確認
- API キーの有効期限が切れていないか確認
- OpenAI のアカウントにクレジットが残っているか確認

## 次のステップ

- [ ] ローカルで動作確認完了
- [ ] GitHub にリポジトリを作成
- [ ] PRE_PUSH_CHECKLIST.md を確認して push
- [ ] DEPLOY.md を読んで Vercel + Render にデプロイ
- [ ] 応用情報の勉強を開始！
