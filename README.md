# Recursion プロジェクト | RPC 実装

このリポジトリは、UNIX ドメインソケット と JSON シリアライザを用いたシンプルな RPC (Remote Procedure Call) サーバー/クライアントの学習用プロジェクトです。クライアントがメソッド名とパラメーターを送信し、サーバーが対応する関数を実行して結果を返します。

## 特徴

- Python 標準ライブラリのみで構成された実装
- アプリケーション / ドメイン / インフラ層に分割
- JSON でのリクエスト・レスポンス表現
- Pytest による単体テストを用意(AI生成)

## ディレクトリ構成

```
.
├─ src/
│  ├─ application/   # エントリポイントとメソッドテーブル定義
│  ├─ domain/        # エンティティ・例外・サービスなどのドメインロジック
│  └─ infrastructure/# ソケットとシリアライザの具象実装
├─ tests/            # Pytest によるテスト
├─ request_template.json
└─ response_template.json
```

## 提供される RPC メソッド

`src/domain/services/rpc_functions.py` に定義されたメソッドを `src/application/config.py` の `METHOD_TABLE` で公開しています。

| メソッド名     | 説明                             | 期待するパラメーター           | 戻り値      |
| -------------- | -------------------------------- | ------------------------------ | ----------- |
| `floor`        | 小数の切り捨て                   | `float` もしくは `int` を 1 つ | `int`       |
| `n_root`       | n 乗根の計算（奇数根は負数対応） | 底 `int`／指数 `int (>0)`      | `float`     |
| `reverse`      | 文字列を逆順に並べ替え           | `str`                          | `str`       |
| `validAnagram` | 2 つの文字列がアナグラムか判定   | `str`, `str`                   | `bool`      |
| `sort`         | 文字列のリストを辞書順ソート     | `list[str]`                    | `list[str]` |

## リクエスト / レスポンス形式

RPC メッセージは JSON で表現し、`RpcRequest` / `RpcResponse` エンティティにマッピングされます。

### リクエスト例 (`request_template.json`)

```json
{
  "method": "n_root",
  "params": ["27", "3"],
  "param_types": ["int", "int"],
  "id": "b6c1f7b2-2b41-45ac-ae84-3d34e6eb9ef5"
}
```

- `params` は文字列として渡し、`param_types` で指定した型にサーバー側でキャストされます。
- `id` はクライアントで UUID などの一意な値を生成します。

### レスポンス例 (`response_template.json`)

```json
{
  "results": "3.0",
  "result_type": "float",
  "error": null,
  "id": "b6c1f7b2-2b41-45ac-ae84-3d34e6eb9ef5"
}
```

- エラーが発生した場合は `error` にメッセージが入り、`results` は `null` になります。

## 動作環境

- Python 3.11 以上を想定（標準ライブラリのみ使用）
- テスト実行には `pytest` が必要

## サーバーとクライアントの実行手順

1. 2 つのターミナルを用意します。
2. 1 つ目のターミナルでサーバーを起動します。
   ```bash
   python3 -m src.application.main_server
   ```
3. 2 つ目のターミナルでクライアントを起動します。
   ```bash
   python3 -m src.application.main_client
   ```
4. プロンプトに従い、メソッド名・パラメーター・パラメーター型を入力すると、サーバーで計算された結果が表示されます。`exit` を入力すると終了します。

## テスト

プロジェクト直下で以下を実行します。

```bash
pytest
```

## 拡張方法

- 新しい RPC 関数を追加する場合は `RpcFunctions` クラスにメソッドを実装し、`config.py` の `METHOD_TABLE` に登録します。
- 送受信フォーマットを変更したい場合は `JsonSerializer` を差し替えることで対応可能です。
- 別のトランスポート層を利用したい場合は `SocketHandler` 抽象クラスを実装した新しいハンドラーを追加してください。
