# unittestのサンプル

起動

```bash
docker compose build
docker compose up -d
```

assertのサンプルのためにブランチを切り替え

```bash
docker compose exec mypython git checkout assert
```

TDDのサンプルのためにpyunitブランチの最初のコミットをチェックアウト

```bash
docker compose exec mypython git checkout e6e3c8852db
```

TDDのユニットテスト

```bash
docker compose exec mypython python -m unittest test_add.py
```

カバレッジの計算のためにmainブランチをチェックアウト

```bash
docker compose exec mypython git checkout main
```

カバレッジの計算

```bash
docker compose exec mypython python -m unittest test_add.py
docker compose exec mypython python -m coverage run test_add.py
docker compose exec mypython coverage report
docker compose exec mypython coverage html
docker compose exec mypython coverage xml
```

テストスイートの実行

```bash
docker compose exec mypython python -m coverage run test_compute.py
```

結合テストの実行とカバレッジの計算

```bash
docker compose exec mypython python -m coverage run test_integration.py
docker compose exec mypython coverage report
docker compose exec mypython coverage html
docker compose exec mypython coverage xml
```

停止

```bash
docker compose down
```
