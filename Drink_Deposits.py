def recycle_refund():
    sm_deposit = 0.10
    lg_deposit = 0.25

    small = int(input("Enter the number of containers 1 liter or less: "))
    large = int(input("Enter the number of containes larger than 1 liter: "))

    refund = small * sm_deposit + large * lg_deposit

    print(f"The total refund of all drinks is:  {refund: .2f}")


#    x = input(f"Enter the size of your container in liters: ").split

#    sm_drinks = []
#    lg_drinks = []

#    sm_deposits = 0.10
#    lg_deposits = 0.25

#    small_container = x <= 1.0
#    large_container = x > 1.0

#    sm_refund = sm_drinks * sm_deposits
#    lg_refund = lg_drinks * lg_deposits

#    for x in input:
#        if x <= 1.0:
#            sm_drinks.append()
#        else:
#            lg_drinks.append()

#    sm_drinks.count([])
#    lg_drinks.count([])

#    print(
#        "Total number of deposits:",
#    )

#    return sm_refund + lg_refund


recycle_refund()
