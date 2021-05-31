import random

payoff = [[0,1,-1],[-1,0,1],[1,-1,0]]

red_hawks = int(input("Enter the Red hawks on the isand"))
snake = int(input("Enter the number of snakes on the isand"))
puma = int(input("Enter the number of Puma on the isand"))

red_hawks_counter = 0
snake_counter = 0
puma_counter = 0

population = red_hawks + snake + puma

animals  = ['red_hawks','snake','puma']

for i in range(30):
    while True:
        animal_1 = animals.index(random.choice(animals))
        animal_2 = animals.index(random.choice(animals))
        # print(animal_1)
        # print(animal_2)

        result = payoff[animal_1][animal_2]
        # print(result)

        if (result == -1):
            prey = animals[animal_1]
            # print(prey)
        elif(result == 1):
            prey = animals[animal_2]
            # print(prey)
        elif(result == 0):
            prey = 'none'
        
        if(prey =='puma'and puma>0):
            puma = puma-1
        elif(prey =='snake' and snake>0):
            snake = snake-1
        elif(prey =='red_hawks' and red_hawks>0):
            red_hawks= red_hawks-1

        if(puma == 0 and snake==0):
            #print("No of red_hawks left"+str(red_hawks))
            red_hawks_counter = red_hawks_counter+1;
            break;
            

        if(puma == 0 and red_hawks==0):
            #print("No of snakes left"+str(snake))
            snake_counter = snake_counter+1
            break;
            

        if(snake == 0 and red_hawks==0):
            #print("No of puma left"+str(puma))
            puma_counter = puma_counter + 1
            break;

print("Number of times snakes were left are : " + str(snake_counter))
print("Number of times red_hawks were left are : " + str(red_hawks_counter))
print("Number of times puma were left are : " + str(puma_counter))            


#print(animal_1)
#print(animal_2)

# for i in range(3):
#     for j in range(3):
#         print(payoff[i][j]) 
#         if(i == j):
    


