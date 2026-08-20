# Journalism — Read-First Orientation

This repository is a **personal research and information system** for structured investigation, evidence collection, analysis, modeling, retrieval, and long-term context recovery.

Its purpose is not merely to store articles or produce conventional news stories. It is intended to preserve an accumulating body of evidence and interpretation that can be revisited as new events, questions, and assignments arise.

The primary human consumer is the researcher. Machine-readable structures are also maintained so AI systems and other tools can retrieve, compare, reason across, and help extend the accumulated material.

This README is **orientation**, not universal factual authority. When a designated current record, source, registry entry, dataset, or other authority conflicts with this README, use the authority appropriate to the question and treat the mismatch here as documentation debt to reconcile.

---

## Serious Work Startup

For substantive Journalism work, use broad orientation first and then load the narrow material required for the task.

Recommended startup sequence:

1. Read this root README.
2. Identify the current **Environment**.
3. Read that Environment's local README.
4. Determine whether the work concerns a **Subject, Dossier, Story, Investigation, Source, Assignment**, or system-development task.
5. Check the Registry for current identity, routing, and Assignment state when available.
6. Read the nearest relevant durable records and source material.
7. Identify the authority appropriate to each consequential claim.
8. Preserve important new evidence, uncertainty, relationships, and conclusions in the Body rather than only in conversation.

The goal is a **coherent starting model followed by targeted retrieval**, not either extreme of loading the entire repository or entering a task with no context.

---

## Core Model

### The Body

The **Body** is the accumulated substantive material of the Journalism system.

It includes the documents, records, evidence, images, datasets, maps, Dossiers, Stories, Investigations, source artifacts, sidecars, catalogs, analyses, timelines, and other durable material that the system collects or creates.

The Body is a **logical concept spanning the repository and related resources**, not a single `body/` folder.

```text
Body
├── source material
├── observations and evidence
├── Dossiers
├── Stories
├── Investigations
├── Subjects and routing records
├── datasets / maps / images
├── structured records / sidecars
└── analysis and downstream products
```

### Environments

An **Environment** is a durable contextual world in which research can be organized and resumed.

The initial active environment is:

**Las Vegas, New Mexico**

The repository is not permanently limited to Las Vegas. Additional environments may be added when actual use justifies them.

### Subjects

A **Subject** is a durable organizational lens over the Body. It gives structure to an area of knowledge and points to relevant Dossiers, Stories, Investigations, Sources, entities, datasets, images, and other Body records.

A Subject may also expose activity state, known gaps, unresolved questions, and useful substructure.

> **Subject = structure and routing over the Body, not a private copy of the Body.**

### Dossiers

A **Dossier** concentrates durable material about a bounded object of continuing interest: an entity, institution, place, infrastructure system, program, project, event, contractor, public office, or recurring problem.

A Dossier can support many Stories and Investigations over time.

### Investigations

An **Investigation** is a bounded question-driven inquiry. It preserves both the starting and resulting state of knowledge, including sources examined, findings, unresolved issues, information added to the Body, and follow-up leads.

The current working model treats Investigation as a specialized **Assignment type**. Assignment Activities record the actual work performed.

### Stories

A **Story** is a living analytical or narrative synthesis. It consumes selected parts of the Body, evolves as events change, and may generate new research requirements when important gaps become visible.

A Story is not limited to a newspaper-style article. A report, briefing, website page, or article can later be rendered from a Story at a point in time.

### Sources

A **Source** may be a continuing information provider or a particular source artifact.

A YouTube channel, podcast, government agency, newspaper, archive, or data portal can be a continuing Source. One video, episode, report, dataset release, article, map, or interview can be a source artifact.

---

## Work Model

Research and system development are organized around **Assignments** and **Assignment Activities**.

An **Assignment** is bounded work with an objective or completion condition. Examples may include:

- Investigation;
- Collection;
- Analysis;
- Documentation;
- Validation;
- Development;
- Administrative work.

An **Assignment Activity** is an actual act performed toward an Assignment, such as searching, reading, collecting, observing, photographing, interviewing, comparing, analyzing, writing, editing, building, testing, verifying, or registering.

This distinction allows field work, desktop research, analysis, and system development to use the same basic work-history mechanism without pretending they are the same kind of Assignment.

---

## Evidence and Interpretation

Evidence should be preserved with enough provenance to determine what a source actually establishes.

Sources are not interchangeable. Official records, datasets, public communications, journalism, maps, historical records, interviews, field observations, photographs, podcasts, videos, and other materials may each be authoritative for different facts.

Keep distinct where useful:

- verified fact;
- source claim;
- observation;
- inference;
- commentary;
- provisional interpretation;
- unresolved contradiction;
- unknown.

Uncertainty should remain visible rather than being silently reconciled.

### Findings and commentary

An Investigation may contain commentary on a newspaper, podcast, YouTube channel, government statement, or other source. Commentary is legitimate analytical material, but it should remain distinguishable from findings supported by evidence.

---

## Identity and Relationships

Repository location should not be mistaken for semantic identity.

A durable identity principle for this system is:

```text
identity != name != location != hierarchy != status != implementation
```

One Body record may legitimately relate to several Subjects, Stories, Dossiers, Investigations, or Environments.

> **Repeat identifiers and locally necessary facts; centralize detailed records and analysis.**

Many important relationships will eventually be carried by Registry records, metadata, sidecars, and catalogs rather than by deeper folder nesting.

---

## Repository Organization

Current initial structure:

```text
Journalism/
├── README.md
├── repository-tree.txt
├── build_repository_tree.py
├── json-viewer.html
├── images/
├── environments/
│   └── las-vegas-new-mexico/
│       ├── README.md
│       ├── subjects/
│       ├── dossiers/
│       ├── stories/
│       ├── investigations/
│       ├── sources/
│       └── images/
├── catalogs/
├── schemas/
├── templates/
└── tools/
```

The tree is intentionally shallow. Physical folders answer **where files live**; they do not by themselves establish authority, ownership, identity, or every semantic relationship.

### Root entry points

- `README.md` — repository-wide orientation.
- `repository-tree.txt` — generated or refreshed physical structure snapshot.
- `build_repository_tree.py` — local tree generator.
- `json-viewer.html` — dependency-free JSON inspection tool.

### `environments/`

Context-specific research worlds and their local Body records.

### `catalogs/`

Aggregate discovery products. Catalogs aid retrieval but do not replace the records they index.

### `schemas/`

Machine-readable structural definitions introduced only when actual record families justify them.

### `templates/`

Reusable authoring structures for durable records.

### `tools/`

Repository-maintenance and research-support utilities.

### `images/`

Repository-wide visual assets. Environment-specific evidentiary images should normally remain within their research environment.

---

## Authority and Derived Products

Different artifacts answer different questions.

A useful general chain is:

```text
evidence / source material
        ↓
Assignment Activities / research work
        ↓
authoritative or current human-readable record
        ↓
structured sidecar where useful
        ↓
catalog / manifest
        ↓
viewer / retrieval surface
        ↓
Story, report, website, briefing, or other synthesis
```

A sidecar is a structured companion, not automatically the authority for every fact it describes.

A catalog is a discovery product, not a second source of truth.

A viewer is a presentation and retrieval layer. Displaying a record does not make the viewer authoritative for that record.

---

## Development Principle

The system should evolve through **actual research use**.

Do not create elaborate schemas, folder hierarchies, or record types merely because they are imaginable. When repeated work reveals a durable need, define the concept, test it against real material, then formalize it.

Small everyday questions can be valuable because they expose missing knowledge and weaknesses in retrieval. A useful system should become more capable each time it is used.

---

## Current Status

The repository is in its initial architecture and development stage.

The first working environment is Las Vegas, New Mexico. The initial directory structure, local orientation READMEs, JSON viewer, repository-tree tooling, and first Investigation summary template have been established.

The next major operational layer is the Registry: stable Resource identity, Assignment state, Assignment Activities, routing, and work-resumption information.
