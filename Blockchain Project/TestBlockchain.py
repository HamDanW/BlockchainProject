import unittest
from Blockchain import Blockchain,Block

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_add_block(self):
        data = "Sample Data"
        self.blockchain.add_block(data)
        self.assertEqual(self.blockchain.chain[-1].data, data)

    def test_hash_block(self):
        block = Block("Sample Data")
        expected_hash = "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
        self.assertEqual(block.hash, expected_hash)

    def test_valid_chain(self):
        self.blockchain.add_block("Block 1")
        self.blockchain.add_block("Block 2")
        self.assertTrue(self.blockchain.is_valid_chain())

    def test_invalid_chain(self):
        self.blockchain.add_block("Block 1")
        self.blockchain.add_block("Block 2")
        self.blockchain.chain[1].data = "Tampered Data"
        self.assertFalse(self.blockchain.is_valid_chain())

if __name__ == '__main__':
    unittest.main()