import os
from typing import List
from pprint import pprint

class BaseModel:
	def __init__(self) -> None:
		pass

class Chunker(BaseModel):
	def __init__(self, *args, **kwargs):
		# super.__init__(*args, **kwargs)
		pass

	def chunking(self, filepath:str, tag_list:List=['<image>', '<table>']):
		with open(filepath, 'r', encoding='utf-8') as file:
			lines = file.readlines()

		idx = 0
		results = {}
		current_type = None
		content_buffer = []

		for line in lines:
			stripped_line = line.strip()
			stripped_line = stripped_line.replace('\n', '')

			if stripped_line != '':
				if stripped_line in tag_list:
					if current_type in tag_list:
						content_buffer.append(stripped_line)

						content = '\n'.join(content_buffer)
						results[idx] = {'type': stripped_line, 'content': content}
						idx += 1
						current_type = None
						content_buffer = []
					else:
						current_type = stripped_line
						content_buffer = [stripped_line]
				else:
					if current_type in tag_list:
						content_buffer.append(line.rstrip())
					else:
						results[idx] = {'type': 'text', 'content': stripped_line}
						idx += 1

		if content_buffer:
			content = ' '.join(content_buffer).strip()
			if content:
				results[idx] = {'type': current_type, 'content': content}

		return results


if __name__ == '__main__':
	PATH = "data/sample01.txt"
	chunk_dict = Chunker().chunking(filepath=PATH)
