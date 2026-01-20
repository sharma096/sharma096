from llm_client import call_llm
def generate_report(result: dict) -> str:
   prompt = f"""
Explain this migration result in simple business language:
{result}
"""
   return call_llm(prompt)