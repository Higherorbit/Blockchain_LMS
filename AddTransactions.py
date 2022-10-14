import datetime

# This function takes input(unverified transactions) from the user
def inputPropertyDetails(blockchain):  
    while True:
        print("\n>>> Print Owner Details")
        SID = input("\n>>> Seller ID")
        PID = input("\n>>> Property ID")
        b=False
        b=blockchain.addProperty(SID,PID)
        if b == False:
            print("\nInvalid Prop ID or SID")
        else :
            print("\n Added Successfully!!!!!")
        
        y_or_n = input("\nD O N E!\n>>> Add more?[y/n]")
        if y_or_n == 'n':
            return 

def inputTransactions(blockchain, leftover_trns):

    input_transactions = leftover_trns

    while True:
        print("\nInput Transaction details")

        while True:
            trn_id = input("\n>>> Transaction id : ")
            # need to have a mechanism to check if that transaction exists

            exists = False
            for block in blockchain.chain:
                for transaction in block["transactions_list"]:
                    if trn_id == transaction[0]:
                        exists = True
                        break
                if exists:
                    break
            for transaction in input_transactions:
                if exists:
                    break
                else:
                    if trn_id == transaction[0]:
                        exists = True
                        break
            if exists:
                print("\nTransaction already exists! Please Try again.")
                continue
            break
        
        SID = input("\n>>> Seller ID")
        PID = input("\n>>> Property ID")
        BID = input("\n>>> Buyer ID")

        # flag1 = False
        flag1 = blockchain.propTransfer(SID, PID, BID)
        if flag1 is False:
            print("WTF BRO!!!!!!!!!")
            y_or_n = input("\nD O N E!\n>>> Add more?[y/n]")

            if y_or_n == 'n':
                return input_transactions
        input_transactions.append((
            trn_id,
            SID,
            PID,
            BID,
            str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p"))
        ))

        y_or_n = input("\nD O N E!\n>>> Add more?[y/n]")

        if y_or_n == 'n':
            return input_transactions


# This function verifies the transactions and adds them to the block(3 transactions per block)
def addTransactions(input_transactions, blockchain):

    count = len(input_transactions)
    while count >= 2:
        verified_trn_list = list(input_transactions[:2])
        input_transactions = input_transactions[2:]

        blockchain.mine_block(verified_trn_list)

        blockchain.chain_valid(blockchain.chain)

        count = count-2

    return input_transactions
