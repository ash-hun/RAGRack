from openai import OpenAI

class BaseLLM:
	def __init__(self) -> None:
		pass

class OpenAILLM(BaseLLM):
	def __init__(self):
		super().__init__()
		self.client = OpenAI()

	def invoke(self, instruction:str) -> str:
		completion = self.client.chat.completions.create(
			model="gpt-4o",
			messages=[
				{"role": "user", "content": instruction}
			]
		)

		response = completion.choices[0].message.content
		print(response)

		return response

if __name__ == '__main__':
	LLM = OpenAILLM()
	LLM.invoke('who are you?')


