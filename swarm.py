from openai import OpenAI

class Swarm:
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key) if api_key else None
        
    def run(self, agent, messages):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": agent.instructions},
                    *messages
                ]
            )
            return [{"role": "assistant", "content": response.choices[0].message.content}]
        except Exception as e:
            print(f"Error calling OpenAI: {e}")
            return [{"role": "assistant", "content": "Error processing request"}]

class Agent:
    def __init__(self, name, instructions, functions=None):
        self.name = name
        self.instructions = instructions
        self.functions = functions or []