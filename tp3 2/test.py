from yahoo_finance_plotter_final import *
import unittest

class Test(unittest.TestCase): 
        def test_rendimientos_posibles(self):
            self.assertEqual(rendimientos_posibles([1,1,7,1]), 6)  
            self.assertEqual(rendimientos_posibles([1,1,1,1]),0)
            self.assertEqual(round(rendimientos_posibles([10,11,13,1]),1),0.3)
        def test_rendimientos_diarios(self):
            self.assertEqual(rendimientos_diarios([1,1,7,1]),[0,6,(1/7)-1])
        def test_aux_rendimientos(self): # en caso de dos rendimientos maximos, toma el mas alejado en el tiempo 
            self.assertEqual(max_rend_aux([1,2,7,1], [1601559000, 1601645400, 1601904600, 1601991000]), ["2020-10-01", "2020-10-05"]) 
            self.assertEqual(max_rend_aux([1,1,7,1], [1601559000, 1601645400, 1601904600, 1601991000]), ["2020-10-02", "2020-10-05"])

unittest.main()