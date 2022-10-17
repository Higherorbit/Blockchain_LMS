import BlockChain
import AddTransactions
# import ViewTransaction
import ViewTransactions
# import ViewTimestamp
import ViewBlockBlockchain
# import ViewUnverifiedTransactions

# Initiating the blockchain
blockchain = BlockChain.Blockchain()

print("<------------------------SESSION START------------------------->")

leftover_trns = []
# To hold any unverified transactions after an iteration

# Iterations start...
# In each iteration the user can perform only one query
while True:
    print("\n_________________________________________")
    print("_________________________________________")
    print("\n[1] - Add User And Property")
    print("[2] - Add Transactions")
    print("[3] - View completed Transactions")
    print("[4] - View the Blockchain")
    print("[5] - View completed Transactions by PID")
    print("\n[e] - Exit")
    choice = input("\n>>> Choose a query to execute: ")

    if choice == "2":
        unverified_trns = AddTransactions.inputTransactions(
            blockchain, leftover_trns)
        leftover_trns = AddTransactions.addTransactions(
            unverified_trns, blockchain)
        # Unverified transactions that weren't added to the block after an iteration
        # are stored in this list (leftover_trns) and are passed into the next iteration, if there is one.
    elif choice == "1":
        AddTransactions.inputPropertyDetails(blockchain)

    elif choice == "3":
        ViewTransactions.viewTransactions(blockchain)

    elif choice == "5":
        pid = input("\n>>> Property ID: ")
        ViewTransactions.viewTransactionsbyPID(blockchain, pid)

    elif choice == "4":
        ViewBlockBlockchain.viewBlockchain(blockchain)

    elif choice == "e":
        if blockchain.chain_valid(blockchain.chain) == False:
            print("Integrity of blockchain lost!!!")
            exit()

        print("\nThank you.\n")
        break

    else:
        print('\nPlease choose from the queries given!!!')

print("<-------------------------SESSION END-------------------------->")
