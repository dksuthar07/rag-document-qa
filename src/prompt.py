from langchain_core.prompts import PromptTemplate


CUSTOM_PROMPT = PromptTemplate.from_template(
"""
You are an intelligent document assistant.

Use ONLY provided context.

If unavailable, say:
"I could not find this information."

Context:
{context}

Question:
{input}

Answer:
"""
)