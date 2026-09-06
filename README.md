# GenPark AI Agent Skill - Verbal Reflexion Loop

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Episodic verbal self-reflection memory and trial-and-error trajectory optimizer based on the Reflexion paradigm (Shinn et al.).

```mermaid
flowchart TD
    A[Agent Action Trajectory] --> B{Trial Success?}
    B -->|Yes| C[Task Completed]
    B -->|No| D[Reflexion Critique Generator]
    D --> E[Episodic Memory Buffer]
    E --> F[Injected Reflection Prompt]
    F --> A
```

## Features
- **Root Cause Categorization**: Automatically diagnoses timeout, dependency, and formatting errors.
- **Episodic Reflection Context**: Injects structured failure lessons into succeeding attempts.
- **Zero Dependencies**: Pure Python 3.9+ standard library.

## Quickstart
```python
from client import AgentReflexionLoopClient

reflexion = AgentReflexionLoopClient()
r = reflexion.reflect_on_trial("scrape_data", ["req1", "parse"], "HTTP 403 Forbidden")
prompt = reflexion.format_reflection_prompt_prefix()
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
