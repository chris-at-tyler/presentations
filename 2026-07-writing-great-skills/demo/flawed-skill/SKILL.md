---
name: commit-helper
description: Helps write commit messages. Use when the user wants to write a commit message, needs to commit changes, asks for help committing, wants to make a commit, mentions git commits, or is committing code.
---

# Commit Helper

This skill helps you write good commit messages. Good commit messages are
important for maintainability and collaboration. Git is a distributed version
control system where every commit is a node in a directed acyclic graph, and
each node points to a tree object representing the state of the repository.
Understanding this model helps you appreciate why commit messages matter.

Always be helpful, clear, and accurate when writing commit messages.

Keep the subject line under 50 characters.

## Guidelines

- Don't write vague commit messages.
- Never use the passive voice in the subject line.
- Avoid being verbose in the body.
- Remember: the subject line should be kept short.
- Use conventional commit prefixes since the Jenkins pipeline parses them
  (note: we moved off Jenkins last year, keeping this just in case)
- TODO: update this section after the GitLab migration finishes (2024)

## Steps

1. Look at the changes.
2. Write the message.
3. Review the message until it looks good.

Note: subject lines must be brief — fifty characters maximum is the rule to
follow here.
