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

# --- Consensus Mechanism Simulation ---

def simulate_pow():
    # Proof of Work: Select validator with highest power
    print("\n--- Proof of Work (PoW) Simulation ---")
    validators = [
        {"name": "MinerA", "power": random.randint(1, 100)},
        {"name": "MinerB", "power": random.randint(1, 100)},
        {"name": "MinerC", "power": random.randint(1, 100)}
    ]
    for v in validators:
        print(f"{v['name']} has power: {v['power']}")
    winner = max(validators, key=lambda v: v["power"])
    print(f"Selected Validator: {winner['name']} (Highest power: {winner['power']})")
    print("Explanation: In PoW, the miner with the most computational power is most likely to add the next block.")


def simulate_pos():
    # Proof of Stake: Select validator with highest stake
    print("\n--- Proof of Stake (PoS) Simulation ---")
    validators = [
        {"name": "StakerA", "stake": random.randint(1, 100)},
        {"name": "StakerB", "stake": random.randint(1, 100)},
        {"name": "StakerC", "stake": random.randint(1, 100)}
    ]
    for v in validators:
        print(f"{v['name']} has stake: {v['stake']}")
    winner = max(validators, key=lambda v: v["stake"])
    print(f"Selected Validator: {winner['name']} (Highest stake: {winner['stake']})")
    print("Explanation: In PoS, the validator with the most coins staked is most likely to add the next block.")


def simulate_dpos():
    # Delegated Proof of Stake: Voters select delegates
    print("\n--- Delegated Proof of Stake (DPoS) Simulation ---")
    delegates = ["DelegateA", "DelegateB", "DelegateC"]
    voters = ["Voter1", "Voter2", "Voter3"]
    # Each voter votes for a delegate (randomly for this simulation)
    votes = {d: 0 for d in delegates}
    for voter in voters:
        vote = random.choice(delegates)
        votes[vote] += 1
        print(f"{voter} votes for {vote}")
    # Find delegate(s) with most votes
    max_votes = max(votes.values())
    winners = [d for d, v in votes.items() if v == max_votes]
    selected = random.choice(winners)
    print(f"Selected Validator: {selected} (Most votes: {max_votes})")
    print("Explanation: In DPoS, validators are chosen by votes. The most-voted delegates take turns adding blocks.")


def main():
    print("\nSimulating and comparing consensus mechanisms (PoW, PoS, DPoS)...")
    simulate_pow()
    simulate_pos()
    simulate_dpos()

if __name__ == "__main__":
    main() 