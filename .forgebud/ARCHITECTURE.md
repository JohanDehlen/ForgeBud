# ForgeBud Architecture

Version 2.0

---

# Purpose

This document describes the architectural design of ForgeBud.

It defines how the application is organized, how responsibilities are separated, and how future features should integrate with the existing system.

This document describes *how* ForgeBud is built.

The roadmap describes *what* ForgeBud will become.

---

# Architectural Principles

ForgeBud follows several fundamental principles.

## Repository First

The software project is always the source of truth.

ForgeBud never invents project state.

Everything shown by ForgeBud is derived from the repository.

---

## Read Before Write

All services inspect existing project state before making changes.

ForgeBud never blindly overwrites project data.

---

## Separation of Responsibilities

Every layer has one responsibility.

Models store data.

Services perform work.

Controllers coordinate workflows.

Widgets display information.

MainWindow composes the UI.

---

## Provider Independence

ForgeBud is independent of any AI provider.

ChatGPT, Claude, Gemini, Ollama, OpenRouter, and future providers are consumers of Engineering Context.

The application architecture must never depend upon a specific AI.

---

# Layered Architecture

ForgeBud consists of five major layers.

```
Repository
      │
      ▼
Project Memory
      │
      ▼
Engineering Context
      │
      ▼
Consumers
      │
      ▼
Presentation
```

---

# Layer 1 — Repository

The repository is the permanent source of truth.

It contains:

- Source code
- Project files
- Git history
- ForgeBud project memory

No layer above the repository owns project state.

---

# Layer 2 — Project Memory

Project Memory stores long-term engineering knowledge.

Current documents include:

- Project Summary
- Current Task
- Coding Standards
- Engineering Decisions
- Release Manifest

These documents describe the project independently of any AI conversation.

---

# Layer 3 — Engineering Context

The Engineering Context is the canonical representation of project knowledge.

It combines:

- Project metadata
- Repository context
- Project Summary
- Current Task
- Coding Standards
- Engineering Decisions
- Release Manifest
- Project Validation

Engineering Context is read-only.

It contains no business logic.

It is derived entirely from repository state.

---

# Layer 4 — Consumers

Consumers use Engineering Context without modifying it.

Current consumers include:

- Markdown serialization

Future consumers include:

- Prompt generation
- ChatGPT
- Claude
- Gemini
- Ollama
- OpenRouter
- Documentation
- Reports
- Search
- Analytics
- Automation

All consumers receive the same Engineering Context.

---

# Layer 5 — Presentation

Presentation includes:

- Widgets
- MainWindow
- Dialogs
- Status displays
- Future dashboards

Presentation never constructs Engineering Context.

Presentation requests information from controllers.

---

# Controllers

Controllers coordinate workflows.

Responsibilities include:

- Project initialization
- Project loading
- Dashboard updates
- Validation
- Future context generation
- Future AI workflows

Controllers contain workflow logic but not UI code.

---

# Services

Services perform all business logic.

Typical services include:

- ProjectService
- GitService
- ValidationService
- EngineeringContextService

Services may depend upon other services.

Services do not depend upon widgets.

---

# Models

Models represent state only.

Examples include:

- ProjectInfo
- ProjectSummary
- CurrentTask
- CodingStandards
- Decisions
- ReleaseManifest
- ProjectValidation
- EngineeringContext

Models contain no workflow logic.

---

# Widgets

Widgets display information.

Widgets emit user actions.

Widgets do not modify project state directly.

---

# MainWindow

MainWindow composes the user interface.

Responsibilities include:

- Window layout
- Dock management
- Toolbar management
- Menu actions
- Widget coordination

Business logic belongs elsewhere.

---

# Context Generation

Engineering Context generation follows this workflow:

```
Repository
        │
        ▼
Project Services
        │
        ▼
EngineeringContextService
        │
        ▼
EngineeringContext
        │
        ▼
EngineeringContextSerializer
```

Generation is always read-only.

---

# Validation

Validation occurs before future AI-assisted workflows.

Validation verifies:

- Project initialization
- Required project-memory documents
- Metadata
- Repository state

Validation never modifies the project.

---

# AI Architecture

ForgeBud does not communicate directly with AI models.

Future provider layers will receive Engineering Context.

Example:

```
EngineeringContext
        │
        ▼
Prompt Builder
        │
        ▼
Provider Layer
        │
 ┌──────┼────────┬────────┬────────┐
 │      │        │        │
GPT   Claude   Gemini  Ollama  OpenRouter
```

Providers are interchangeable.

---

# Dependency Rules

Allowed dependencies:

Widgets

↓

Controllers

↓

Services

↓

Models

Services may use other services.

Models never depend upon services.

Widgets never depend upon services directly unless explicitly designed for passive display.

---

# Future Extensions

Future milestones may add:

- Multiple serializers
- JSON export
- XML export
- Token estimation
- AI provider abstraction
- Safe response analysis
- Change application
- Automation
- Plugin architecture

These should build upon Engineering Context rather than bypassing it.

---

# Definition of Success

ForgeBud succeeds architecturally when:

- Repository is always the source of truth.
- Engineering Context completely represents project knowledge.
- Every consumer uses the same Engineering Context.
- AI providers remain interchangeable.
- Business logic remains separated from presentation.
- New features can be added without architectural redesign.

The architecture should remain understandable, extensible, and provider-independent for many years.