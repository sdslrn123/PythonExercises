story=[]
print("Enter details with a , separating the elements")
string=input("Enter details of a main character, an object, a verb \n")
story=string.split(",")
printedStory=(str(story[0])+str(story[2])+str(story[1]))
print(type(printedStory))
print (printedStory)
