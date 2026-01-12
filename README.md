To update after changes:
-change version in root pkg json
-change version in python/mn_contracts/pyproject.toml (if any changes to python files)
-run `npx tsc` inside ts/mn_contracts
-commit and push to git
-reinstall pkg in the consumer app