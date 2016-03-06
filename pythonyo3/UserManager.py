from User import User

class UserManager:
    def __init__(self):
        self.userList=[]

    ###prints out userList in a pretty format###
    def displayUsers(self):
        pass

    ###takes in a User object###
    ###returns 0 if user already in list###
    ###returns 1 if user was added###
    def addUser(self,user):
        for i in self.userList:
            if(i.ID==user.ID):
                return 0
        self.userList.append(user)
        return 1

    ###takess in a userID (int)###
    ###returns 1 if user was deleted###
    ###returns 0 if user was not found in userlist###
    def removeUser(self,userID):
        count=0
        for i in self.userList:
            if(i.ID==userID):
                self.userList.pop(count)
                return 1
            count+=1
        return 0

    ###finds all users with matching ###
    def findUsers(self,username):
        alist=[]
        for i in self.userList:
            if(i.username==username):
                alist.append(i)
        
    ###allows user to update any User Object's information interactively###
    def updateUser(self,userID):
        ###interactive###
        pass

    ###takes in a tuple with all User Object attributes and constructs###
    ###and puts User in userList###
    def userFactory(self,tup):
        user = User(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5])
        self.userList.append(user)
        
