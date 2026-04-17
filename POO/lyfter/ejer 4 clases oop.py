class Head:

    def __init__(self,head,neck):
        self.head=head
        self.neck=neck

class Torso:

        def __init__(self,chest):
            self.chest=chest


class Arms:

    def __init__(self):
        self.right_arm
        self.left_arm
        

class Hands:

    def __init__(self):
        self.left_hand
        self.right_hand

class Leg:

    def __init__(self):
        self.right_leg
        self.left_leg
    
class Human:

    def __init__(self):
        self.arms=Arms()+Hands()
        self.torso=Torso()+Head()
        self.legs=Leg()
        self.human=self.arms+self.torso+self.legs

human1=Human()
human2=Human()
