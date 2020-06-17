#import datetime
import time
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from urllib.parse import urlparse

# Building a Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        # self.shared_files = [] 
        # self.sender = [] ###########
        # self.receiver = [] ##########
        self.create_block(proof = 1, previous_hash = '0' , sender = 'N.A' , receiver = 'N.A' , file_hash = 'N.A') ##########
        self.nodes = set()
        self.nodes.add("127.0.0.1:5111")
    
    def create_block(self, proof, previous_hash, sender, receiver, file_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(time.strftime("%d %B %Y , %I:%M:%S %p", time.localtime())),  # d-date, B-Month, Y-Year ,I-Hours in 12hr format, M-Minutes, S-secnods, p-A.M or P.M
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'sender': sender, #########
                 'receiver':receiver, #########
                 'shared_files': file_hash}
        # self.shared_files = []
        # self.sender = [] #########
        # self.receiver = [] ########
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    def add_file(self, sender, receiver, file_hash):
        # self.sender.append({'sender': sender}) #########
        # self.receiver.append({'receiver': receiver}) ##########
        # self.shared_files.append({'file_hash': file_hash})

        previous_block = self.get_previous_block()
        index = previous_block['index'] + 1
        # To be changed to 10 later
        # if len(self.shared_files) == 1 and len(self.sender) == 1 and len(self.receiver) == 1: #########
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        self.create_block(proof, previous_hash, sender, receiver, file_hash)
        return index
    
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False

