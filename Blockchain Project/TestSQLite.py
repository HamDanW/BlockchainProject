import sqlite3
import unittest

# import my blockchain class
from Blockchain import Blockchain

class TestBlockchainSQLite(unittest.TestCase): 
    def setUp(self):
        self.blockchain = Blockchain()
        self.conn = sqlite3.connect('blockchain.db')
        self.cursor = self.conn.cursor()

    def test_store_block(self):
        # Add a block to the blockchain
        block = self.blockchain.add_block("test data")
        # Verify that the block was stored in the database
        self.cursor.execute("SELECT * FROM blocks WHERE hash=?", (block.hash,))
        block_from_db = self.cursor.fetchone()
        self.assertIsNotNone(block_from_db)
        self.assertEqual(block_from_db[1], block.timestamp)
        self.assertEqual(block_from_db[2], block.data)
        self.assertEqual(block_from_db[3], block.prev_hash)

    def tearDown(self):
        self.conn.close()
        
if __name__ == '__main__':
    unittest.main()