# Blockchain_Technology

# Group Details
# Samandeep Singh (2020A7PS0065H)
# Vedant Mathur (2020A7PS0065H)
# Sri Harshitha Ronda (2020A3PS0496H)

## Land Management System using Blockchain

## The consensus algorithm used is Delegated Proof of Stake(DPoS)

### --------------------COMPONENTS-------------------

## 1. Block

### Index, Previous Hash, Proof, Transactions{List of transactions}

### block = {

### "Index": len(self.chain) + 1,

### "Previous Hash": "",

### "Proof": "",

### "Transaction list": "",

### "Root Hash": "",

### "Transaction": []

### }

###

## 2. Transaction

### Transaction ID, Buyer ID, Seller ID, Property ID, Timestamp of the transaction.

### transaction = {

### "Transaction ID": "",

### "Buyer ID": "",

### "Property ID": "",

### "Seller ID": "",

###

### "Timestamp": ""

### }

###

## 3. Property History

### property_history = {

### "Property_ID": {

### "Transaction ID": "",

### "Buyer ID": "",

### "Property ID": "",

### "Seller ID": "",

###

### "Timestamp": ""

### }

### }

### --------------------FUNCTIONS-------------------

### 1. Create_Block

#### Create a new Block as soon as minimum threshold(2) of transactions occur

### 2. Create_Node

#### Register new users with preowned property

### 3. New_Transaction

#### Create a new Transaction

### 4. Print_Property_history

#### Print the details of all the transactions related to a property

### 5. Print_Nodes

#### Print the details of particular user

### 6. Print_BlockChain

#### Print the entire BlockChain network

### 7. DPoS

#### Implementation of Delegated Proof of Stake

### 8. Create_Merkle_Tree

#### Implement Merkle Tree

### 9. Validate_Chain

#### Validates the Blockchain

### 10. Hash_Block

#### Hashes the data using SHA 256 protocol

### 11. Validate Transaction

#### Validates the transaction and checks for anomalies
