# Robotics: Science and Systems Website

This repository contains the Jekyll-based website for the RSS conference.

Each year’s site should be archived under its own subdirectory (e.g., `/2024/`, `/2025/`), but the current year should be served from the root (even if maintaining the archived version in parallel). Note, github pages builds and serves from the repository automatically, so the site doesn't need to be built manually before pushing to the repository.

For links, use `{{ site.baseurl }}` for all internal links and assets within the current year’s site, but `{{ site.url }}` should be used when linking across years (e.g., pointing from the current site to an archived version) to avoid links of the form `/2025/2024/2023/`.

A Makefile is provided with a few helpful commands: `make serve` serves the site locally with `bundle exec jekyll serve`, and `make build YEAR=<year>` builds the site into `./<year>` with the appropriate `--baseurl` (i.e., this automatically updates `{{ site.baseurl }}` to point to the permalink).
