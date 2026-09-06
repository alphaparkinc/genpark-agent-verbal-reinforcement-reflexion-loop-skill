"""
Demonstration of genpark-agent-verbal-reinforcement-reflexion-loop-skill
"""

from client import AgentReflexionLoopClient

def main():
    agent_reflexion = AgentReflexionLoopClient()

    # Simulate Trial 1 Failure
    t1_steps = ["navigate_to_cart", "click_checkout_button"]
    t1_err = "TimeoutException: Checkout button element not interactable"
    r1 = agent_reflexion.reflect_on_trial("Complete E-commerce Checkout", t1_steps, t1_err)
    print("Trial 1 Reflection:", r1["critique"])

    # Simulate Trial 2 Failure
    t2_steps = ["navigate_to_cart", "dismiss_modal", "click_checkout_button", "submit_payment"]
    t2_err = "ValidationError: CVV code required"
    r2 = agent_reflexion.reflect_on_trial("Complete E-commerce Checkout", t2_steps, t2_err)
    print("\nTrial 2 Reflection:", r2["critique"])

    print("\n=== COMPILED REFLECTION PROMPT CONTEXT ===")
    print(agent_reflexion.format_reflection_prompt_prefix())

if __name__ == "__main__":
    main()
