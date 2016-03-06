

class User:
    def __init__(self,contact,username,password,ID,recipesMade=[],recipesRated=dict()):
        ##string##
        self.contact=contact
        self.username=username
        self.password =password

        ##int##
        self.ID=ID

        ##Recipe.ID [] (int)##
        self.recipesMade=recipesMade

        ##dictionary key is recipe ID that was rated##
        ##value is the rating 1-5##
        self.recipesRated=recipesRated


    ####mutators####
    def addRecipeToRecipesMade(self,recipe):
        self.recipesMade.append(recipe)

    def addRecipeToRecipesRated(self,recipe):
        self.recipesRated.append(recipe)

    def removeRecipeFromRecipesMade(self,string):
        ##this will remove by name for now but we could extend that
        num =len(self.recipesMade)
        for i in range(num):
            if(self.recispesMade[i].name==string):
               self.recipesMade.pop(i)

    def removeRecipeFromRecipesRated(self,string):
        ##this will remove by name for now but we could extend that
        num =len(self.recipesRated)
        for i in range(num):
            if(self.recipesRated[i].name==string):
               self.recipesRated.pop(i)
                
                

    ####operators####
    ###for sorting purposes###
    def __lt__(self,rhs):
        if(self.username==rhs.username):
            return self.ID<rhs.ID
        return self.username<rhs.username
    #def __eq__(self,rhs):
     #   return self.ID == rhs.ID

