from naoqi.naoqi import ALModule

nextExercise = None

class Callback(ALModule):
    def pictureChanged(self, strVarName, value, strMessage):
        pass
            
def pictureChanged(strVarName, value, strMessage):        
    try:
        global nextExercise
        nextExercise = value[1][0][0][1]
    except IndexError:
        pass
