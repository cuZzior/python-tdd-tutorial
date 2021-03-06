import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Pioter dowiedział się o nowej to-do apce. Odpala strone.
        self.browser.get('http://localhost:8000')

        # Widzi 'To-Do' w tytule strony
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Odrazu ma mozliwosc dodawania to-do listy
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # Dodaje "Kup karme dla kota" bo kocha koty
        inputbox.send_keys('Kup karme dla kota')

        # Klika enter i strone sie aktualizuje, widac w niej
        # "1: Kup karme dla kota" w liscie to-do
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Kup karme dla kota')

        # Wciaz widzi tekst proponujacy dodanie nowego to-do
        # Dodaje "Nasyp tej karmy kotkowi"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Nasyp tej karmy kotkowi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Kup karme dla kota')
        self.check_for_row_in_list_table('2: Nasyp tej karmy kotkowi')
        self.fail('Finish the test!')

        # Po kliknieciu enter strona znowu sie aktualizuje i teraz widzi 2 punkty

        # Pioter zastanawia sie czy strona zapamieta jej liste.
        # Widzi ze strona wygenerowala specjalny URL ktory jest unikatowy.
        # Dostaje rowniez wyjaśnienie tego.

        # Wchodzi w ten link i widzi liste ktora wczesniej wprowadzila

        # Usatysfakcjonowany idzie spac :)


if __name__ == '__main__':
    unittest.main()
