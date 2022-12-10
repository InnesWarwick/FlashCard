#Innes Warwick 
#somtime in 2022
import random 


def main():
    print("-help for info")
    commandInput = input(": ")
    CommandProcessor(commandInput)


#command processor manages command input and redirects to correct function
def CommandProcessor(commandInput):
    #converts input string to list
    commandList = commandInput.split()
    #takes first list value
    commandType = commandList[0]
    #removes command type just leaving data
    del commandList[0]
    #converts data back to string
    commandData = ' '.join(commandList)
    print(commandData)
    #switch staments :))
    match commandType:
        case 'c':
            CreateCard(commandData)
        case 'q':
            AskCard()


def CreateCard(question):
    answer = input(": ")
    #creates string of my data type thing
    data = f"{question}~{answer}"
    #wrties to high priority by deafault
    f = open("cards/highP.txt", "a")
    f.write(data+"\n")
    f.close()
    
#bro idk ngl i enterd a trance this is schizo conde ong
def AskCard():
    pPick = random.randint(0,100)
    fileName = ""

    try:
        if pPick >= 80:
            fileName = "lowP.txt"
    except:
        pPick = random.radint(0,79)
    finally:
        try:
            if pPick >= 50:
                fileName = "mediumP.txt"
        except:
            pPick = random.randint(0,49)
        finally:
            fileName = "highP.txt"

    f = open(f"cards/{fileName}","r")
    lines = f.readlines()
    f.close()
    QueAnsFull = random.choice(lines)
    QueAns = QueAnsFull.split("~")
    question = QueAns[0]
    answer = QueAns[1]
    input(question)
    print(answer)
    priorityPick = input("easy(1) medium(2) hard(3): ")
    match priorityPick:
        case "1":
            if fileName == "lowP.txt":
                return
            else:
                FileRewrite(fileName,"lowP.txt",lines,QueAnsFull)
        case "2":
            if fileName == "mediumP.txt":
                return
            else:
                FileRewrite(fileName,"mediumP.txt",lines,QueAnsFull)
        case "3":
            if fileName == "highP.txt":
                return
            else:
                FileRewrite(fileName,"highP.txt",lines,QueAnsFull)


def FileRewrite(sourceFile,destFile,dataList,chosenLine):
    f = open(f"cards/{sourceFile}", "w")
    for line in dataList:
        if line != chosenLine:
            f.write(line)
    f.close()
    f = open(f"cards/{destFile}", "a")
    f.write(chosenLine)
    f.close
    return




if __name__ == "__main__":
    main()
