# Calculating the hash in order to add digital fingerprints to the blocks
from ast import main
import hashlib
import MerkleTree
# To store data in our blockchain
import json
# import AddUser


class Blockchain:

    # This function is created to create the blockchain
    # It stores the chain in the form of a tuple owing to its immutability feature
    def __init__(self):
        self.chain = ()
        self.mp = {}

    # This function is created to add blocks into the chain.
    def create_block(self, previous_hash, proof_of_work, tr_list):
        # mtree = MerkleTree.MerkleTree(tr_list)
        block = {'index': len(self.chain) + 1,
                 'previous_hash': previous_hash,
                 'proof': proof_of_work,
                 'transactions_list': tr_list,
                 #  'roothash' : mtree                         # 3 transactionsper block, stored in the form of a tuple
                 }
        temp_list = list(self.chain)
        temp_list.append(block)
        self.chain = tuple(temp_list)
        return block
    # This function is created to get the last added block

    def latest_block(self):
        return self.chain[-1]

    # This function used SHA256 hashing algorithm to hash a block and return the hash value
    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        # print(encoded_block)
        return hashlib.sha256(encoded_block).hexdigest()

    # this function is used to transfer property
    # pid->sid => pid->rid
    def propTransfer(self, sid, pid, rid):
        if pid in self.mp:
            if self.mp[pid] == sid:
                self.mp[pid] = rid
                return True
            else:
                return False
        else:
            return False

    # this is used to add property to our user
    def addProperty(self, sid, pid):
        if pid in self.mp:
            return False
        self.mp[pid] = sid
        # yaha add ho rha hai
        return True

    # This is the function for proof of work and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        proof_of_work = 1
        is_proof_valid = False

        while is_proof_valid is False:
            hash_operation = hashlib.sha256(
                str(proof_of_work*2 - previous_proof*2).encode()).hexdigest()
            if hash_operation[:2] == '00':
                is_proof_valid = True
            else:
                proof_of_work += 1

        return proof_of_work

    # This function checks if the blockchain is valid and intact
    def chain_valid(self, chain):
        if len(chain) == 0:
            return True

        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof*2 - previous_proof*2).encode()).hexdigest()

            if hash_operation[:2] != '00':
                return False

            previous_block = block
            block_index += 1

        return True

    # This function is used to mine the block
    def mine_block(self, tr_list):
        # print(type(tr_list))
        main_list = []

        for i in range(0, 2):
            tup = tr_list[i]
            s = ''.join(tup)
            main_list.append(s)

        root_hash = MerkleTree.MerkleTree(main_list)
        print(root_hash.getRootHash())

        # print(type(tr_list[0]))
        if len(self.chain) == 0:
            previous_hash = self.hash('Genesis Block')
        else:
            previous_hash = self.hash(self.latest_block())

        if len(self.chain) == 0:
            proof_of_work = 1
        else:
            proof_of_work = self.proof_of_work(self.latest_block()['proof'])

        self.create_block(previous_hash, proof_of_work, tr_list)
