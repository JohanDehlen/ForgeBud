# ForgeBud Architecture

Version 1.0

---

# Purpose

This document defines the software architecture of ForgeBud.

Unlike the Constitution, this document may evolve as the application grows.

Every architectural decision should remain consistent with the principles defined in FORGEBUD_PRINCIPLES.md.

---

# High-Level Architecture

ForgeBud follows a layered architecture.

```
                User

                 │

                 ▼

          MainWindow (UI)

                 │

                 ▼

          Controllers

                 │

      ┌──────────┼──────────┐

      ▼          ▼          ▼

  Project     Prompt      AI

 Controller  Controller Controller

      │          │          │

      └──────────┼──────────┘

                 ▼

             Services

                 │

      ┌──────────┼──────────┐

      ▼          ▼          ▼

 FileService GitService ContextService

                 │

                 ▼

              Models

                 │

                 ▼

         Project Metadata
```

---

# Layer Responsibilities

## MainWindow

Responsibilities

- Own the application's UI.
- Manage widgets.
- Connect signals.
- Delegate work.

MainWindow should contain almost no business logic.

---

## Widgets

Widgets display information.

Examples

- ProjectPanel
- StatusBar
- Future PromptPanel
- Future AIResponsePanel

Widgets should never:

- read Git
- read files
- call AI providers

Widgets display data only.

---

## Controllers

Controllers coordinate behaviour.

Examples

ProjectController

PromptController

AIController

WorkspaceController

Controllers decide WHAT happens.

They do not perform the work themselves.

---

## Services

Services perform work.

Examples

GitService

FileService

ProjectService

ContextService

SettingsService

Future

PromptService

ValidationService

AIService

Services should never own UI.

---

## Models

Models represent data.

Examples

ProjectInfo

ReleaseManifest

ContextSummary

AIResponse

Models contain no business logic.

---

# Project Structure

```
ForgeBud/

    config/

    controllers/

    models/

    services/

    widgets/

    resources/

    tests/

    version.py

    main.py

    main_window.py
```

---

# Project Metadata

Every managed project contains:

```
.forgebud/

    project.json

    FORGEBUD_PRINCIPLES.md

    ARCHITECTURE.md

    ROADMAP.md

    PROJECT_STATE.md

    assistant_rules.md

    decisions.md

    current_task.md

    release_manifest.md
```

This directory represents the permanent memory of the project.

---

# Data Flow

Typical workflow

```
User

↓

Widget

↓

MainWindow

↓

Controller

↓

Service

↓

Model

↓

Controller

↓

Widget

↓

User
```

Data should always flow downward through the architecture.

Widgets should not bypass controllers.

---

# Dependency Rules

Allowed

MainWindow → Controllers

Controllers → Services

Controllers → Models

Services → Models

Forbidden

Widgets → Services

Widgets → Git

Widgets → AI

Services → Widgets

Models → Services

Models → Widgets

Circular dependencies

---

# AI Architecture

ForgeBud should support multiple AI providers.

The application should never depend on a single provider.

Future providers include

- ChatGPT
- Claude
- Gemini
- Grok
- DeepSeek
- OpenRouter
- Ollama

Changing providers should not require changes elsewhere in the application.

---

# Git Architecture

Git remains the source of truth.

ForgeBud enhances Git.

ForgeBud never replaces Git.

GitService should remain read-only unless a future feature explicitly requires write operations.

---

# Project Memory

The project owns its engineering knowledge.

The AI conversation is temporary.

The project documentation is permanent.

ForgeBud should always generate AI context from project memory rather than conversation history.

---

# Prompt Generation

The Prompt Builder should generate context using:

- Project metadata
- Current task
- Architecture
- Roadmap
- Changed files
- Assistant rules
- Release history

Prompt generation should never rely on memory from previous chats.

---

# Validation

Before AI-generated code is applied:

- Validate replacement files.
- Verify project structure.
- Check imports.
- Detect placeholders.
- Detect incomplete files.
- Verify architecture rules.
- Create backups when appropriate.

---

# Future Architecture

Planned components

Controllers

- ProjectController
- PromptController
- AIController
- WorkspaceController

Services

- PromptService
- ValidationService
- AIService
- BackupService
- ReleaseService
- WorkspaceService

Widgets

- PromptPanel
- AIResponsePanel
- ProjectDashboard
- ReleasePanel
- ArchitectureViewer

---

# Scalability

ForgeBud should scale from small utilities to large enterprise software projects without architectural changes.

The architecture should support:

- thousands of source files
- multiple programming languages
- multiple AI providers
- multiple repositories
- multiple workspaces

---

# Architectural Goals

Every architectural decision should improve at least one of the following:

- Maintainability
- Readability
- Simplicity
- Reliability
- Testability
- Extensibility
- Consistency

If a change does not improve one of these qualities, it should be reconsidered.

---

# Final Architectural Principle

The architecture exists to make future development easier.

Every release should leave the project easier to understand than it was before.