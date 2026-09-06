"""
Agent Verbal Reinforcement Reflexion Loop and Episodic Self-Correction Memory.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional

class AgentReflexionLoopClient:
    """
    Implements the Reflexion framework (Shinn et al.):
    - Evaluates agent execution trajectories against task success criteria
    - Generates verbal self-reflections on failures (root causes, missed assumptions)
    - Persists episodic reflections to working memory to steer future trial attempts
    """

    def __init__(self, max_reflections: int = 5):
        self.max_reflections = max_reflections
        self.reflection_memory = []

    def reflect_on_trial(self, task_goal: str, trajectory_steps: List[str], error_message: str) -> Dict[str, Any]:
        """
        Synthesizes a structured verbal reflection from a failed attempt trajectory.
        """
        last_step = trajectory_steps[-1] if trajectory_steps else "initialization"
        
        # Heuristic root-cause analysis
        root_cause = "logic_error"
        if "timeout" in error_message.lower():
            root_cause = "execution_timeout"
        elif "not found" in error_message.lower() or "missing" in error_message.lower():
            root_cause = "missing_dependency_or_resource"
        elif "syntax" in error_message.lower() or "parse" in error_message.lower():
            root_cause = "formatting_or_syntax_flaw"

        critique = (
            f"Failed at step '{last_step}' while attempting to achieve '{task_goal}'. "
            f"Error encountered: '{error_message}'. "
            f"Root cause category: {root_cause}. "
            f"Action plan for next trial: Avoid repeating '{last_step}' directly without pre-checking prerequisite state."
        )

        reflection_entry = {
            "trial_index": len(self.reflection_memory) + 1,
            "task_goal": task_goal,
            "root_cause": root_cause,
            "critique": critique
        }

        self.reflection_memory.append(reflection_entry)
        if len(self.reflection_memory) > self.max_reflections:
            self.reflection_memory.pop(0)

        return reflection_entry

    def format_reflection_prompt_prefix(self) -> str:
        """Formats accumulated reflections into system prompt context for next trial."""
        if not self.reflection_memory:
            return ""

        lines = ["=== PAST TRIAL LESSONS & SELF-REFLECTIONS ==="]
        for r in self.reflection_memory:
            lines.append(f"[Trial {r['trial_index']}]: {r['critique']}")
        lines.append("Use the above reflections to avoid previous failure modes.
")
        return chr(10).join(lines)
