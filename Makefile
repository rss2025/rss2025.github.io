build:
	bundle exec jekyll build -d 2025

serve:
	bundle exec jekyll serve

serve-nowatch:
	bundle exec jekyll serve --no-watch

.PHONY: build serve
