.PHONY: build
build:
	@bash scripts/git-diff-make.sh build

.PHONY: push
push:
	@bash scripts/git-diff-make.sh push

.PHONY: release
release:
	@bash scripts/git-diff-make.sh release

.PHONY: dev-release
dev-release:
	@bash scripts/git-diff-make.sh dev-release
