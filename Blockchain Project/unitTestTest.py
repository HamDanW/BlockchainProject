import unittest
import hashlib

from Blockchain import Blockchain,Block

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_invalid_chain(self): 
        self.blockchain.add_block("Block 1")
        self.blockchain.add_block("Block 2")
        self.blockchain.chain[1].data = "Tampered Data"
        self.assertFalse(self.blockchain.is_valid_chain())

if __name__ == '__main__':
    unittest.main()