.PHONY: help build serve

help:
	@echo "Usage:"
	@echo "  make serve                 #serve the site locally"
	@echo "  make build YEAR=<year>     #build the site into ./<year> with baseurl=/<year>"

build:
	@if [ -z "$(YEAR)" ]; then \
		echo "Usage: make build YEAR=<year>"; \
		exit 1; \
	fi
	bundle exec jekyll build -d $(YEAR) --baseurl "/$(YEAR)"

serve:
	bundle exec jekyll serve
