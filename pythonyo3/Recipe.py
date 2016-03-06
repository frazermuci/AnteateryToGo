

class Recipe:
    def __init__(self,name,ingredients,steps,makerID,time,ID,rating=(0,0,0)):
        ##string##
        self.name=name
        ##string []##
        self.ingredients = ingredients
        self.steps = steps

        ##int (representing minutes)##
        self.time =time
        self.ID=ID
        self.makerID = makerID

        ##rating is three tuple##
        ##index 0 is the average rating##
        ##index 1 is the sum of ratings##
        ##index 2 is the sume of raters##
        self.rating=rating

    ###for sorting purposes###
    def __lt__(self,rhs):
        if(self.name==rhs.name):
            return self.ID<rhs.ID
        return self.name<rhs.name

    def __str__(self):
        name="Name: "+self.name+"\n"
        ingredients="Ingredients:\n"
        steps="Steps:\n"
        count =0
        for i in self.ingredients:
            ingredients +="  "+str(count+1)+" "+ self.ingredients[count]+"\n"
            count+=1
        count=0
        for i in self.steps:
            steps +="  "+str(count+1)+" "+ self.steps[count]+"\n"
            count+=1
        time="Time: "+str(self.time)+"\n"
        ID = "ID: "+str(self.ID)+"\n"
        makerID = "Maker ID: " +str(self.makerID)+"\n"
        return name+ingredients+steps+time+ID+makerID
        


