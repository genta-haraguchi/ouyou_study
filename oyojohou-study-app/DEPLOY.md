# デプロイ手順

ローカル PC とスマホの両方からアクセスできるようにする手順です。

## 構成

- **フロントエンド** → Vercel（無料・自動デプロイ）
- **バックエンド** → Render（無料プランあり）

両方とも GitHub と連携でき、push するだけで自動デプロイされます。

---

## ステップ1: GitHub にリポジトリを作る

1. GitHub で新しいリポジトリを作成（例: `oyojohou-study-app`）
2. ローカルでこのプロジェクトを Git に登録:

```bash
cd oyojohou-study-app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/あなたのユーザー名/oyojohou-study-app.git
git push -u origin main
```

**確認**: GitHub のページを開いて、`.env` ファイルが **含まれていない** ことを必ず確認してください。
含まれていたら、API キーが流出しています。すぐに OpenAI のページでキーを再発行してください。

---

## ステップ2: バックエンドを Render にデプロイ

1. [Render](https://render.com/) にサインアップ（GitHub アカウントで OK）
2. ダッシュボードから「New」→「Web Service」
3. 先ほど作った GitHub リポジトリを選択
4. 設定:
   - **Name**: `oyojohou-backend`（任意）
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. 「Environment Variables」で以下を追加:
   - `OPENAI_API_KEY` = `sk-...`（あなたの API キー）
6. 「Create Web Service」を押す

数分待つと、`https://oyojohou-backend.onrender.com` のような URL が発行されます。
ブラウザで `そのURL/api/health` を開いて `{"status":"ok"}` が返れば成功です。

> **補足**: Render の無料プランは15分間アクセスがないとスリープします。
> 最初のリクエストだけ20秒くらい待たされますが、勉強用なら気になりません。

> **補足2**: `gunicorn` は `requirements.txt` に未追加です。Render にデプロイする前に
> `requirements.txt` に `gunicorn==21.2.0` を追加してください。

---

## ステップ3: フロントエンドを Vercel にデプロイ

1. [Vercel](https://vercel.com/) にサインアップ（GitHub アカウントで OK）
2. 「Add New Project」→ GitHub リポジトリを選択
3. 設定:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
4. 「Environment Variables」で以下を追加:
   - `VITE_API_URL` = `https://oyojohou-backend.onrender.com`（ステップ2の URL）
5. 「Deploy」を押す

数分後、`https://oyojohou-study-app.vercel.app` のような URL が発行されます。
スマホでもこの URL を開けば使えます。

---

## ステップ4: フロントのコードを修正（必須）

現状のコードは Anthropic API を直接呼んでいる仮実装になっているので、
バックエンド経由に書き換える必要があります。

`frontend/src/App.jsx` の `summarize` 関数の `fetch` 部分を以下に置き換え:

```javascript
const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000';

const body = inputMode === 'image' && imageData
  ? { image: imageData, media_type: imageMediaType }
  : { text: explanation };

const response = await fetch(`${apiUrl}/api/summarize`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
});

const data = await response.json();
if (data.error) throw new Error(data.error);
setSummary(data.summary);
```

---

## ステップ5: スマホのホーム画面に追加

iPhone:
1. Safari で Vercel の URL を開く
2. 共有ボタン → 「ホーム画面に追加」

Android:
1. Chrome で Vercel の URL を開く
2. メニュー → 「ホーム画面に追加」

これでアプリのアイコンとして起動できるようになります。

---

## トラブルシューティング

### CORS エラーが出る
バックエンドの `app.py` の `CORS(app)` を以下のように変更:
```python
CORS(app, origins=["https://oyojohou-study-app.vercel.app"])
```

### Render が起動しない
- `requirements.txt` に `gunicorn` が入っているか確認
- 環境変数 `OPENAI_API_KEY` が設定されているか確認
- Render のログ画面でエラー内容を確認

### 画像アップロード時に413エラー
画像が大きすぎる可能性。フロント側のリサイズ処理（MAX = 1500）が動いているか確認。
