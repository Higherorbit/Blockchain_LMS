import datetime
# from BlockChainTech-main.BlockChain import Blockchain

# This function takes input(unverified transactions) from the user

# adding user here


def inputPropertyDetails(blockchain):
    while True:
        print("\n>>> Print Owner Details")
        SID = input("\n>>> User Name  : ")
        PID = input("\n>>> Property ID  : ")
        if SID == "" or PID == "":
            print("\nEnter valid User Name or PID")
            continue
        b = False
        b = blockchain.addProperty(SID, PID)
        if b == False:
            print("\nInvalid Prop ID or User Name")
        else:
            print("\n Added Successfully!!!!!")

        while True:
            y_or_n = input("\n>>> Add more?[y/n]")
            if y_or_n == 'n':
                return
            elif y_or_n == 'y':
                break
            else:
                print("Enter either y or n!!")


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

        SID = input("\n>>> Seller Name: ")
        PID = input("\n>>> Property ID: ")
        BID = input("\n>>> Buyer Name: ")
        if SID == "" or PID == "" or BID == "":
            print("Please enter Valid Seller Name or PID or Buyer Name")
            continue

        if BID == SID:
            print("Buyer and Seller cant be same, wtf")
            continue

        # flag1 = False
        flag1 = blockchain.propTransfer(SID, PID, BID)
        if flag1 is False:
            print("Invalid Seller Name or PID or Buyer Name")
        else:
            input_transactions.append((
                trn_id,
                SID,
                PID,
                BID,
                str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p"))
            ))
        while True:
            y_or_n = input("\n>>> Add more?[y/n]")
            if y_or_n == 'n':
                return input_transactions
            elif y_or_n == 'y':
                break
            else:
                print("Enter either y or n!!")


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
