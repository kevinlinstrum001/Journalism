# Tools

## Purpose

This directory contains repository-support tooling: generators, validators, converters, catalog builders, import/export helpers, and other utilities used to maintain or inspect the Journalism Body.

User-facing or repository-wide entry points may remain at the repository root when that location materially improves discovery. For example, the current JSON Viewer is intentionally rooted at `json-viewer.html`.

## Tooling principles

- Tools should not become hidden semantic authorities.
- Generated output should identify its source inputs where practical.
- A generator, manifest, catalog, or viewer is part of a dependency chain and should be changed with downstream consumers in mind.
- Keep utilities simple until actual research work demonstrates a need for greater automation.
