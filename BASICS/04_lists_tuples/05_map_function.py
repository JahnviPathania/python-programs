#map function allows you to transform list elements to get a new element
# we can transfrom them by using for loop
bonuses=[200,300,400,500,600]
new_bonuses=[]
for bonus in bonuses:
    new_bonuses.append(bonus*2)
    
print(new_bonuses)
#but python allows map() function to do the same
def double(bonus):
    return bonus*2
bonus=[200,300,400]
iterator=map(double,bonus)
print(list(iterator))

#we can also use lambda function
bonus1=[200,300,400,500]
iterator1=map(lambda bonus:bonus*2,bonus1)
print(list(iterator1))
#example
ls=["jahnvi","ashutosh","karan","chaitali"]
iterator2=map(lambda x: x.capitalize(),ls)
print(list(iterator2))