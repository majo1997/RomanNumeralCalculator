import unittest
from roman_to_arabic import convert_to_arabic, CONVERSION_FAILED


class TestRomanToArabicMethods(unittest.TestCase):
	def test_i_lowercase(self):
		self.assertEqual(convert_to_arabic('i'), CONVERSION_FAILED)
		
	def test_I(self):
		self.assertEqual(convert_to_arabic('I'), 1)
		
	def test_V(self):
		self.assertEqual(convert_to_arabic('V'), 5)
		
	def test_X(self):
		self.assertEqual(convert_to_arabic('X'), 10)
		
	def test_L(self):
		self.assertEqual(convert_to_arabic('L'), 50)
		
	def test_C(self):
		self.assertEqual(convert_to_arabic('C'), 100)
		
	def test_D(self):
		self.assertEqual(convert_to_arabic('D'), 500)
		
	def test_M(self):
		self.assertEqual(convert_to_arabic('M'), 1000)
		
	def test_wrong_character(self):
		self.assertEqual(convert_to_arabic('d'), CONVERSION_FAILED)
		
	def test_empty(self):
		self.assertEqual(convert_to_arabic(''), CONVERSION_FAILED)
		
	def test_MMMM(self):
		self.assertEqual(convert_to_arabic('MMMM'), CONVERSION_FAILED)

	def test_II(self):
		self.assertEqual(convert_to_arabic('II'), 2)
		
	def test_III(self):
		self.assertEqual(convert_to_arabic('III'), 3)
		
	def test_IIII(self):
		self.assertEqual(convert_to_arabic('IIII'), CONVERSION_FAILED)
		
	def test_VIII(self):
		self.assertEqual(convert_to_arabic('VIII'), 8)
		
	def test_VIIII(self):
		self.assertEqual(convert_to_arabic('VIIII'), CONVERSION_FAILED)
		
	def test_XIII(self):
		self.assertEqual(convert_to_arabic('XIII'), 13)
	
	def test_VIVI(self):
		self.assertEqual(convert_to_arabic('VIVI'), CONVERSION_FAILED)	
	
	def test_IVIXI(self):
		self.assertEqual(convert_to_arabic('IVIXI'), CONVERSION_FAILED)
		
	def test_IVIX(self):
		self.assertEqual(convert_to_arabic('IVIX'), CONVERSION_FAILED)
		
	def test_IXIV(self):
		self.assertEqual(convert_to_arabic('IXIV'), CONVERSION_FAILED)
		
	def test_IVI(self):
		self.assertEqual(convert_to_arabic('IVI'), CONVERSION_FAILED)
		
	def test_MMMCMXCIX(self):
		self.assertEqual(convert_to_arabic('MMMCMXCIX'), 3999)
		
	def test_VIV(self):
		self.assertEqual(convert_to_arabic('VIV'), CONVERSION_FAILED)
		
	def test_LXL(self):
		self.assertEqual(convert_to_arabic('LXL'), CONVERSION_FAILED)
		
	def test_DCD(self):
		self.assertEqual(convert_to_arabic('DCD'), CONVERSION_FAILED)
		
	def test_IXV(self):
		self.assertEqual(convert_to_arabic('IXV'), CONVERSION_FAILED)

	def test_VIX(self):
		self.assertEqual(convert_to_arabic('VIX'), CONVERSION_FAILED)

	def test_V_space(self):
		self.assertEqual(convert_to_arabic('V '), CONVERSION_FAILED)

	def test_VI_space(self):
		self.assertEqual(convert_to_arabic('V I'), CONVERSION_FAILED)

	def test_XXi_(self):
		self.assertEqual(convert_to_arabic('XXi'), CONVERSION_FAILED)
		

if __name__ == '__main__':
	unittest.main()
