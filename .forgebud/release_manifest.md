# Release Manifest

## Release

Version: **v0.11.0**

Name: **Engineering Context Foundation**

Status: **Completed**

---

# Goal

Establish the provider-independent Engineering Context as the canonical representation of a software project's engineering state.

This release replaces AI-specific terminology with architecture that supports any current or future consumer.

---

# Features Delivered

- EngineeringContext model
- EngineeringContextService
- EngineeringContextSerializer
- Provider-independent engineering terminology
- Repository-state integration
- Project-memory aggregation
- Deterministic Markdown serialization
- Compatibility aliases for previous AIContext names
- End-to-end Engineering Context generation

---

# Files Added

- `models/engineering_context.py`
- `services/engineering_context_service.py`
- `services/engineering_context_serializer.py`

---

# Files Modified

- `models/ai_context.py`
- `services/context_serializer_service.py`

---

# Files Removed

- `services/context_generation_service.py`

---

# Architecture

ForgeBud now uses the following knowledge pipeline:

```
Repository
      │
      ▼
Project Memory
      │
      ▼
Engineering Context
      │
      ├── AI Providers
      ├── Documentation
      ├── Reports
      ├── Search
      ├── Automation
      └── Future Consumers
```

The Engineering Context is now the single provider-independent representation of project knowledge.

---

# Validation Performed

## Compilation

Passed.

## Runtime

Passed.

Verified:

- EngineeringContext construction
- EngineeringContext serialization
- Repository metadata
- Project Summary
- Current Task
- Coding Standards
- Engineering Decisions
- Release Manifest
- Project Validation
- Voiceanator end-to-end context generation
- Repository-wide deprecated-name search
- Full ForgeBud compilation

---

# Compatibility

Temporary compatibility modules remain:

- `models/ai_context.py`
- `services/context_serializer_service.py`

These preserve backwards compatibility while the project transitions to Engineering Context terminology.

They may be removed during a future cleanup release.

---

# Design Decisions

During implementation the project architecture evolved.

The former concept of an **AI Context** was generalized into an **Engineering Context**.

This better reflects the long-term architecture because the same project knowledge can be consumed by:

- AI providers
- Documentation
- Analytics
- Search
- Reporting
- Automation

without changing the Engineering Context itself.

---

# Known Issues

None.

---

# Release State

Implementation Complete

Compilation Passed

Runtime Validation Passed

Documentation Synchronized

Ready for Commit

Ready for Push

---

# Next Release

Following repository synchronization:

1. Re-read every `.forgebud` document.
2. Inspect the roadmap.
3. Select the next Milestone 3 objective.
4. Produce the next release specification.
5. Continue the one-file workflow.

The Engineering Context foundation is complete.