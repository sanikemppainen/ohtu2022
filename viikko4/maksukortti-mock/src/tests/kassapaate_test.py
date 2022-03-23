import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()
    
    def ei_lisaa_rahaa_jos_summa_negatiivinen(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.lataa(maksukortti_mock,-15)

        maksukortti_mock.osta.assert_not_called()
    
    def lisaa_rahaa_jos_on_positiivinen_summa(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.lataa(maksukortti_mock,15)

        maksukortti_mock.assert_called_with(25)