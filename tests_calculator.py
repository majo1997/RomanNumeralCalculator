import unittest
from roman_calculator import roman_numeral_calculator, INCORRECT_INPUT, \
	OUT_OF_INTERVAL


class TestRomanToArabicMethodss(unittest.TestCase):
	def test_addition_spaces2(self):
		self.assertEqual(roman_numeral_calculator(' XI + I X '), 'XX')
		
	def test_division2(self):
		self.assertEqual(roman_numeral_calculator('XXV/V'), 'V')
		
	def test_subtraction2(self):
		self.assertEqual(roman_numeral_calculator('MMCDXLIV-MCCXXII'), 'MCCXXII')
		
	def test_one_number(self):
		self.assertEqual(roman_numeral_calculator(' MD '), INCORRECT_INPUT)
		
	def test_division_float_result(self):
		self.assertEqual(roman_numeral_calculator('MCDXLIV / MCDXLV'), OUT_OF_INTERVAL)
		
	def test_out_of_range_input(self):
		self.assertEqual(roman_numeral_calculator(' MMMM + I'), INCORRECT_INPUT)
		
	def test_out_of_range_higher(self):
		self.assertEqual(roman_numeral_calculator('MMM + M'), OUT_OF_INTERVAL)
		
	def test_unknown_operator(self):
		self.assertEqual(roman_numeral_calculator('MM @ I'), INCORRECT_INPUT)

		
	def test_empty_expression(self):
		self.assertEqual(roman_numeral_calculator(''), INCORRECT_INPUT)
		
	def test_just_spaces_expression(self):
		self.assertEqual(roman_numeral_calculator('       '), INCORRECT_INPUT)
		
	def test_spaces_with_operator(self):
		self.assertEqual(roman_numeral_calculator('   +    '), INCORRECT_INPUT)
		
	def test_spaces_with_operator2(self):
		self.assertEqual(roman_numeral_calculator('  *  '), INCORRECT_INPUT)
		
	def test_multiple_operators(self):
		self.assertEqual(roman_numeral_calculator('  +*  '), INCORRECT_INPUT)
		
	def test_multiple_operators2(self):
		self.assertEqual(roman_numeral_calculator('-+*'), INCORRECT_INPUT)
		
	def test_one_number_with_operator(self):
		self.assertEqual(roman_numeral_calculator('XX-'), INCORRECT_INPUT)
		
	def test_one_number_with_operator2(self):
		self.assertEqual(roman_numeral_calculator('*MX'), INCORRECT_INPUT)

	def test_addition(self):
		self.assertEqual(roman_numeral_calculator('I+I'), 'II')
		
	def test_addition_multiple_operators(self):
		self.assertEqual(roman_numeral_calculator('I+I+I'), INCORRECT_INPUT)
		
	def test_addition2(self):
		self.assertEqual(roman_numeral_calculator('VIII+I'), 'IX')
		
	def test_addition_spaces(self):
		self.assertEqual(roman_numeral_calculator(' V  +   V '), 'X')
		
	def test_addition_spaces_more_numerals(self):
		self.assertEqual(roman_numeral_calculator(' V  +   V III '), 'XIII')
		
	def test_subtraction(self):
		self.assertEqual(roman_numeral_calculator('CD-CC'), 'CC')
		
	def test_subtraction_spaces(self):
		self.assertEqual(roman_numeral_calculator('   M C  M     - M '), 'CM')
		
	def test_multiplication(self):
		self.assertEqual(roman_numeral_calculator('VII*V'), 'XXXV')
		
	def test_multiplication_spaces(self):
		self.assertEqual(roman_numeral_calculator('  I I    I* XX   X'), 'XC')
		
	def test_division(self):
		self.assertEqual(roman_numeral_calculator('MMM/M'), 'III')
		
	def test_division_spaces(self):
		self.assertEqual(roman_numeral_calculator('   X X IV /VIII '), 'III')
		
	def test_out_of_range_higher2(self):
		self.assertEqual(roman_numeral_calculator('MMMCMXCIX+I'), OUT_OF_INTERVAL)
		
	def test_out_of_range_lower(self):
		self.assertEqual(roman_numeral_calculator('XI-XI'), OUT_OF_INTERVAL)
		
	def test_out_of_range_negative(self):
		self.assertEqual(roman_numeral_calculator('XI-MM'), OUT_OF_INTERVAL)

	def test_out_of_range_input2(self):
		self.assertEqual(roman_numeral_calculator('I+ MMMM'), INCORRECT_INPUT)

	def test_out_of_range_input3(self):
		self.assertEqual(roman_numeral_calculator('MMMMII+ MMMMIII'), INCORRECT_INPUT)


if __name__ == '__main__':
	unittest.main()
