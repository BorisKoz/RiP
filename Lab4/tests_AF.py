import unittest
from unittest import TestCase
from unittest.mock import patch
from main import Intel_AMD
from main import AMD_AMD
from main import Intel_Nvidia
from main import PC_Factory
from main import AMD_Motherboard

class PC_FactoryTestCase(TestCase):

    #тест логики определения неправильного типа платы
    @patch('main.Intel_Nvidia.install_motherboard', return_value=AMD_Motherboard())
    def test_intel_nvidia_build(self, arg):
        factory = Intel_Nvidia()
        proc = factory.install_processor()
        mb = factory.install_motherboard()
        self.assertEqual("неверный тип платы", proc.install(mb))

    #проверка фабрики Intel_AMD установка процессора
    def test_intel_AMD_build_proc(self):
        factory = Intel_AMD()
        proc = factory.install_processor()
        mb = factory.install_motherboard()
        self.assertEqual("установлен процессор INTEL", proc.install(mb))
"""
    # проверка фабрики Intel_AMD установка платы
    def test_intel_AMD_build_MB(self):
        factory = Intel_AMD()
        mb = factory.install_motherboard()
        self.assertEqual("установлена плата с чипсетом INTEL", mb.install())

    # проверка фабрики Intel_AMD установка видеокарты
    def test_intel_AMD_build_GPU(self):
        factory = Intel_AMD()
        gpu = factory.install_gpu()
        self.assertEqual("установлена видеокарта AMD", gpu.install())

    # проверка фабрики Intel_AMD подсчет цены
    def test_intel_AMD_build_Price(self):
        factory = Intel_AMD()
        mb =factory.install_motherboard()
        pr = factory.install_processor()
        gpu = factory.install_gpu()
        mb.install()
        pr.install(mb)
        gpu.install()
        self.assertEqual(510, factory.price())
"""

if __name__ == '__main__':
        unittest.main()
