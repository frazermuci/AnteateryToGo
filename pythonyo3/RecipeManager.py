from Recipe import Recipe
class RecipeManager:
    def __init__(self):
        self.recipeList=[]

    ###takes in a Recipe object###
    ###returns 0 if recipe already in list###
    ###returns 1 if recipe was added###
    def addRecipe(self,recipe):
        for i in self.recipeList:
            if(i.ID==recipe.ID):
                return 0
        self.recipeList.append(recipe)
        return 1

    ###takes in recipeID (int)###
    ###returns 1 if recipe was deleted###
    ###returns 0 if recipe was not found in recipeList###
    def removeRecipe(self,recipeID):
        count=0
        for i in self.recipeList:
            if(i.ID==recipeID):
                self.recipeList.pop(count)
            count+=1

    ###finds recipe by ID###
    def findRecipe(self, recipeID):
        count =-1
        num=0
        for i in self.recipeList:
            num+=1
            if(i.ID==recipeID):
                count =num
        return count

    ##calculates the rating of the recipes that have been rated##
    def calculateAverageRating(self,userManager):
        for user in userManager.userList:
            for rating in user.recipesRated:
                index =self.findRecipe(rating)
                if(index!=-1):
                    tup=self.recipeList[index-1].rating
                    num1=(tup[1]-user.recipesRated[rating])
                    num2=(tup[2]-1)
                    
                    num1+=user.recipesRated[rating]
                    num2+=1
                    num3=(num1/num2)
                    self.recipeList[index-1].rating=(num3,num1,num2)

    ###takes in a tuple with all Recipe Object attributes and constructs###
    ###and puts Recipe in recipeList###
    def recipeFactory(self,tup):
        recipe = Recipe(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5],tup[6])
        self.recipeList.append(recipe)
        
