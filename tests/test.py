import unittest
from submitter import submit_data, retrieve_data, create_data


class SubmitterTest(unittest.TestCase):

    def test_receive_data(self):
        retrieve_data()

    def test_create_data(self):
        create_data("filename")

if __name__ == '__main__':
    unittest.main()
