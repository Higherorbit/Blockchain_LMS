# Calculating the hash in order to add digital fingerprints to the blocks
from ast import main
import hashlib
import imp
import MerkleTree
# To store data in our blockchain
import json
import random
import datetime
# import AddUser


class Blockchain:

    # This function is created to create the blockchain
    # It stores the chain in the form of a tuple owing to its immutability feature
    def __init__(self):
        self.chain = []
        self.mp = {}
        self.user = {}
        self.np = 0
    # This function is created to add blocks into the chain.

    def create_block(self, previous_hash, dpos, tr_list1,tr_list2):
        if len(self.chain) == 0:
            nonce  = 1
        else :
            nonce = self.puzzle(self.latest_block()['Nonce'])

        
        
        mtree = MerkleTree.MerkleTree(tr_list1)
        t=str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p"))
        block = {
            'index': len(self.chain) + 1,
            'previous_hash': previous_hash,
            'proof': dpos,
            'transactions_list': tr_list2,
            'roothash': mtree.getRootHash(),
            'Timestamp': t,
            'Nonce' : nonce
        }
        temp_list = list(self.chain)
        temp_list.append(block)
        self.chain = list(temp_list)
        return block
    # This function is created to get the last added block

    def latest_block(self):
        return self.chain[-1]
    

    def puzzle(self, previous_proof):
        nonce = 1
        is_proof_valid = False

        while is_proof_valid is False:
            hash_operation = hashlib.sha256(
                str(nonce*2 - previous_proof*2).encode()).hexdigest()
            if hash_operation[:2] == '00':
                is_proof_valid = True
            else:
                nonce += 1
             
        return nonce
    # This function used SHA256 hashing algorithm to hash a block and return the hash value
    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # this function is used to transfer property
    # pid->sid => pid->rid
    def propTransfer(self, sid, pid, rid):
        if pid in self.mp:
            if self.mp[pid] == sid:
                self.mp[pid] = rid
                if sid not in self.user:
                    self.user[sid] = 0
                if rid not in self.user:
                    self.user[rid] = 0
                self.user[sid] -= 1
                self.user[rid] += 1
                return True
            else:
                return False
        else:
            return False

    # this is used to add property to our user
    def addProperty(self, sid, pid):
        if pid in self.mp:  # pid is already assigned to some other user
            return False
        self.mp[pid] = sid  # assigned the property pid to sid

        if sid not in self.user:    # need to tell user map ki sid ke pas 0 property hai
            self.user[sid] = 0

        self.user[sid] += 1
        self.np += 1  # this is the count of total propety we have | for threshold calculations
        # yaha add ho rha hai
        return True

    def delegated_proof_of_stake(self):
        # first lets make a list which tells the number of users/nodes we have
        threshold = int(0.25 * self.np)
        delegates = {}
        maximumVotes = {}
        cnt = 0
        ans = 0

        for id, val in self.user.items():
            if val >= threshold:
                cnt += 1
        for id, val in self.user.items():
            if val >= threshold:
                if id not in delegates:
                    delegates[id] = 0
                delegates[id] = random.randint(0, cnt-1)
                if delegates[id] not in maximumVotes:
                    maximumVotes[delegates[id]] = 0
                maximumVotes[delegates[id]] += 1
                ans = max(ans, maximumVotes[delegates[id]])

        for id, val in maximumVotes.items():
            if val == ans:
                return id

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

        if len(self.chain) == 0:
            previous_hash = self.hash('Genesis Block')
        else:
            previous_hash = self.hash(self.latest_block())

        dpos = self.delegated_proof_of_stake()

        self.create_block(previous_hash, dpos, main_list,tr_list)
