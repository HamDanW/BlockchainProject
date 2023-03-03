from Block import Block
from proof_of_work import proof_of_work
import sqlite3

class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]
        self.conn = sqlite3.connect('blockchain.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS blocks ('index' INTEGER PRIMARY KEY, timestamp FLOAT, data TEXT, previous_hash TEXT, nonce INTEGER, hash TEXT)")
    
    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        block = Block(data, prev_hash)
        block.nonce = proof_of_work(block, 0)
        self.chain.append(block)
        self.cursor.execute("INSERT INTO blocks (timestamp, data, previous_hash, nonce, hash) VALUES (?,?,?,?,?)", (block.timestamp, block.data, block.prev_hash, block.nonce, block.hash))
        self.conn.commit()
        return block
        
    def get_blocks(self):
        self.cursor.execute("SELECT * FROM blocks")
        blocks = self.cursor.fetchall()
        return blocks
    
    def __del__(self):
        self.conn.close()
        
    def genesis(self):
        return Block("Genesis Block", 0)
    
    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate():
                return False
            if previous_block.hash != current_block.prev_hash:
                return False
            if previous_block.hash == current_block.calculate() and previous_block.nonce == current_block.nonce:
                return False
        return True

def genesis():
    return Block("The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", "0")
