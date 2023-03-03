def proof_of_work(block, difficulty):
    max_nonce = 2**32
    for nonce in range(max_nonce):
        block.nonce = nonce
        if block.hash[:difficulty] == '0' * difficulty:
            return nonce
    return None