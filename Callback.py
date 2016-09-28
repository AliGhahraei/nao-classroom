from naoqi import ALModule

class Callback(ALModule):
    def __init__(self):
        """python class myModule test auto documentation"""
        self.nextExercise = None

    def pictureChanged(self, strVarName, value, strMessage, callbackCalled):
        """callback when data change"""
        try:
            nextExercise = value[1][0][0][1]
        except IndexError:
            pass