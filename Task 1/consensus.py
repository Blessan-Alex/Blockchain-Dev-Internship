# consensus.py
# Simulates consensus mechanisms (PoW, PoS, DPoS) in a blockchain network

import hashlib
from datetime import datetime
import random

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

# Node simulates a blockchain node
class Node:
    def __init__(self, name):
        self.name = name
        self.blockchain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Genesis block for the node
        genesis_block = Block(0, "Genesis Block", "0")
        self.blockchain.append(genesis_block)

    def add_block(self, data):
        # Add a new block to the node's chain
        previous_block = self.blockchain[-1]
        new_block = Block(len(self.blockchain), data, previous_block.hash)
        self.blockchain.append(new_block)

    def get_blockchain(self):
        return self.blockchain

    def update_blockchain(self, new_chain):
        # Update blockchain if new chain is longer
        if len(new_chain) > len(self.blockchain):
            self.blockchain = new_chain
            return True
        return False

# Network simulates a network of nodes
class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def broadcast_blockchain(self, sender_node):
        # Share sender's blockchain with all other nodes
        for node in self.nodes:
            if node != sender_node:
                node.update_blockchain(sender_node.get_blockchain())

    def simulate_consensus(self):
        # Print the state of all nodes' blockchains
        print("\nSimulating consensus mechanism...")
        for node in self.nodes:
            print(f"\nNode {node.name} has blockchain length: {len(node.blockchain)}")
            for block in node.blockchain:
                print(f"Block {block.index}: {block.data}")

def main():
    # Create network and nodes
    network = Network()
    node1 = Node("Node 1")
    node2 = Node("Node 2")
    node3 = Node("Node 3")
    network.add_node(node1)
    network.add_node(node2)
    network.add_node(node3)
    # Add blocks and broadcast
    print("Adding blocks to Node 1...")
    node1.add_block("Transaction 1")
    node1.add_block("Transaction 2")
    print("\nBroadcasting Node 1's blockchain...")
    network.broadcast_blockchain(node1)
    network.simulate_consensus()
    # Fork scenario
    print("\nDemonstrating fork scenario...")
    node2.add_block("Transaction 3 (from Node 2)")
    node3.add_block("Transaction 3 (from Node 3)")
    print("\nFork created:")
    network.simulate_consensus()
    # Resolve fork
    print("\nResolving fork (longest chain wins)...")
    for node in network.nodes:
        for other_node in network.nodes:
            if node != other_node:
                node.update_blockchain(other_node.get_blockchain())
    print("\nFinal state after consensus:")
    network.simulate_consensus()

if __name__ == "__main__":
    main() 