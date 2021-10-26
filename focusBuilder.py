#Hoi4 Focus Tree Builder
#Joel Harder
#October 25, 2021

indentNum = 0
countryTag = ""

def toFile(string):
    global indentNum

    #open the text file
    with open("focusTree.txt", "a") as f:

        # if the first character is a curly bracket
        if string[0] == "}":
            # then decrease indent
            indentNum -= 1
        
        f.write(indent(string))
        f.write("\n")

        # if the final character was a curly bracket
        if string[len(string)-1] == "{":
            #then increase the indent
            indentNum += 1


def indent(string):
    global indentNum
    newString = ("  " * indentNum) + string
    return newString


def createFocus():
    focusID = input("Enter focus id: ")
    focusPrereq = input("Enter prerequisite focus id, or press enter to leave blank: ")
    relitivePos = "#relative_position_id = "
    if (focusPrereq):
        relitivePos = "#relative_position_id = " + focusPrereq
        focusPrereq = " focus = " + focusPrereq + " "
    
    focusString = """
    focus = {
        id = """ + focusID + """
        icon = GFX_
        
        x = 0
        y = 1
        
        cost = 10

        """ + relitivePos + """ 
        prerequisite = {""" + focusPrereq + """}
        
        completion_reward = {
            
        }

        search_filters = {}
        ai_will_do = {
            factor = 10
        }
    }"""

    return focusString


def generateHeader():
    global countryTag
    
    header = """focus_tree = {
    # PLEASE CHANGE #
    id = focus_tree_id

    country = {
        factor = 0
        
        modifier = {
            add = 10
            tag = """ + countryTag + """
        }
    }

    default = no"""

    return header



def main():
    global indentNum
    global countryTag
    
    while (len(countryTag) != 3):
        countryTag = input("Enter country tag: ")

    #put in the header
    toFile(generateHeader())

    while (True):
        #focuses
        toFile(createFocus())
        check = input("Make another focus? y/n: ")
        if (check == 'n' or check == 'N'):
            break;

    #end bracket
    toFile("}")


# clear the current contents of the file
file = open("focusTree.txt","r+")
file.truncate(0)
# 0 is the char index to start clearing from

main()
