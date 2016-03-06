##read and write to file at the end of session
from RecipeManager import RecipeManager
from UserManager import UserManager
#store the info as tuples of the (problem is need to print out ID) to
#get ID of user and recipe
class FileManager:
    def __init__(self):
        ###RecipeManager###
        self.recipeManager = RecipeManager()

        ###UserManager###
        self.userManager = UserManager()

    ###reads lines as tuples with attributes from files###
    ###into recipeManager and userManager###
    def read(self):
        with open("recipes.txt","r") as f:
            for line in f:
                self.recipeManager.recipeFactory(eval(line))

        with open("users.txt","r") as file:
            for l in file:
                self.userManager.userFactory(eval(l))

        
    ###writes lines as tuples with attributes from files###
    ###to userManager and recipeManager's respective lists###
    def write(self):
        check =False
        self.recipeManager.calculateAverageRating(self.userManager)
        
        with open("recipes.txt","w") as f:
            self.recipeManager.recipeList.sort()
            for r in self.recipeManager.recipeList:
                tup= (r.name,r.ingredients,r.steps,r.makerID,r.time,r.ID,r.rating)
                if(check):
                    f.write("\n"+str(tup))
                else:
                    f.write(str(tup))
                    check=True
                
        with open("users.txt","w") as file:
            self.userManager.userList.sort()
            for u in self.userManager.userList:
                tup=(u.contact,u.username,u.password,u.ID,u.recipesMade,u.recipesRated)
                if(check):
                    file.write(str(tup))
                    check = False
                else:
                    file.write("\n"+str(tup))
    


