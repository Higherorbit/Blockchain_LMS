from ViewTransactions import addSpaces

# This function prints the leftover unverified transactions in an iteration


def viewUnverifiedTransactions(leftover_transactions):
    if len(leftover_transactions) == 0:
        print("\nNo Unverfied Transactions.")
        return

    print("Transaction ID      Customer Name      Amount(INR)      Timestamp")
    print("-------------------------------------------------------------------------------------")

    for unverified_trn in leftover_transactions:
        print("{}      {}      {}      {}".format(
            addSpaces(unverified_trn[0], len("Transaction ID")),
            addSpaces(unverified_trn[2], len("Customer Name")),
            addSpaces(unverified_trn[1], len("Amount(INR)")),
            unverified_trn[3]
        ))
