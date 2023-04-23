import json
from datetime import datetime
from hashlib import sha256
from merkle_tree import MerkleTree


class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.transactions = []

        self.new_block()

    def new_block(self, previous_hash=None, transaction=None):

        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.transactions,
            'previous_hash': previous_hash
        }

        if transaction is not None:
            self.transactions.append(transaction.transactionId)
            merkle_root = MerkleTree(self.transactions).getRootHash()
            block['merkle_root'] = merkle_root
            block['transactions'] = self.transactions

        block_hash = self.hash(block)
        block['hash'] = block_hash

        self.chain.append(block)

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1] if self.chain else None
