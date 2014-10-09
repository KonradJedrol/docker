n = 600851475143 #The input number
n2 = n #Copy of the input
i = 2
while i * i < n2: #The loop works as long as the product of i*i is less than the input number
     while n2 % i == 0: #The loop works as long as there is no remainder
         n2 = n2 / i
     i = i + 1

print ('The Largest Prime factor of', n,'is', n2)
