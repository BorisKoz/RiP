import unittest
from unittest import TestCase
from unittest.mock import patch
from observer import meteostation
from observer import subscriber


class ObserverTestCase(TestCase):

    #тест подписки
    def testsubscribe(self):
        st1 = meteostation("st1")
        sub1 = subscriber("S1")
        self.assertEqual("S1 подписался", st1.subscribe(sub1))
    #тест запуска оповещения
    def testnotify(self):
        st1 = meteostation("st1")
        st1.temperature = [-4]
        sub1 = subscriber("s1")
        self.assertEqual(st1.measure(), "оповещение запущено")


if __name__ == '__main__':
        unittest.main()
