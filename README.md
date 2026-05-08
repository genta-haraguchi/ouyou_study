[README.md](https://github.com/user-attachments/files/27503918/README.md)
# 応用情報 学習帳

応用情報技術者試験の勉強を **「毎日少しずつ続ける」** ことに特化した Web アプリ。

## 主な機能

| 機能 | 説明 |
|---|---|
| 🎲 サイコロ機能 | 1〜6 の数字をランダム表示。「今日は何問やる？」を自動で決めて継続のハードルを下げる |
| ✨ AI要約 | 解説文を貼り付け（または画像をアップロード）すると、AI が覚えやすい1文に要約 |
| 📷 画像入力 | スクショや教科書の写真からも要約できる。PC では `Ctrl+V` で直接貼り付け可能 |
| 📝 メモ機能 | AI 要約に対して自分用のメモを残せる |
| 📚 学習履歴 | 過去の要約とメモを一覧で振り返れる |

## 使い方（ユーザー視点）

### PC の場合
1. Web 教材や PDF を開く
2. `Win + Shift + S`（Mac は `Cmd + Shift + 4`）で範囲スクショ
3. アプリのページ上で `Ctrl + V`（Mac は `Cmd + V`）
4. 「AIで1文に要約」ボタンを押す
5. メモを書いて保存

### スマホの場合
1. 「画像」モードを選択
2. 「写真/ファイルを選ぶ」ボタンでカメラを起動
3. 教科書のページや問題集を撮影
4. 「AIで1文に要約」ボタンを押す

## 技術スタック

- **フロントエンド**: React (Vite), Tailwind CSS, lucide-react
- **バックエンド**: Python (Flask)
- **AI API**: OpenAI API (GPT-4o)
- **デプロイ予定**: Vercel (フロント) + Render (バックエンド)

## セットアップ（開発者向け）

### 前提
- Node.js 18+
- Python 3.10+
- OpenAI API キー（[こちら](https://platform.openai.com/api-keys) から取得）

### バックエンド起動

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# .env ファイルを作成
cp .env.example .env
# .env を編集して OPENAI_API_KEY=sk-... を記入

python app.py
```

→ `http://localhost:5000` でバックエンドが起動

### フロントエンド起動

```bash
cd frontend
npm install
npm run dev
```

→ `http://localhost:5173` でフロントが起動

## ディレクトリ構成

```
oyojohou-study-app/
├── README.md
├── .gitignore
├── frontend/
│   ├── package.json
│   └── src/
│       ├── App.jsx          # メインのUIコンポーネント
│       └── main.jsx
└── backend/
    ├── requirements.txt
    ├── .env.example
    └── app.py               # Flask APIサーバー
```

## 開発記録

このアプリは応用情報技術者試験の学習効率化と、Web アプリ開発・GitHub 運用・API 利用の経験を積むことを目的に作っています。

### 実装済み

- [x] サイコロ機能
- [x] テキスト入力での AI 要約
- [x] 画像入力での AI 要約（カメラ撮影・ファイル選択・クリップボード貼り付けに対応）
- [x] メモ機能
- [x] 学習履歴の保存（localStorage）
- [x] レスポンシブデザイン

### 今後追加したい機能

- [ ] 苦手分野のタグ付け / 分析
- [ ] 連続学習日数カウント
- [ ] 科目別管理（ネットワーク・DB・セキュリティ等）
- [ ] AI による復習問題自動生成
- [ ] ログイン機能（複数端末でデータ同期）
- [ ] PWA化（ホーム画面追加・オフライン対応）

## ライセンス

MIT
