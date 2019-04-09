from unittest import main, TestCase
import outputGenerator as out

class MyUnitTests(TestCase):
	def test_baseSolver_2(self):
		self.assertEqual(out.baseSolver("101", 2), 5)
	def test_baseSolver_3(self):
		self.assertEqual(out.baseSolver("202", 3), 20)
	def test_baseSolver_4(self):
		self.assertEqual(out.baseSolver("303", 4), 51)
	def test_baseSolver_5(self):
		self.assertEqual(out.baseSolver("404", 5), 104)
	def test_baseSolver_6(self):
		self.assertEqual(out.baseSolver("505", 6), 185)
	def test_baseSolver_7(self):
		self.assertEqual(out.baseSolver("606", 7), 300)
	def test_baseSolver_8(self):
		self.assertEqual(out.baseSolver("707", 8), 455)
	def test_baseSolver_9(self):
		self.assertEqual(out.baseSolver("808", 9), 656)
	def test_baseSolver_10(self):
		self.assertEqual(out.baseSolver("909", 10), 909)
	def test_baseSolver_11(self):
		self.assertEqual(out.baseSolver("A0A", 11), 1220)
	def test_baseSolver_12(self):
		self.assertEqual(out.baseSolver("B0B", 12), 1595)
	def test_baseSolver_13(self):
		self.assertEqual(out.baseSolver("C0C", 13), 2040)
	def test_baseSolver_14(self):
		self.assertEqual(out.baseSolver("D0D", 14), 2561)
	def test_baseSolver_15(self):
		self.assertEqual(out.baseSolver("E0E", 15), 3164)
	def test_baseSolver_16(self):
		self.assertEqual(out.baseSolver("F0F", 16), 3855)

if __name__ == "__main__":
	main()