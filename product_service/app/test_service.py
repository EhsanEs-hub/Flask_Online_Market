import unittest
import setup
import json

class ProductServiceTestCase(unittest.TestCase):
    def setUp(self):

        # Define test variables and initialise app
        self.app = setup.Create_app()
        self.client = self.app.test_client

    def test_products(self):

        # Test API can get the products (Get request)
        res = self.client().get('/api/products')
        self.assertEqual(res.status_code, 200)
        response = {
            "results": [
                {
                    "id": 1,
                    "image": "banana.png",
                    "name": "banana",
                    "price": 2,
                    "slug": "product-1"
                },
                {
                    "id": 2,
                    "image": "coffee.png",
                    "name": "coffee",
                    "price": 5,
                    "slug": "product-2"
                }
            ]
        }
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data, response)

    def test_product(self):

        # Test API can get a product (Get request)
        res = self.client().get('/api/product/product-1')
        self.assertEqual(res.status_code, 200)
        response = {
            "results": [
                {
                    "id": 1,
                    "image": "banana.png",
                    "name": "banana",
                    "price": 2,
                    "slug": "product-1"
                }
            ]
        }
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data, response)


if __name__ == '__main__':
    unittest.main()
