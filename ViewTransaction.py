# This function asks transaction ID from the user and prints the corresponding transaction details
def viewTransaction(blockchain):
    if len(blockchain.chain) == 0:
        print('\nBlockchain empty!!!')
        return

    quote_string = "\nDetails of Transaction {}::==\nSeller ID       :  {}\nProperty ID              :  {}\nBuyer ID           :  {}\nTimestamp           :  {}"

    while True:
        transaction_id = input("\nEnter Transaction id: ")

        exists = [False]
        for block in blockchain.chain:
            for transaction in block["transactions_list"]:
                if transaction[0] == transaction_id:
                    exists = [True, transaction[1], transaction[2],
                              transaction[3], transaction[4]]
                    break
            if exists[0]:
                break

        if exists[0]:
            print(quote_string.format(transaction_id,
                  exists[1], exists[2], exists[3], exists[4]))
        else:
            print("\nInvalid Transaction id!!!")
            y_or_n = input("\n>>> Repeat query?[y/n]")
            if y_or_n == "y":
                continue

        break
    print("")
    return
