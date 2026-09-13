# AI TEAM HQ

複数のAIを1つのチームとして動かすための司令部リポジトリ。

## 基本構造

User → Chief → GitHub → Copilot → GitHub → Gemini → GitHub → Chief

AI同士が直接チャットするのではなく、GitHubを共通の作業記憶・伝言板・監査ログとして利用する。

## 原則
- Userは目的を伝えるだけ。可能な限りコードや設定を手編集しない。
- Chiefが全体設計と最終判断を担当する。
- Copilotは実装・テスト・GitHub上の作業中継を担当する。
- Geminiは独立レビュー担当。仕様を勝手に変更しない。
- 不明な情報は推測せず、UNKNOWNとして扱う。
- 重要な変更・判断・テスト結果はGitHubに記録する。

## 現在の状態
Protocol v1.0 foundation

## 次に整備するもの
1. AIへの指示テンプレート
2. 結果報告テンプレート
3. Geminiレビュー手順
4. Copilotエージェント指示
5. プロジェクト登録方式
6. 将来的な自動ハンドオフ
