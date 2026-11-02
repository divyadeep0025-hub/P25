#date 17/09/2026 practice set

# Question 1 — E-Commerce Return System 📦
# Input:
# - Product category  : (electronics/clothing/food)
# - Days since purchase :
# - Product opened  : (yes/no)

# Conditions :
# - Electronics:
#     - ≤ 7 days:
#         - Opened no → Return Accepted
#         - Opened yes → Return Depends on Condition
#     - 7 days → Return Period Expired
# - Clothing:
#     - ≤ 15 days:
#         - Opened no → Return Accepted
#         - Opened yes → Return Accepted with Conditions
#     - 15 days → Return Period Expired
# - Food → Food Items Cannot Be Returned

product = input("enter product category : ")

if product == "electronics" :
    Day_since_purchase = int(input("enter days : "))
    if Day_since_purchase <= 7 :
        Product_opened = input("product opened say yes or no : ")
        if Product_opened == "no" :
            print("Return accepted")
        else :
            print("Return depends on condition")
    else :
        print("sorry for your inconvinence but after 7 days return period have been expired.")

elif product == "clothes":
    Day_since_purchase = int(input("enter days : "))
    if Day_since_purchase <= 15 :
        Product_opened = input("product opnened say yes or no : ")
        if Product_opened == "no" :
            print("return accepted")
        else :
            print("return depends on condition")
    else :
        print("sorry for your inconvinence but after 15 days return period have been expired.")

else :
    print("sorry for your inconvinence but food product can not be returned according to our policy.")

# Question 2 — Driving License Eligibility 🚗
# Input:
# - Age :
# - Learner license  : (yes/no)
# - Driving test passed : (yes/no)

# Conditions :
# - Age ≥ 18:
#     - Learner license yes:
#         - Test passed yes → License Approved
#         - Test passed no → Retake Driving Test
#     - Learner license no → Get Learner License First
# - Age < 18 → Not Eligible

age = int(input("enter your age : "))

if age >= 18 :
    Learner_license = input("you have learner license say yes or no : ")

    if Learner_license == "yes" :
        Driving_test_passed = input("did you passed driving test say yes or no : ")

        if Driving_test_passed == "yes" :
            print("Congratulation your driving license have been approved.")

        else :
            print("Sorry you failed the driving test. Retake again and try again.")

    else :
        print("Get the learner license first and than try for driving license.")    

else :
    print("you are minor you are not eligible for learner license. try after your age turn 18.")        

# Question 3 — Internet Plan Selection 

# Input:

# - Plan type :(basic/premium)
# - Data usage :
# - Auto-renewal : (yes/no)

# Conditions :

# - Basic:
#     - Usage ≤ 100 GB → ₹499
#     - Usage > 100 GB:
#         - Auto-renewal yes → ₹599
#         - No → Upgrade to Premium
# - Premium:
#     - Usage ≤ 300 GB:
#         - Auto-renewal yes → ₹799
#         - No → ₹849
#     - Usage > 300 GB → Premium Limit Exceeded

Plan_type = input("enter your internet plan type(basic or premium) : ")

if Plan_type == "basic" :
    Data_usage = input("enter data usage limit(ex. = 50 GB) : ")
    if Data_usage > "100 GB" :
        Auto_renewal = input("do you want to auto renewal your pack say yes or no : ")
        if Auto_renewal == "yes":
            print("you have to pay 599 Rs.")
        else :
            print("you have to upgrade to premium.")
    else :
        print("you have to pay 499 Rs.")

else :
    Data_usage = input("enter data usage limit(ex. = 50 GB) : ")
    if Data_usage <= "300 GB" :
        Auto_renewal = input("do you want to auto renewal your pack say yes or no : ")
        if Auto_renewal == "yes":
            print("you have to pay 799 Rs.")
        else :
            print("you have to pay 849 Rs.")
    else :
        print("premium limit exceed.")

# Question 4 — Restaurant Table Booking 🍽️

# Input:
# - Number of guests :
# - Table type : (normal/private)
# - Special occasion : (yes/no)

# Conditions :
# - Normal table:
#     - Guests ≤ 6 → Booking Available
#     - Guests > 6 → Choose Private Table
# - Private table:
#     - Guests ≤ 10:
#         - Special occasion yes → Private Table + Decoration
#         - No → Private Table Booked
#    - Guests > 10 → Maximum 10 Guests

Table_type = input("select the table type(normal or private) : ")
if Table_type == "normal" :
    guest = int(input("enter how many guests are with you : "))
    if guest <= 6 :
        print("Booking available")
    else :
        print("choose private table")

else :
    guest = int(input("enter how many guests are with you : "))
    if guest <= 10 :
        Special_occaison = input("Is there any special occaison say yes or no : ")
        if Special_occaison == "yes" :
            print("private table and decoration booked ")

        else:
            print("private table book")

    else :
        print("maximum guest limit is 10 only.")
      
# Question 5 — Check Scholarship Eligibility 

# Input:
# - Percentage :
# - Family income :
# - Sports achievement  : (yes/no)

# Conditions :
# - Percentage ≥ 80:
#     - Income ≤ ₹3 lakh → Full Scholarship
#     - Income > ₹3 lakh:
#         - Sports achievement yes → Partial Scholarship
#         - No → No Scholarship
# - Percentage 60–79:
#     - Sports achievement yes → Sports Scholarship
#     - No → Not Eligible
# - Percentage < 60 → Not Eligible

Percentage = int(input("write your percentage : "))

if Percentage >= 80:
    Family_income = int(input("write yearly income of your family : "))

    if Family_income <= 300000 :
        print("congratulations you get full scholarship.")

    else :
        Sports_achievment = input("do you have any sports achivemnet say yes or no : ")

        if Sports_achievment == "yes" :
            print("congratualtions you get the sports scholarship.")

        else :
            print("sorry but you are not eligible for scholarship.")

elif Percentage > 60 :
    Sports_achievment = input("do you have any sports achivemnet say yes or no : ")

    if Sports_achievment == "yes" :
        print("congratualtions you get the sports scholarship.")

    else :
        print("sorry but you are not eligible for scholarship.")

else :
        print("Because your percentage is below 60. Sorry but you are not eligible for scholarship.")