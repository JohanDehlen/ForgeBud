# ForgeBud Constitution
Version 1.0

---

# Mission

ForgeBud is an AI-assisted software engineering workspace.

Its purpose is not to replace the developer.

Its purpose is to become the permanent engineering memory, workflow manager, and AI coordinator for every software project.

ForgeBud should reduce friction between developers and AI while improving software quality, consistency, maintainability, and productivity.

---

# Vision

ForgeBud is intended to become the central workspace used to build every future software project.

Examples include:

- Voiceanator
- Figured Mind
- Biblical Insights
- Future SaaS products
- Internal development tools

ForgeBud should become the first application opened when starting work on any software project.

---

# Core Philosophy

The project owns its memory.

The AI does not.

No important architectural knowledge should exist only inside an AI conversation.

Everything important belongs inside the project.

---

# Long-Term Goal

A developer should be able to open any project years later and immediately understand:

- why the project exists
- how it is structured
- what decisions were made
- what work remains
- what the AI needs to know

without searching old conversations.

---

# Primary Objectives

ForgeBud should:

- understand projects
- preserve engineering knowledge
- generate AI context
- validate AI responses
- safely apply AI-generated code
- integrate with Git
- maintain project history
- support multiple AI providers

---

# Software Architecture

ForgeBud follows strict separation of responsibilities.

Models
    Store data only.

Widgets
    Display information.
    Never perform business logic.

Controllers
    Coordinate application behaviour.

Services
    Perform work.

MainWindow
    Owns the UI.
    Delegates work to controllers.

No layer should perform another layer's responsibilities.

---

# Design Principles

Every class should have one responsibility.

Small classes are preferred over large classes.

Composition is preferred over inheritance.

Readable code is preferred over clever code.

Simple code is preferred over complex code.

Consistency is more important than personal preference.

---

# AI Development Rules

These rules are permanent.

1.
Generate COMPLETE replacement files.

Never generate snippets.

Never generate partial patches.

2.

Never guess code that has not been seen.

If required files are missing,
request them first.

3.

Do not invent APIs.

Use only APIs that exist in the project.

4.

Every generated file must compile with the existing project.

5.

Avoid placeholder implementations.

Avoid TODO comments.

Avoid fake implementations.

6.

Generate production-quality code.

Not demonstration code.

7.

Every architectural decision should reduce future complexity.

---

# Coding Standards

Use pathlib instead of os whenever practical.

Prefer type hints.

Use descriptive names.

Avoid magic numbers.

Keep methods short.

Prefer explicit code.

Write meaningful docstrings.

Avoid duplicated logic.

---

# Release Rules

Every release must begin with a release specification.

Example

Version

Goal

Files Added

Files Replaced

Files Removed

Tests

Release Notes

Only then should implementation begin.

---

# Complete Replacement Rule

ForgeBud always generates complete replacement files.

Never require manual merging.

Never require editing individual methods.

Every generated source file should be ready to copy and paste.

---

# Project Memory

Every project managed by ForgeBud contains

.forgebud/

project.json

roadmap.md

architecture.md

assistant_rules.md

coding_standards.md

current_task.md

decisions.md

known_issues.md

release_manifest.md

FORGEBUD_PRINCIPLES.md

The project should be self-documenting.

---

# Release Manifest

Every release should document

Version

Goal

Files Added

Files Changed

Files Removed

Known Issues

Tests

Release Notes

Future Work

---

# Development Workflow

Open Project

↓

Scan Project

↓

Read Project Memory

↓

Generate AI Context

↓

Developer sends prompt

↓

Receive AI response

↓

Validate response

↓

Apply replacement files

↓

Run validation

↓

Commit to Git

↓

Update Release Manifest

↓

Continue Development

---

# AI Workflow

The AI should receive:

Project Summary

Architecture

Current Task

Development Rules

Changed Files

Relevant Source Files

Release Manifest

The AI should never need previous conversations to understand the project.

---

# AI Independence

ForgeBud should support multiple AI providers.

Examples

ChatGPT

Claude

Gemini

Grok

DeepSeek

OpenRouter

Local Ollama

The project context should remain identical regardless of AI provider.

---

# Git Integration

ForgeBud should never hide Git.

Git remains the source of truth.

ForgeBud augments Git.

It does not replace Git.

---

# Safety

Before applying AI-generated code:

Validate replacement files.

Check imports.

Verify project structure.

Create backup if necessary.

Allow rollback.

Prevent accidental overwrite.

---

# Future Features

Project Summary Generator

Context Generator

Prompt Builder

Clipboard Integration

AI Response Parser

Replacement File Validator

Safe Apply

Automatic Backups

Architecture Viewer

Dependency Graph

Conversation Archive

Decision Tracker

Roadmap Manager

Plugin System

AI Provider Manager

Workspace Dashboard

Project Analytics

Release Manager

One-click Git Commit

One-click AI Context

---

# Future Vision

ForgeBud should eventually become an AI-powered software engineering workspace rather than merely a prompt generator.

The application should understand an entire project and coordinate development across multiple AI providers while preserving engineering knowledge permanently.

---

# Guiding Principle

Every feature added to ForgeBud should answer at least one question:

Does it make software development

- faster,
- safer,
- more consistent,
- easier to understand,
- or easier to maintain?

If the answer is no,

it probably does not belong in ForgeBud.

---

# Final Principle

The purpose of ForgeBud is not to write code.

The purpose of ForgeBud is to help developers build better software.

Everything else follows from that.