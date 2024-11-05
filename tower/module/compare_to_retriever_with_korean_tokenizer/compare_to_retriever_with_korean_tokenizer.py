from kiwipiepy import Kiwi
from typing import Literal, List, Dict
from konlpy.tag import Komoran, Kkma, Okt

class Tokenizer():
	def __init__(self, type: Literal['Kiwi', 'Komoran', 'Kkma', 'Okt']) -> None:
		self.type = type

	def _kiwi_tokenizing(self, **kwargs) -> Dict:
		from kiwipiepy.utils import Stopwords
		kiwi, stopwords = Kiwi(), Stopwords()

		return {}

	def tokenizing(self, target:List, **kwargs) -> Dict:
		if self.type == 'Kiwi':
			result = self._kiwi_tokenizing(**kwargs)
		elif self.type == 'Komoran':
			print("Komoran ~~")
			result = {}
		elif self.type == 'Kkma':
			print("Kkma ~~")
			result = {}
		elif self.type == 'Okt':
			print("Okt ~~")
			result = {}

		return result


if __name__ == 'main':
	tokenizer = Tokenizer(type='Komoran')
	result = tokenizer.tokenizing(target=['hi'])