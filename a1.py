'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''
lst = [[0, "Tshirt", "Apparels", "500"], [1, "Trousers", "Apparels", "600"], [2, "Scarf", "Apparels", "250"],
           [3, "Smartphone", "Electronics", "20000"], [4, "iPad", "Electronics", "30000"],
           [5, "Laptop", "Electronics", "50000"],
           [6, "Eggs", "Eatables", "5"], [7, "Chocolate", "Eatables", "10"], [8, "Juice", "Eatables", "100"],
           [9, "Milk", "Eatables", "45"]]



def show_menu():
    '''
	Description: Prints the menu as shown in the PDF
	
	Parameters: No paramters
	
	Returns: No return value
	'''
    print("=" * 50)
    print(" " * 19, end="")
    print("MY BAZAAR")
    print("=" * 50,end="")
    print("\nHello Welcome to my grocery store!")
    print("Following are the products available in the shop:\n")

    print("-" * 50)
    print(" CODE\t|  DESCRIPTION\t|   CATEGORY\t|  COST(Rs)")
    print("-" * 50)

    for i in lst:
        for j in i:
            print(" ", j, end="\t")
            if i.index(j) != 3:
                print("|", end="")
            print("", end=" ")
        print()

    print("-"*50)
    print()




def get_regular_input():
    '''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
    code_l = [0] * 10
    print()
    print("-" * 50)
    print("ENTER ITEMS YOU WISH TO BUY")
    print("-" * 50)

    item = list(map(int, input("Enter the item codes (space separated): ").split()))
    for i in item:
        if i>=0 and i<=9:
            code_l[i] += 1
        else:
            print("Invalid input:",i)

    return code_l


def get_bulk_input():
    '''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
    lst3 = [0] * 10
    lst1 = list()
    print()
    print("-" * 50)
    print("ENTER ITEM AND QUANTITIES")
    print("-" * 50)

    while (1):

        w=input("Enter code and quantity (leave blank space to stop):")
        if w=="":
            print("Your order has been finalized.")
            break

        c, q = map(int,w.split())

        if (c >= 0 and c <= 9) and q >= 0:
            print("You added", q, lst[c][1])
            lst1.append((c, q))
        elif q < 0 and (c < 0 or c > 9):
            print("Invalid code and quantity. Try again")
        elif q < 0:
            print("Invalid quantity. Try again.")
        elif c < 0 or c > 9:
            print("Invalid code. Try again.")

        print()
    for i in lst1:
        lst3[i[0]] += i[1]
    return lst3


def print_order_details(quantities):
    '''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''

    print("\n")
    print("-" * 50)
    print("ORDER DETAILS")
    print("-" * 50)
    count = 1
    v=0
    w=0
    for i in range(len(quantities)):
        if quantities[i]==0:
            continue
        w=quantities[i] * int(lst[i][3])
        print("[" + str(count) + "]", lst[i][1], "x", quantities[i], "= Rs", lst[i][3], "*", quantities[i], "=", "Rs",w)
        v +=w
        count += 1

    print("\nTOTAL COST = Rs",v)


def calculate_category_wise_cost(quantities):
    '''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''

    print("\n")
    print("-" * 50)
    print("CATEGORY-WISE COST")
    print("-" * 50)
    app = 0
    elec = 0
    eat = 0
    for i in range(len(quantities)):
        if lst[i][2] == "Apparels":
            app += int(lst[i][3])*quantities[i]
        elif lst[i][2] == "Electronics":
            elec += int(lst[i][3])*quantities[i]
        elif lst[i][2] == "Eatables":
            eat += int(lst[i][3])*quantities[i]
    if app!=0:
        print("Apparels = Rs", app)
    if elec!=0:
        print("Electronics = Rs", elec)
    if eat!=0:
        print("Eatables = Rs", eat)

    return (app, elec, eat)


def get_discount(cost, discount_rate):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
    dis_app = apparels_cost
    dis_elec = electronics_cost
    dis_eat = eatables_cost
    dis_a = 0
    dis_el = 0
    dis_e = 0
    if apparels_cost >= 2000:
        dis_a = get_discount(apparels_cost,0.1)
        dis_app = apparels_cost - (dis_a)
    if electronics_cost >= 25000:
        dis_el = get_discount(electronics_cost,0.1)
        dis_elec = electronics_cost - (dis_el)
    if eatables_cost >= 500:
        dis_e = get_discount(eatables_cost,0.1)
        dis_eat = eatables_cost - (dis_e)

    print("\n")
    print("-" * 50)
    print("DISCOUNTS")
    print("-" * 50)


    if dis_a != 0:
        print("[APPAREL] Rs", apparels_cost, "- Rs", dis_a, "= Rs", dis_app)
    if dis_el != 0:
        print("[ELECTRONICS] Rs", electronics_cost, "- Rs", dis_el, "= Rs", dis_elec)
    if dis_e != 0:
        print("[EATABLES] Rs", eatables_cost, "- Rs", dis_e, "= Rs", dis_eat)

    print("\nTOTAL DISCOUNT = Rs", dis_a + dis_el + dis_e)
    print("TOTAL COST = Rs", dis_app + dis_eat + dis_elec)

    return (dis_app, dis_elec, dis_eat)


def get_tax(cost, tax):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
    t_a = get_tax(apparels_cost,0.10)
    t_el = get_tax(electronics_cost,0.15)
    t_e = get_tax(eatables_cost,0.05)

    print("\n")

    print("-" * 50)
    print("TAX")
    print("-" * 50)

    if t_a!=0:
        print("[APPAREL] Rs", apparels_cost, "* 0.10 = Rs", t_a)
    if t_el!=0:
        print("[ELECTRONICS] Rs", electronics_cost, "* 0.15 = Rs", t_el)
    if t_e!=0:
        print("[EATABLES] Rs", eatables_cost, "* 0.05 = Rs", t_e)

    tot_tax_inc = (apparels_cost + t_a) + (electronics_cost + t_el) + (eatables_cost + t_e)
    tot_tax = (t_e) + (t_el) + (t_a)

    print("\nTOTAL TAX= Rs", tot_tax)
    print("TOTAL COST= Rs", tot_tax_inc)

    return (tot_tax_inc, tot_tax)


def apply_coupon_code(total_cost):
    '''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
    print("\n")
    print("-" * 50)
    print("COUPON CODE")
    print("-" * 50)

    while (1):
        s = input("Enter coupon code (else leave blank):")

        if s == "HELLE25" and total_cost>=25000:
            min_m = min(5000, get_discount(total_cost,0.25))
            print("[HELLE25] min(5000, Rs", total_cost, "* 0.25) = Rs", min_m)
            break
        elif s == "HELLE25" and total_cost<25000:
            print("Coupon not valid since total cost < 25000")

        elif s == "CHILL50" and total_cost>=50000:
            min_m = min(10000, get_discount(total_cost,0.50))
            print("[CHILL50] min(10000, Rs", total_cost, "* 0.50) = Rs", min_m)
            break
        elif s == "CHILL50" and total_cost<50000:
            print("Coupon not valid since total cost < 50000")

        elif s == "":
            min_m = 0
            print("No coupon code applied.")
            break

        else:
            print("Invalid Coupon Code. Try Again.")
        print()
    print("\nTOTAL COUPON DISCOUNT = Rs", min_m)
    print("TOTAL COST = Rs", total_cost - min_m)

    return (total_cost - min_m,min_m)


def main():
    '''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''

    show_menu()

    while (1):
        ch = input("Would you like to buy in bulk?(y or Y / n or N):")

        if ch == "y" or ch == "Y":

            lst2 = get_bulk_input()
            break

        elif ch == "n" or ch == "N":

            lst2 = get_regular_input()
            break

    print_order_details(lst2)
    app, elec, eat = calculate_category_wise_cost(lst2)
    dis_app, dis_elec, dis_eat = calculate_discounted_prices(app, elec, eat)
    tot_c_incl_tax, tot_tax, = calculate_tax(dis_app, dis_elec, dis_eat)
    min_m, final = apply_coupon_code(tot_c_incl_tax)

    print("\nThank you for visiting!")

if __name__ == '__main__':
    main()
