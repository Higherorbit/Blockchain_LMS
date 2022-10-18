import json
# This function prints the entre blockchain
def viewBlockchain( blockchain ):
    if len(blockchain.chain) == 0:
        print("\nNo blocks added yet.")
        return
    
    print(json.dumps(blockchain.chain, indent=4))