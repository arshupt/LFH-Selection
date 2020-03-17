class Tech:

    def __init__(self):

        self.position="null"

        self.availableStartTime = 9

        self.availableEndTime = 16

        self.Mentor=[]

        self.Learner=[]


    def addStacks(self):

        self.stack=[]

        interests = input("Enter the area of interests/expertises: ")

        x=interests.split(",")

        self.stack.append(x)

        self.setMentorOrLearner()


    def setMentorOrLearner(self):

        
val = input("Are you a mentor or learner. Enter 1 for mentor and 2 for learner: ")

        val=int(val)

        if val == 1:

            self.position="mentor"

        elif val == 2:

            self.position="learner"

        else:

            print("Invalid value")

        
if self.position=="mentor":

            self.Mentor.append(self.stack)

            self.setAvailableTime()

        elif self.position=="learner":

            self.Learner.append(self.stack)

            self.getMentor()

    def setAvailableTime(self):

        if self.position=="mentor":

            start = input("Enter the availability starting time(in hours): ")

            stop = input("Enter the availability ending time(in hours): ")

            start=int(start)

            stop=int(stop)

            self.availableStartTime=start

            self.availableEndTime=stop

    def getMentor(self):

        def checkMentor(y):

            for i in self.Mentor:

                for x in i:

                    for z in x:

                         if y == z:

                            return 1

            return 0

                                     

        for x in self.stack:     

            for y in x:

                val=checkMentor(y)

                if val==1:

                    print("Mentor Available for "+ y)

                else:

                    print("Mentor not available for "+ y)


c=Tech()

c.addStacks()

c.addStacks()

c.addStacks()