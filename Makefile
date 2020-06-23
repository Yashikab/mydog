.PHONY: build
build:
	@sh scripts/git-diff-make.sh build

.PHONY: push
push:
	@sh scripts/git-diff-make.sh push

.PHONY: release
release:
	@sh scripts/git-diff-make.sh release
