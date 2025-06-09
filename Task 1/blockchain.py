# blockchain.py
# Basic blockchain simulation with tamper detection

import hashlib
from datetime import datetime

# Block represents a single block in the blockchain
class Block:
    def __init__(self, index, data, previous_hash):
        # Block properties
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        # Hash is calculated when block is created
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block data and return SHA-256 hash
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def print_block(self):
        # Print block details
        print(f"\nBlock #{self.index}")
        print(f"Time: {self.timestamp}")
        print(f"Data: {self.data}")
        print(f"Previous Hash: {self.previous_hash}")
        print(f"Hash: {self.hash}")
        print(f"Nonce: {self.nonce}")

# Blockchain manages the chain of blocks
class Blockchain:
    def __init__(self):
        # Start with the genesis block
        self.chain = [self.create_first_block()]

    def create_first_block(self):
        # Genesis block has index 0 and previous hash '0'
        return Block(0, "First Block", "0")

    def add_block(self, data):
        # Add a new block to the chain
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Validate the blockchain's integrity
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            # Check if hash is correct
            if current.hash != current.calculate_hash():
                return False
            # Check if previous hash matches
            if current.previous_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        # Print all blocks in the chain
        print("\nBlockchain:")
        print("=" * 50)
        for block in self.chain:
            block.print_block()
            print("-" * 50)

def main():
    # Create blockchain and add blocks
    print("Creating a new blockchain...")
    blockchain = Blockchain()
    print("\nAdding blocks...")
    blockchain.add_block("Second Block Data")
    blockchain.add_block("Third Block Data")
    blockchain.print_chain()
    # Validate chain
    print(f"\nIs the chain valid? {blockchain.is_chain_valid()}")
    # Tampering demonstration
    print("\nDemonstrating tampering...")
    print("Changing data in Block 1...")
    blockchain.chain[1].data = "Modified Data"
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    blockchain.print_chain()
    print(f"\nIs the chain valid after tampering? {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main() 