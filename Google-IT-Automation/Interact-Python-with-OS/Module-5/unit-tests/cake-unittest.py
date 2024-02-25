import unittest
from cake_factory import CakeFactory

class TestCakeFactory(unittest.TestCase):
    def test_create_cake(self):
        cake = CakeFactory("vanilla", 'small')
        self.assertEqual(cake.cake_type, 'vanilla')
        self.assertEqual(cake.size, 'small')
        self.assertEqual(cake.price, 8) # vanilla cake, small size
        
    def test_add_topping(self):
        cake = CakeFactory("chocolate", 'large')
        cake.add_toppings('sprinkles')
        self.assertIn('sprinkles', cake.toppings)
        
    def test_check_ingredients(self):
        cake = CakeFactory("chocolate", 'medium')
        cake.add_toppings('cherries')
        ingredients = cake.check_ingredients()
        self.assertIn('cocoa', ingredients)
        self.assertIn('cherries', ingredients)
        self.assertNotIn('vanilla extract', ingredients)

    def test_check_price(self):
        cake = CakeFactory("vanilla", 'large')
        cake.add_toppings('sprinkles')
        cake.add_toppings('cherries')
        price = cake.check_price()
        self.assertEqual(price, 14) # vanilla cake, large size + 2 toppings
        
# running the unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))