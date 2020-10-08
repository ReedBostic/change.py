#Name: Reed Bostic
#Date: 10/7/2020
#Description: A program that calculates change.

print('Please enter an amount in cents less than a dollar.')
money = int(input())
Q = money // 25
D = (money%25) // 10
N = (money%25%10) // 5
P = money % 5

print("Your change will be:")
print("Q:",Q)
print("D:",D)
print("N:",N)
print("P:",P)

