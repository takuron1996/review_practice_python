## 概要

- PR勉強会のPython用リポジトリ
- 使用する場合はforkして使用すること
- ヒント
    - テストは必ずしも正しいわけではないです。

## レビュー対象

- ./application/template/example.py
- ./application/tests/test_example.py

## レビュー対象外

- レビュー対象に含めたファイルとディレクトリ以外
- ファイル名、パッケージ名はレビュー対象外

## 実行方法

### 起動準備

```sh
$ make prepare
```

### コードを実行

```sh
$ make run
```

### テストを実行

```sh
$ make test
```
