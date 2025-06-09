# mining.py
# Simulates mining (Proof-of-Work) in a blockchain

import hashlib
from datetime import datetime
import time

# Block represents a single block in the blockchain
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block data and return SHA-256 hash
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Miner simulates a miner that mines blocks
class Miner:
    def __init__(self, name, difficulty=4):
        self.name = name
        self.difficulty = difficulty
        self.blockchain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Genesis block for the miner
        genesis_block = Block(0, "Genesis Block", "0")
        self.blockchain.append(genesis_block)

    def mine_block(self, data):
        # Mine a new block by finding a hash with required difficulty
        previous_block = self.blockchain[-1]
        new_block = Block(len(self.blockchain), data, previous_block.hash)
        print(f"\nMiner {self.name} is mining block {new_block.index}...")
        start_time = time.time()
        while True:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
            # Check if hash meets difficulty (e.g., starts with '0000')
            if new_block.hash.startswith('0' * self.difficulty):
                end_time = time.time()
                print(f"Block mined! Hash: {new_block.hash}")
                print(f"Mining time: {end_time - start_time:.2f} seconds")
                print(f"Nonce: {new_block.nonce}")
                self.blockchain.append(new_block)
                return new_block

    def get_blockchain(self):
        return self.blockchain

    def print_blockchain(self):
        # Print all blocks for this miner
        print(f"\nBlockchain for Miner {self.name}:")
        print("=" * 50)
        for block in self.blockchain:
            print(f"\nBlock #{block.index}")
            print(f"Time: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)

def main():
    # Create miners and simulate mining
    miner1 = Miner("Miner 1", difficulty=4)
    miner2 = Miner("Miner 2", difficulty=4)
    print("Starting mining simulation...")
    miner1.mine_block("Transaction 1")
    miner2.mine_block("Transaction 2")
    miner1.print_blockchain()
    miner2.print_blockchain()
    # Demonstrate higher difficulty
    print("\nDemonstrating difficulty adjustment...")
    hard_miner = Miner("Hard Miner", difficulty=5)
    hard_miner.mine_block("Transaction 3")
    hard_miner.print_blockchain()

if __name__ == "__main__":
    main() 