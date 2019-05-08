from unittest import main, TestCase
import WorksheetGenerator as generator

class MyUnitTests(TestCase):
	def test_baseConverter_2(self):
		self.assertEqual(generator.baseConverter(5,2), "101")
		self.assertEqual(generator.baseConverter(2,2), "10")
	def test_baseConverter_3(self):
		self.assertEqual(generator.baseConverter(7,3), "21")
		self.assertEqual(generator.baseConverter(3,3), "10")
	def test_baseConverter_4(self):
		self.assertEqual(generator.baseConverter(12,4), "30")
		self.assertEqual(generator.baseConverter(4,4), "10")
	def test_baseConverter_5(self):
		self.assertEqual(generator.baseConverter(17,5), "32")
		self.assertEqual(generator.baseConverter(5,5), "10")
	def test_baseConverter_6(self):
		self.assertEqual(generator.baseConverter(77,6), "205")
		self.assertEqual(generator.baseConverter(6,6), "10")
	def test_baseConverter_7(self):
		self.assertEqual(generator.baseConverter(18,7), "24")
		self.assertEqual(generator.baseConverter(7,7), "10")
	def test_baseConverter_8(self):
		self.assertEqual(generator.baseConverter(91,8), "133")
		self.assertEqual(generator.baseConverter(8,8), "10")
	def test_baseConverter_9(self):
		self.assertEqual(generator.baseConverter(56,9), "62")
		self.assertEqual(generator.baseConverter(9,9), "10")
	def test_baseConverter_10(self):
		self.assertEqual(generator.baseConverter(101,10), "101")
		self.assertEqual(generator.baseConverter(10,10), "10")
	def test_baseConverter_11(self):
		self.assertEqual(generator.baseConverter(84, 11), "77")
		self.assertEqual(generator.baseConverter(11,11), "10")
	def test_baseConverter_12(self):
		self.assertEqual(generator.baseConverter(23,12), "1B")
		self.assertEqual(generator.baseConverter(12,12), "10")
	def test_baseConverter_13(self):
		self.assertEqual(generator.baseConverter(143,13), "B0")
		self.assertEqual(generator.baseConverter(13,13), "10")
	def test_baseConverter_14(self):
		self.assertEqual(generator.baseConverter(101,14), "73")
		self.assertEqual(generator.baseConverter(14,14), "10")
	def test_baseConverter_15(self):
		self.assertEqual(generator.baseConverter(927,15), "41C")
		self.assertEqual(generator.baseConverter(15,15), "10")
	def test_baseConverter_16(self):
		self.assertEqual(generator.baseConverter(256,16), "100")
		self.assertEqual(generator.baseConverter(16,16), "10")

	def test_toBaseTen_dif1(self):
		print("%%%%%% toBaseTen dif 1 %%%%%%")
		print("\n" + generator.toBaseTen(1) +"\n")
	def test_toBaseTen_dif2(self):
		print("%%%%%% toBaseTen dif 2 %%%%%%")
		print("\n" + generator.toBaseTen(2) +"\n")
	def test_toBaseTen_dif3(self):
		print("%%%%%% toBaseTen dif 3 %%%%%%")
		print("\n" + generator.toBaseTen(3) +"\n")
	def test_toBaseTen_dif4(self):
		print("%%%%%% toBaseTen dif 4 %%%%%%")
		print("\n" + generator.toBaseTen(4) +"\n")
	def test_toBaseTen_dif5(self):
		print("%%%%%% toBaseTen dif 5 %%%%%%")
		print("\n" + generator.toBaseTen(5) +"\n")


	def test_baseConversion_dif1(self):
		print("%%%%%% baseConversion dif 1 %%%%%%")
		print("\n" + generator.baseConversion(1) +"\n")
	def test_baseConversion_dif2(self):
		print("%%%%%% baseConversion dif 2 %%%%%%")
		print("\n" + generator.baseConversion(2) +"\n")
	def test_baseConversion_dif3(self):
		print("%%%%%% baseConversion dif 3 %%%%%%")
		print("\n" + generator.baseConversion(3) +"\n")
	def test_baseConversion_dif4(self):
		print("%%%%%% baseConversion dif 4 %%%%%%")
		print("\n" + generator.baseConversion(4) +"\n")
	def test_baseConversion_dif5(self):
		print("%%%%%% baseConversion dif 5 %%%%%%")
		print("\n" + generator.baseConversion(5) +"\n")


	def test_singleIfWkst_dif1(self):
		print("%%%%%% singleIfWkst dif 1 %%%%%%")
		print("\n" + generator.singleIfWkst(1) +"\n")
	def test_singleIfWkst_dif2(self):
		print("%%%%%% singleIfWkst dif 2 %%%%%%")
		print("\n" + generator.singleIfWkst(2) +"\n")
	def test_singleIfWkst_dif3(self):
		print("%%%%%% singleIfWkst dif 3 %%%%%%")
		print("\n" + generator.singleIfWkst(3) +"\n")
	def test_singleIfWkst_dif4(self):
		print("%%%%%% singleIfWkst dif 4 %%%%%%")
		print("\n" + generator.singleIfWkst(4) +"\n")
	def test_singleIfWkst_dif5(self):
		print("%%%%%% singleIfWkst dif 5 %%%%%%")
		print("\n" + generator.singleIfWkst(5) +"\n")


	def test_IfElseWkst_dif1(self):
		print("%%%%%% IfElseWkst dif 1 %%%%%%")
		print("\n" + generator.IfElseWkst(1) +"\n")
	def test_IfElseWkst_dif2(self):
		print("%%%%%% IfElseWkst dif 2 %%%%%%")
		print("\n" + generator.IfElseWkst(2) +"\n")
	def test_IfElseWkst_dif3(self):
		print("%%%%%% IfElseWkst dif 3 %%%%%%")
		print("\n" + generator.IfElseWkst(3) +"\n")
	def test_IfElseWkst_dif4(self):
		print("%%%%%% IfElseWkst dif 4 %%%%%%")
		print("\n" + generator.IfElseWkst(4) +"\n")
	def test_IfElseWkst_dif5(self):
		print("%%%%%% IfElseWkst dif 5 %%%%%%")
		print("\n" + generator.IfElseWkst(5) +"\n")


	def test_IfElseIfElseWkst_dif1(self):
		print("%%%%%% IfElseIfElseWkst dif 1 %%%%%%")
		print("\n" + generator.IfElseIfElseWkst(1) +"\n")
	def test_IfElseIfElseWkst_dif2(self):
		print("%%%%%% IfElseIfElseWkst dif 2 %%%%%%")
		print("\n" + generator.IfElseIfElseWkst(2) +"\n")
	def test_IfElseIfElseWkst_dif3(self):
		print("%%%%%% IfElseIfElseWkst dif 3 %%%%%%")
		print("\n" + generator.IfElseIfElseWkst(3) +"\n")
	def test_IfElseIfElseWkst_dif4(self):
		print("%%%%%% IfElseIfElseWkst dif 4 %%%%%%")
		print("\n" + generator.IfElseIfElseWkst(4) +"\n")
	def test_IfElseIfElseWkst_dif5(self):
		print("%%%%%% IfElseIfElseWkst dif 5 %%%%%%")
		print("\n" + generator.IfElseIfElseWkst(5) +"\n")


	def test_StringMethodProblems_dif1(self):
		print("%%%%%% StringMethodProblems dif 1 %%%%%%")
		print("\n" + generator.StringMethodProblems(1) +"\n")
	def test_StringMethodProblems_dif2(self):
		print("%%%%%% StringMethodProblems dif 2 %%%%%%")
		print("\n" + generator.StringMethodProblems(2) +"\n")
	def test_StringMethodProblems_dif3(self):
		print("%%%%%% StringMethodProblems dif 3 %%%%%%")
		print("\n" + generator.StringMethodProblems(3) +"\n")
	def test_StringMethodProblems_dif4(self):
		print("%%%%%% StringMethodProblems dif 4 %%%%%%")
		print("\n" + generator.StringMethodProblems(4) +"\n")
	def test_StringMethodProblems_dif5(self):
		print("%%%%%% StringMethodProblems dif 5 %%%%%%")
		print("\n" + generator.StringMethodProblems(5) +"\n")


	def test_classProblems_dif1(self):
		try:
			generator.classProblems(1)
			assert False
		except:
			assert True
	def test_classProblems_dif2(self):
		try:
			generator.classProblems(2)
			assert False
		except:
			assert True
	def test_classProblems_dif3(self):
		try:
			generator.classProblems(3)
			assert False
		except:
			assert True
	def test_classProblems_dif4(self):
		try:
			generator.classProblems(4)
			assert False
		except:
			assert True
	def test_classProblems_dif5(self):
		try:
			generator.classProblems(5)
			assert False
		except:
			assert True


	def test_arrayIteration_dif1(self):
		print("%%%%%% arrayIteration dif 1 %%%%%%")
		print("\n" + generator.arrayIteration(1) +"\n")

	def test_arrayIteration_dif2(self):
		print("%%%%%% arrayIteration dif 2 %%%%%%")
		print("\n" + generator.arrayIteration(2) +"\n")
	def test_arrayIteration_dif3(self):
		print("%%%%%% arrayIteration dif 3 %%%%%%")
		print("\n" + generator.arrayIteration(3) +"\n")
"""
	def test_arrayIteration_dif4(self):
		pass
	def test_arrayIteration_dif5(self):
		pass


	def test_simpleRecur_dif1(self):
		pass
	def test_simpleRecur_dif2(self):
		pass
	def test_simpleRecur_dif3(self):
		pass
	def test_simpleRecur_dif4(self):
		pass
	def test_simpleRecur_dif5(self):
		pass
"""
if __name__ == "__main__":
	main()