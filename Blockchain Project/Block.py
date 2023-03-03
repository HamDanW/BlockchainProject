import hashlib
import time

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.timestamp = time.time()
        self.nonce = 0
        self.prev_hash = prev_hash
        self.hash = self.calculate()

    def calculate(self):
        block_string = f"{self.data}{self.timestamp}{self.nonce}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()
