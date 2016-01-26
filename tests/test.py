import unittest
from submitter import submit_data, retrieve_data


class SubmitterTest(unittest.TestCase):

    def test_survey_submit(self):
        submit_data("test", "test")

    def test_receive_data(self):
        retrieve_data()

if __name__ == '__main__':
    unittest.main()