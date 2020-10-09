import sys
import random
import datetime

sum1 = 0
my_dict = {}

n = int(input("How Many cities do you want to include for Analysis ? : "))
if n < 3:
    sys.exit("Please provide a minimum 3 cities.")

t = int(input("How Many days do you want for Analysis ? : "))
if t < 5:
    sys.exit("Please provide a minimum 5 days.")


def random_count():
    r = random.randint(0, 1000)
    return r


for i in range(n):
    print("\n")
    c = str(input("Please Enter city name : "))
    for j in range(t):
        a = (datetime.date.today() - datetime.timedelta(j))
        indian_format = a.strftime("%d/%m/%Y")
        num =  ()
        print(c, "Corona Patient Number On -", indian_format, ":", num)
        sum1 = sum1 + num
    avg = sum1 / t
    print("Average Cases: ", avg)
    sum1 = 0
    my_dict.update({c: avg})

max_avg = max(my_dict, key=my_dict.get)
print("\n")
print("The Most Affected City is : ", max_avg)
min_avg = min(my_dict, key=my_dict.get)
print("The Least Affected City is : ", min_avg)
