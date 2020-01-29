import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Pioter dowiedział się o nowej to-do apce. Odpala strone.
        self.browser.get('http://localhost:8000')

        # Widzi 'To-Do' w tytule strony
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Odrazu ma mozliwosc dodawania to-do listy

        # Dodaje "Kup karme dla kota" bo kocha koty

        # Klika enter i strone sie aktualizuje, widac w niej
        # "1: Kup karme dla kota" w liscie to-do

        # Wciaz widzi tekst proponujacy dodanie nowego to-do
        # Dodaje "Nasyp tej karmy kotkowi"

        # Po kliknieciu enter strona znowu sie aktualizuje i teraz widzi 2 punkty

        # Pioter zastanawia sie czy strona zapamieta jej liste.
        # Widzi ze strona wygenerowala specjalny URL ktory jest unikatowy.
        # Dostaje rowniez wyjaśnienie tego.

        # Wchodzi w ten link i widzi liste ktora wczesniej wprowadzila

        # Usatysfakcjonowany idzie spac :)
if __name__ == '__main__':
    unittest.main()
