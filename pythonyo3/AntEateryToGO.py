from FileManager import FileManager
from User import User
from Recipe import Recipe

class AntEateryToGO:
    def __init__(self):
        self.boolLogin=False
        self.quit=False
        self.fileManager = FileManager()
        self.userIDassign=0
        self.recipeIDassign=0

    def newUser(self):
        print("Welcome to AntEateryToGo, the only eating experience known by that name\n")
        if(len(self.fileManager.userManager.userList)!=0):
            while(True):
                yn=input("New user? [y/n]: ")
                if(yn in ["y","n"]):
                    return yn
                else:
                    print("Please select yes or no\n")
        else:
            return "y"
                 
    def makeUser(self):
        print("\nPlease enter your information and we can get you started")
        contact=input("Email: ")
        while(True):
            userName=input("User name:")
            if(userName =="quit"):
                self.quit =True
                return
            boolean=True
            for user in self.fileManager.userManager.userList:
                if(user.username==userName):
                    boolean=False
                    break
            if(boolean):
                break
            print("\nThat username is already taken please make another")
        password=input("password: ")
        if(password =="quit"):
            self.quit =True
            return
        self.userIDassign+=1
        Id= self.userIDassign
        self.userIn=User(contact,userName,password,Id)
        self.fileManager.userManager.userList.append(self.userIn)
        print("\nWelcome {0}\n".format(userName))

    def logIn(self):
        print("\nLogin")
        while(True):
            userName=input("User name: ")
            if(userName =="quit"):
                    self.quit=True
                    return
            password=input("Password: ")
            if(password =="quit"):
                    self.quit=True
                    return

            for user in self.fileManager.userManager.userList:
                if(user.username==userName and password==user.password):
                    self.userIn=user
                    print("\nWelcome {0}\n".format(userName))
                    return

            print("User name, password combination incorrect\n")

    def featureOptions(self):
         while(True):
            print(" 1. Search Recipes under certain cook time\n",
                "2. Search Recipes by maker ID\n",
                  "3. Search Recipes with certain ingredients\n",
                  "4. Search Recipes by their name\n",
                  "5. Search Users\n",
                  "6. Make Recipe")
            num=input("What number do you want to do: ")

            if(num in ["logout","quit"]):
                self.boolLogin=False
                if(num=="quit"):
                    self.quit=True
                return

            if(num in ["1","2","3","4","5","6"]):
                return int(num)
            print("\nIncorrect input, please input 1-6\n")
                
    def getRecipe(self,resultList):
        while(True):
            yn=input("Would you like to pick a recipe [y/n]: ")
            if(yn in["logout","quit"]):
                self.boolLogin=False
                if(yn=="quit"):
                    self.quit=True
                return
            if(yn not in ["y","n"]):
                print("Please select yes or no\n")
                continue
            break
        if(yn =="y"):
            while(True):
                try:
                    num=input("Please enter the number of the recipe you want: ")
                    if(yn in["logout","quit"]):
                        self.boolLogin=False
                        if(yn=="quit"):
                            self.quit=True
                        return
                    if(int(num)-1 not in range(len(self.fileManager.recipeManager.recipeList))):
                        print("\nNot a number on the list, please try again")
                        continue
                    print(resultList[int(num)-1])
                    break
                except:
                    print("\nPlease insert an integer")
        else:
            return
        while(True):
            yn=input("Would you like to rate this recipe [y/n]: ")
            if(yn in["logout","quit"]):
               self.boolLogin=False
               if(yn=="quit"):
                   self.quit=True
               return
            if(yn not in ["y","n"]):
                print("Please select yes or no\n")
                continue
            break

        if(yn=="y"):
            while(True):
                try:
                    num2=input("Please enter a rating 1-5: ")
                    if(yn in["logout","quit"]):
                        self.boolLogin=False
                        if(yn=="quit"):
                            self.quit=True
                        return
                    if(int(num2) not in range(6)):
                        print("\nNot 1-5, please try again")
                        continue
                    self.userIn.recipesRated[resultList[int(num)-1].ID]=int(num2)
                    break
                except:
                    print("\nPlease insert an integer")
                                
            
                
                
    def searchRecipesTime(self):
        result=[]
        while(True):
            try:
                num=input("Enter number for how much time(in minutes)you have: ")
                if(num in ["logout","quit"]):
                    self.boolLogin=False
                    if(num=="quit"):
                        self.quit =True
                    return
                for recipe in self.fileManager.recipeManager.recipeList:
                    if(int(num)>=recipe.time):
                        result.append(recipe)
                count=0
                for i in result:
                    count+=1
                    str0 = '{:<5}'.format(str(count))
                    str1='{:<15}'.format("time: " + str(i.time))
                    str2='{:<15}'.format("ID: " + str(i.ID))
                    str3='{:<30}'.format("Name: "+i.name)
                    print(str0+str1+ str2+str3)
                print()
                break
            except:
                print("\nPlease insert an integer value")
        if(len(result)==0):
            print("No recipe was found\n")
        else:
            self.getRecipe(result)
            
    def searchRecipesMaker(self):
        result=[]
        while(True):
            try:
                num=input("Enter number for maker ID: ")
                if(num in ["logout","quit"]):
                    self.boolLogin=False
                    if(num=="quit"):
                        self.quit =True
                    return
                for recipe in self.fileManager.recipeManager.recipeList:
                    if(int(num)==recipe.makerID):
                        result.append(recipe)
                count=0
                for i in result:
                    count+=1
                    str0 = '{:<5}'.format(str(count))
                    str1='{:<20}'.format("Maker ID: " + str(i.makerID))
                    str2='{:<15}'.format("ID: " + str(i.ID))
                    str3='{:<30}'.format("Name: "+i.name)
                    print(str0+str1+ str2+str3)
                print()
                break
            except:
                print("\nPlease insert an integer value")
        if(len(result)==0):
            print("No recipe was found\n")
        else:
            self.getRecipe(result)
                
    def searchRecipeIngredients(self):
        ingredients=[]
        result=[]
        print("Keep entering ingredients till your done (q when done)")
        st=""
        while(st!="q"):
            st = input("Which ingredient do you want to search for: ")
            if(st in ["logout","quit"]):
                    self.boolLogin=False
                    if(st =="quit"):
                        self.quit =True
                    return
            if(st!="q"):
                ingredients.append(st)
        
        for recipe in self.fileManager.recipeManager.recipeList:
            check =True
            for i in ingredients:
                if(i not in recipe.ingredients):
                    check = False
                    break
            if(check):
                result.append(recipe)

        count=0
        for i in result:
            count+=1
            str0 = '{:<5}'.format(str(count))
            str1='{:<15}'.format("ID: " + str(i.ID))
            str2='{:<15}'.format("Name: "+i.name)
            str3='{:<40}'.format("Ingredients: " + str(i.ingredients))
            print(str0+str1+ str2+str3)
        print()
        
            
        if(len(result)==0):
            print("No recipe was found\n")
        else:
            self.getRecipe(result)

    def searchRecipeName(self):
        result=[]
        st=input("Enter name for recipe name: ")
        if(st in ["logout","quit"]):
            self.boolLogin=False
            if(st=="quit"):
                self.quit =True
            return
        for recipe in self.fileManager.recipeManager.recipeList:
            if(st==recipe.name):
                result.append(recipe)
        count=0
        for i in result:
            count+=1
            str0 = '{:<5}'.format(str(count))
            str1='{:<15}'.format("ID: " + str(i.ID))
            str2='{:<30}'.format("Name: "+i.name)
            print(str0+str1+ str2)
        print()
        if(len(result)==0):
            print("No recipe was found\n")
        else:
            self.getRecipe(result)

    def searchUsers(self):
        result=[]
        st=input("Enter name of user to search for: ")
        if(st in ["logout","quit"]):
            self.boolLogin=False
            if(st=="quit"):
                self.quit =True
            return
        for user in self.fileManager.userManager.userList:
            if(st==user.username):
                result.append(user)
        count=0
        for i in result:
            count+=1
            
            str0 = '{:<5}'.format(str(count))
            str1 ='{:<15}'.format("Name: "+i.username)
            str1 ='{:<25}'.format("Contact: "+i.contact)
            str2='{:<15}'.format("ID: " + str(i.ID))
            str3='{:<30}'.format("Recipes: "+str(i.recipesMade))
            print(str0+str1+ str2+str3)
        print()
        if(len(result)==0):
            print("No user was found\n")

    def makeRecipe(self):
        ingredients=[]
        steps=[]
        name=input("Enter name of the recipe: ")
        if(name in ["logout","quit"]):
                    self.boolLogin=False
                    if(name =="quit"):
                        self.quit =True
                    return
        print("Keep entering ingredients till your done (q when done)")
        st=""
        while(st!="q"):
            st = input("Which ingredient do you want in your recipe: ")
            if(st in ["logout","quit"]):
                    self.boolLogin=False
                    if(st =="quit"):
                        self.quit =True
                    return
            if(st!="q"):
                ingredients.append(st)
        print("Keep entering steps till your done (q when done)")
        st=""
        while(st!="q"):
            st = input("Which step do you want in your recipe: ")
            if(st in ["logout","quit"]):
                    self.boolLogin=False
                    if(st =="quit"):
                        self.quit =True
                    return
            if(st!="q"):
                steps.append(st)

        while(True):
            time = input("Enter time it takes to cook the recipe: ")
            if(time in ["logout","quit"]):
                self.boolLogin=False
                if(time =="quit"):
                    self.quit =True
                return
            try:
                time=int(time)
                break
            except:
                print("\nPlease insert an integer value")
        self.recipeIDassign+=1
        recipe=Recipe(name,ingredients,steps,self.userIn.ID,time,self.recipeIDassign)
        self.fileManager.recipeManager.recipeList.append(recipe)
        self.userIn.recipesMade.append(self.recipeIDassign)

    def Run(self):
        self.fileManager.read()
        for user in self.fileManager.userManager.userList:
            if(user.ID>self.userIDassign):
                self.userIDassign=user.ID

        
        for recipe in self.fileManager.recipeManager.recipeList:
            if(recipe.ID>self.recipeIDassign):
                self.recipeIDassign=recipe.ID
                
        while(True):
            if(not self.boolLogin):
                yn=self.newUser()
                if(yn=="n" and len(self.fileManager.userManager.userList)!=0):
                    self.logIn()
                    if(self.quit):
                        break
                else:
                    self.makeUser()
                    if(self.quit):
                        break
                self.boolLogin = True

            option=self.featureOptions()
            if(self.quit):
                break
            if(not self.boolLogin):
                continue
            optList=[self.searchRecipesTime,
                         self.searchRecipesMaker,
                         self.searchRecipeIngredients,
                         self.searchRecipeName,
                         self.searchUsers,
                         self.makeRecipe]
            count=0
            for i in optList:
                if(count==option-1):
                    i()
                    break
                count+=1
            if(self.quit):
                break
            if(not self.boolLogin):
                continue
       
        self.fileManager.write()

a= AntEateryToGO()
a.Run()
            
