import re
from roman_to_arabic import convert_to_arabic, CONVERSION_FAILED

OPERATOR_SYMBOLS = '+-*/'
ROMAN_NUMERAL_CHARACTERS = 'IVXLCDM'

NEWLINE_CHARACTER = '\n'

INCORRECT_INPUT = 'Zly vstup'
OUT_OF_INTERVAL = 'Cislo mimo'

MIN_VALUE = 1
MAX_VALUE = 3999


class ArgumentOutOfIntervalError(Exception):
	"""Raised when argument is out of defined interval"""
	pass


class ResultOutOfIntervalError(Exception):
	"""Raised when result of expression is out of defined interval"""
	pass


class IncorrectExpressionFormatError(Exception):
	"""Raised when entered expression has wrong format."""
	pass


class UnknownOperatorError(Exception):
	"""There was used unknown operator in the expression"""
	pass


class RomanNumeralCalculator:
	def evaluate(self, expression: str) -> str:
		"""
		Evaluates expression and returns a result or one of defined errors.
		:param expression: str - expression to evaluate
		:return: str - calculated roman numeral value
		"""
		try:
			stripped_expression = self._remove_spaces(expression)
			
			roman_num1, op, roman_num2 = self._split_arguments(stripped_expression)
							
			int_num1 = self._to_int(roman_num1)
			int_num2 = self._to_int(roman_num2)

			int_result = self._calculate(int_num1, int_num2, op)

			roman_result = self._to_roman(int_result)
			
		except IncorrectExpressionFormatError:
			return INCORRECT_INPUT
		except UnknownOperatorError:
			return INCORRECT_INPUT
		except ArgumentOutOfIntervalError:
			return INCORRECT_INPUT
		except ResultOutOfIntervalError:
			return OUT_OF_INTERVAL
		
		return roman_result
		
	def _to_int(self, roman_numeral: str) -> int:
		"""
		Converts roman numeral to int.
		:param roman_numeral: str - numeral to convert
		:raise: ArgumentOutOfIntervalError - if conversion failed
		:return: int - converted number
		"""
		int_number = convert_to_arabic(roman_numeral)
		if int_number == CONVERSION_FAILED:
			raise ArgumentOutOfIntervalError
			
		return int_number
		
	def _remove_spaces(self, expression: str) -> str:
		"""
		Removes spaces from string and returns it.
		:param expression: str - entered expression
		:return: str - expression without space characters
		"""
		return expression.replace(' ', '')
			
	def _split_arguments(self, stripped_expression: str) -> tuple:
		"""
		Parse numerals and operator from expression.
		:param stripped_expression: str - entered expression without spaces
		:raise: IncorrectExpressionFormatError - if expression is not valid
		:raise: UnknownOperatorError - if used non-defined operator
		:return: tuple - containing first argument, operator, second argument
		"""
		if not self._is_valid(stripped_expression):
			raise IncorrectExpressionFormatError

		for op in OPERATOR_SYMBOLS:
			if op in stripped_expression:
				arguments = stripped_expression.split(op)
				if len(arguments) != 2:
					raise IncorrectExpressionFormatError
				return arguments[0], op, arguments[1]
				
		raise UnknownOperatorError

	def _to_roman(self, number: int) -> str:
		"""
		Converts int to roman number from defined interval.
		:param number: int - number to convert
		:raise: ResultOutOfIntervalError - raised when number is out of
		interval
		:return: str - roman number string
		"""
		if MIN_VALUE <= number <= MAX_VALUE:
			conversion_result = ''
			
			sorted_numerals = [
				RomanNumeral('M', 1000),
				RomanNumeral('CM', 900),
				RomanNumeral('D', 500),
				RomanNumeral('CD', 400),
				RomanNumeral('C', 100),
				RomanNumeral('XC', 90),
				RomanNumeral('L', 50),
				RomanNumeral('XL', 40),
				RomanNumeral('X', 10),
				RomanNumeral('IX', 9),
				RomanNumeral('V', 5),
				RomanNumeral('IV', 4),
				RomanNumeral('I', 1)
			]
			
			for numeral in sorted_numerals:
				while number >= numeral.get_numeral_value():
					number -= numeral.get_numeral_value()
					conversion_result += numeral.get_numeral_string()
			
			return conversion_result
		
		raise ResultOutOfIntervalError
		
	def _calculate(self, num_1: int, num_2: int, operator: str) -> int:
		"""
		Executes one of defined operations on numbers determined by operator.
		:param num_1: int - first number
		:param num_2: int - second number
		:param operator: str - operator
		:raise: UnknownOperatorError - if there is non-defined operator
		:return: int - returns result of operation
		"""
		if operator == '+':
			return num_1 + num_2
		elif operator == '-':
			return num_1 - num_2
		elif operator == '*':
			return num_1 * num_2
		elif operator == '/':
			result = num_1 // num_2

			return result
		
		raise UnknownOperatorError

	def _is_valid(self, stripped_expression: str) -> bool:
		"""
		Checks if the expression has the correct format using regular
		expression. Expression can not contain only specified roman numerals
		or defined operators. Expression can not contain newline character.
		:param stripped_expression: str - string containing expression without
		any spaces
		:return: bool - whether expression has valid format
		"""
		re_escaped_operators = re.escape(OPERATOR_SYMBOLS)
	
		expression_pattern = re.compile(
			f'^[{ROMAN_NUMERAL_CHARACTERS}]+[{re_escaped_operators}][{ROMAN_NUMERAL_CHARACTERS}]+$'
		)
		
		matched = expression_pattern.search(stripped_expression)
		if NEWLINE_CHARACTER in stripped_expression or not matched:
			return False
			
		return True


class RomanNumeral:
	def __init__(self, numeral_string: str, numeral_value: int):
		self._numeral_string = numeral_string
		self._numeral_value = numeral_value
		
	def get_numeral_string(self) -> str:
		return self._numeral_string
		
	def get_numeral_value(self) -> int:
		return self._numeral_value


def roman_numeral_calculator(expression: str) -> str:
	"""
	Evaluates and returns simple roman numeral expression with defined
	operators. Expression must have specified format:
	"[roman numeral][operator][roman numeral]", but there can be multiple
	spaces before, between or after roman numerals.
	:param: expression - expression to evaluate
	:return: str - roman numeral result of expression
	"""
	calculator = RomanNumeralCalculator()
	
	result = calculator.evaluate(expression)
	return result
