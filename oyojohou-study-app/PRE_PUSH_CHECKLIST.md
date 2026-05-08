# GitHub に push する前の確認チェックリスト

## 🚨 最重要：API キー流出防止

push する前に、**絶対に** これを確認してください:

```bash
git status
```

出力内容を見て、以下がないことを確認:

- ❌ `.env`（OpenAI API キーが入っているファイル）
- ❌ `frontend/node_modules/` 
- ❌ `backend/venv/`

もし `.env` や `node_modules` が出ていたら、**push しないでください**。

## チェックリスト

- [ ] `git status` で `.env` が出ていない
- [ ] `.gitignore` に `.env` が書かれている
- [ ] `backend/.env.example` （API キー入りではなく見本ファイル）があることを確認
- [ ] 初回 push の後、GitHub の Web ページでリポジトリを開き、ファイル一覧に `.env` が見当たらないことを確認

## もし誤って push してしまった場合

1. **OpenAI のページで API キーを再発行（無効化）する** — これが最優先
   - https://platform.openai.com/api-keys
   - 古いキーを「削除」し、新しいキーを作成
2. GitHub から履歴を削除する（ただしコミット履歴には残る）
3. 新しいキーで `.env` を更新し、改めて push

**API キーは盗まれると、勝手に OpenAI を使われて課金されます。絶対に流出させないこと。**
