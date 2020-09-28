# mydogの使い方

## 機能

ciツールのdroneを使うことで以下のコメント投稿が行える。

- reviewdog: reviewdogのpull requestへの投稿
- pytest coverage: pytestのカバレッジのpull requestへの投稿
- comment from file: 任意のtextファイル、mdのpull requestへの投稿

## 準備

指定するdocker imageは[こちら](https://hub.docker.com/repository/docker/yashikab/mydog)

tagはtokenの取得にpythonを用いた場合はpython, ほか言語を用いた場合はその言語名とする（予定）。 `dev`がつくものは開発中のものなので動作が安定しない場合がある。

github appを作成し、`app_id`と`installation_id`、private keyを用意する。
それらを、以下の環境変数名で指定する。
|id|環境変数名|
|---|---|
|app_id|APP_ID|
|installation_id|INSTALLATION_ID|
|privete key|PRIVATE_KEY|

セキュリティの観点から、上記IDはdroneのsecret変数として登録し、環境変数で登録したsecretを読み込むのが良い。

drone1系での設定例

```yml
steps:
- name: reviewdog
  pull: always
  image: yashikab/mydog:python
  environment:
    DOCKER_API_VERSION: 1.39
    PRIVATE_KEY:
      from_secret: github_pri_key
    APP_ID:
      from_secret: app_id
    INSTALLATION_ID:
      from_secret: installation_id
  commands:
    ...
```

## 使用方法

### reviewdog

`rp_reviewdog`を使い、引数としてreviewdogで検知してほしいファイルまたはフォルダを選ぶ。

```yml
...
  commands:
    - rp_reviewdog --dir={target file or dir}
```

### pytest

`rp_pytest`を使い、引数としてテストカバレッジを計測したいファイルまたはフォルダを選ぶ。

```yml
  commands:
    - rp_pytest {target file or dir}
```

### comment from file

`pr_comment`を使い、引数としてテキストファイルまたはmarkdownを指定する。
markdownの場合現在のところurlリンクには対応していないので注意する。

```yml
  commands:
    - pr_comment {target text file or markdown}
```
