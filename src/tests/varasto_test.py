import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varastoVirheSaldo = Varasto(1, -1)
        self.varastoVirheTilavuus  = Varasto(-1, 0)
        self.varastoYliTayteen  = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_korjaa_tilan(self):
        self.assertAlmostEqual(self.varastoVirheTilavuus.paljonko_mahtuu(), 0)

    def test_konstruktori_korjaa_alku_saldon(self):
        self.assertAlmostEqual(self.varastoVirheSaldo.saldo, 0)

    def test_konstruktori_korjaa_yli_taytetyn(self):
        self.assertAlmostEqual(self.varastoYliTayteen.saldo, 5)
    
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_yritetaa_laittaa_liikaa_tavaraa(self):
        paljonko_mahtuu = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(paljonko_mahtuu + 1)
        self.assertAlmostEqual(paljonko_mahtuu, self.varasto.saldo)

    def test_ottaa_liikaa_tavaraa(self):
        self.varasto.ota_varastosta(self.varasto.saldo + 1)

        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_lisaa_varastoon_negatiivinen(self):
        aikaisempi_saldo = self.varasto.saldo 
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, aikaisempi_saldo)

    def test_ota_varastosta_negatiivinen(self):
        aikaisempi_saldo = self.varasto.saldo 
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, aikaisempi_saldo)

    def test_str_method(self):
        odotettu_tulostus = "saldo = 0, vielä tilaa 10"
        self.assertEqual(str(self.varasto), odotettu_tulostus)