CONVERSION_FAILED = -9999


class UndefinedCharacterError(Exception):
	pass


class RomanNumeralNode:
	"""
	This class represent one roman numeral containing roman numeral string,
	its integer value, position where can we put this numeral, count how many
	times we can use this number.
	"""
	def __init__(
			self, numeral_string: str, numeral_value: int,
			position: int, max_count: int
		):
		self._numeral_string = numeral_string
		self._numeral_value = numeral_value
		self._position = position
		self._occurences_left = max_count
		self._children = dict()

	def __le__(self, other):
		return self._numeral_string <= other.get_numeral_string()

	def get_numeral_string(self) -> str:
		return self._numeral_string

	def is_one_character_numeral(self) -> bool:
		return len(self._numeral_string) == 1

	def get_numeral_value(self) -> int:
		return self._numeral_value

	def get_position(self) -> int:
		return self._position - 1

	def get_occurences_left(self) -> int:
		return self._occurences_left

	def decrease_occurences(self):
		self._occurences_left -= 1

	def get_child(self, character: str):
		if character in self._children.keys():
			return self._children[character]
		return None

	def add_child(self, character: str, roman_numeral):
		self._children[character] = roman_numeral


class RomanNumeralNodeTraversal:
	"""
	Class, which is used for traverse created roman numeral prefix tree.
	"""
	def __init__(self, initial_node: RomanNumeralNode):
		self._result = 0
		self._initial_node = initial_node
		self._current_node = initial_node
		self._last_position = initial_node.get_position()
		self._next_node = None

	def _add_current_node_value(self):
		self._result += self._current_node.get_numeral_value()

	def get_result(self) -> int:
		return self._result

	def get_current_node(self) -> RomanNumeralNode:
		return self._current_node

	def get_last_position(self) -> int:
		return self._last_position

	def move_to(self, character: str):
		"""
		Changes current node to next node defined by character.
		:param character: str - character, which defines the edge which can be
		used to move onto
		:raise: UndefinedCharacterError - raised if there is no edge defined
		under selected character
		"""
		if not self.can_move_to(character):
			raise UndefinedCharacterError
		self._current_node = self._current_node.get_child(character)

	def can_move_to(self, character: str) -> bool:
		"""
		Checks if there exist edge by character.
		:param character: str - character, which defines the edge which can be
		used to move onto
		:return: bool - whether edge with character exists
		"""
		next_node = self._current_node.get_child(character)
		if next_node is None:
			return False
		return True

	def update(self):
		"""
		Updates position, result and decrease number of possible occurences.
		"""
		self._last_position = self._current_node.get_position()
		self._current_node.decrease_occurences()
		self._add_current_node_value()

	def reset_to_root(self):
		"""
		Sets current node reference to prefix tree root.
		"""
		self._current_node = self._initial_node


class RomanNumeralsConverter:
	"""
	This class contain a prefix tree like structure of the roman numeral
	nodes. It also contains convert method for converting string roman numeral
	into integer.
	"""
	def __init__(self, roman_numerals_list: list):
		positions_count = max(
			roman_numeral.get_position()
			for roman_numeral in roman_numerals_list
		) + 1

		self._positions = [None] * positions_count
		self._root = RomanNumeralNode('', 0, positions_count, 0)

		for roman_numeral in roman_numerals_list:
			node = self._root
			for character in roman_numeral.get_numeral_string():
				next_node = node.get_child(character)
				if next_node is None:
					node.add_child(character, roman_numeral)
					break

				node = next_node

	def convert(self, numeral_string: str) -> int:
		"""
		Converts roman numeral to integer.
		:param numeral_string: str - string to convert
		:return: int - converted roman numeral
		"""
		node_traversal = RomanNumeralNodeTraversal(self._root)

		for character in numeral_string:
			if node_traversal.can_move_to(character):
				node_traversal.move_to(character)
			else:
				if not self._valid_current_node(node_traversal):
					return CONVERSION_FAILED

				self._process_current_node(node_traversal)
				try:
					node_traversal.reset_to_root()
					node_traversal.move_to(character)
				except UndefinedCharacterError:
					return CONVERSION_FAILED

		if not self._valid_current_node(node_traversal):
			return CONVERSION_FAILED

		node_traversal.update()

		return node_traversal.get_result()

	def _process_current_node(self, node_traversal: RomanNumeralNodeTraversal):
		"""
		Updates node traversal values and tree positions
		:param node_traversal: RomanNumeralNodeTraversal - node traversal
		"""
		node_traversal.update()

		node = node_traversal.get_current_node()
		self._update_position(node)

	def _update_position(self, node: RomanNumeralNode):
		"""
		Save current node to its specified position, if there is no other node saved.
		:param node: RomanNumeralNode - node to save
		"""
		if self._positions[node.get_position()] is None:
			self._positions[node.get_position()] = node

	def _valid_current_node(self, node_traversal: RomanNumeralNodeTraversal) -> bool:
		"""
		Checks some roman numerals rules.
		:param node_traversal: RomanNumeralNodeTraversal - node traversal
		:return: bool - state if current node is valid
		"""
		node = node_traversal.get_current_node()
		last_position = node_traversal.get_last_position()

		numeral_on_same_position = self._positions[node.get_position()]
		if numeral_on_same_position is not None and \
			numeral_on_same_position != node and \
			not self._single_character_and_less_equal(node):
			return False
		elif node == self._root:
			return False
		elif node.get_position() > last_position:
			return False
		elif node.get_occurences_left() == 0:
			return False

		return True

	def _single_character_and_less_equal(self, node: RomanNumeralNode) -> bool:
		"""
		Checks if entered node which is on the same position as the some other
		is just single character numeral like the other one, but has smaller
		numeric value.
		:param node: RomanNumeralNode - node for comparison
		:return: bool - whether nodes on the same position are single character
		numerals and current node has smaller value
		"""
		numeral_on_same_position = self._positions[node.get_position()]
		if numeral_on_same_position.is_one_character_numeral() and \
			node.is_one_character_numeral() and \
			node <= numeral_on_same_position:
			return True
		return False


def convert_to_arabic(roman_numeral: str) -> int:
	"""
	Convert roman numeral to arabic. Roman numeral string can contain
	only these uppercase characters: I, V, X, L, C, D, M.
	:param roman_numeral: str - string containing the roman number
	:return: int - converted roman number or -9999 if conversion failed
	"""
	roman_numerals_list = [
		RomanNumeralNode('M', 1000, 4, 3),
		RomanNumeralNode('D', 500, 3, 1),
		RomanNumeralNode('C', 100, 3, 3),
		RomanNumeralNode('L', 50, 2, 1),
		RomanNumeralNode('X', 10, 2, 3),
		RomanNumeralNode('V', 5, 1, 1),
		RomanNumeralNode('I', 1, 1, 3),

		RomanNumeralNode('CM', 900, 3, 1),
		RomanNumeralNode('CD', 400, 3, 1),
		RomanNumeralNode('XC', 90, 2, 1),
		RomanNumeralNode('XL', 40, 2, 1),
		RomanNumeralNode('IX', 9, 1, 1),
		RomanNumeralNode('IV', 4, 1, 1)
	]

	roman_numerals_converter = RomanNumeralsConverter(roman_numerals_list)
	result = roman_numerals_converter.convert(roman_numeral)

	return result
