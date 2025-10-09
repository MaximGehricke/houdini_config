#latestWorkfile2.0
#loads the latest workfile from a selection. Meant to be customized manually for a show.
#icon = SOP_file

datafileName = "latestWorkfile.csv"

import hou, os
import csv

def getOptions():
        #returns a dictionary of names and paths from a csv file
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        datapath = parent_dir.split("python")[0]+"data/"+datafileName

        choices = {}
        with open(datapath, newline='') as csvfile:
                reader = csv.DictReader(csvfile,fieldnames=["n","p"])
                try:
                        for row in reader:
                            key = row['n']
                            value = row['p']                
                            choices[key]=value
                except KeyError:
                        print("end of file")


        return choices


def addCurrentFileToCsv():

    houfile = hou.hipFile.path()
    input = hou.ui.readInput("Provide a shortcut for loading this files latest:",buttons=('Accept','Cancel'),default_choice = 1, close_choice=2)
    if not input or input[0]==2:
        print("no input, exiting")
        sys.exit(0)
    else:
        houname = input
    
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    datapath = parent_dir.split("python")[0]+"data/"+datafileName
    #choices = {}
    with open(datapath, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([str(houname[1]), str(houfile)])


def main(**kwargs):
    choices = getOptions() #this is a dict like this:       { "TST" : "job/test/test/test.hip" [...] }

    menu = ["copy current .hip path","add current file"]
    menu += list(choices.keys())

    
    #choose workfile:
    choice = hou.ui.selectFromList(menu,exclusive=True)
    if not choice:
        exit()

    #if first option is selected, copy to clipboard
    if choice[0]==0:
        hou.ui.copyTextToClipboard(hou.hipFile.path())
        exit()

    if choice[0]==1:
        addCurrentFileToCsv()
        exit()

    try:
        workfile = str(choices[menu[choice[0]]])
    except:
        print("latestWorkfile -- improper selection!")
        exit()
    


    #load the latest workfile:
    workfile = workfile.replace('"',"").replace(" ","")
    houfile = workfile.split("/")[-1]
    path = workfile.replace(houfile,"")
    
    print(houfile)
    orig_version = houfile.split(".hip")[0].split("_")[-1]
    basename = houfile.split(orig_version)[0]
    filesInDir = [f for f in os.listdir(path) if os.path.isfile(path + f)]

    latest = 1
    for found in filesInDir:
        if basename:
            if(basename in found and ".hip" in found):
                ver = int(found.split(".hip")[0].split("_")[-1].replace("v",""))
                if(ver>latest): latest=ver
        else:
            print("DEBUG: no basename - does file have '_v001' in it's name?")

    print("latest: ",latest)
    version = "v"+str(latest).zfill(3)
    houfile = houfile.replace(orig_version,version)

    fileToLoad = path+houfile
    print(fileToLoad)
    hou.setUpdateMode(hou.updateMode.Manual)
    hou.hipFile.load(fileToLoad,suppress_save_prompt=True)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
