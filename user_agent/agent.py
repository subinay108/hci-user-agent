from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

shopping_agent = RemoteA2aAgent(
    name="shopping_agent",
    description="Agent that perform shopping at ecommerce platform",
    agent_card=(
        f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, you have a subagent called shopping_agent which you can delegate tasks',
    sub_agents=[shopping_agent]
)
