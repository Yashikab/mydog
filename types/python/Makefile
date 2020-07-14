NAME             := mydog
REVISION         := $(shell git rev-parse --short HEAD)
ORIGIN           := $(shell git remote get-url origin | sed -e 's/^.*@//g')
RELEASE_TAGS     := latest python
DEV_RELEASE_TAGS := python-dev
TAGS             := python
REGISTRY         := index.docker.io
USER             := yashikab
IMAGENAME        := $(USER)/$(NAME)
.PHONY: test
test:
	@echo $(NAME)

.PHONY: build
build:
	@docker build \
		--build-arg GIT_REVISION=$(REVISION) \
		--build-arg GIT_ORIGIN=$(ORIGIN) \
		--build-arg IMAGE_NAME=$(IMAGENAME) \
		--build-arg APP_ID=$(APP_ID) \
		--build-arg INSTALLATION_ID=$(INSTALLATION_ID) \
		--build-arg PRIVATE_KEY="$(PRIVATE_KEY)" \
		$(addprefix -t $(IMAGENAME):,$(TAGS)) .

.PHONY: push
push:
	@for TAG in $(TAGS); do\
		docker push $(IMAGENAME):$$TAG; \
	done

.PHONY: release
release:
	@make build TAGS="$(RELEASE_TAGS)"
	@make push TAGS="$(RELEASE_TAGS)"

.PHONY: dev-release
dev-release:
	@make build TAGS="$(DEV_RELEASE_TAGS)"
	@make push TAGS="$(DEV_RELEASE_TAGS)"
