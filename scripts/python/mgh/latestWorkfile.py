#latestWorkfile
#loads the latest workfile from a selection. Meant to be customized manually for a show.
#icon = SOP_file

import hou, os

##########################################################
#ADD YOUR WORKFILES HERE:

#add it to option
options = ("copy current .hip path","f")
#...and create a variable of the same name containing the workfile path

filename = """/path/to/file/filename"""

##########################################################


def main(**kwargs):
    #choose workfile:
    choice = hou.ui.selectFromList(options,exclusive=True)
    if not choice:
        exit()

    #if first option is selected, copy to clipboard
    if choice[0]==0:
        hou.ui.copyTextToClipboard(hou.hipFile.path())
        exit()


    try:
        choice = int(choice[0])
    except:
        print("latestWorkfile -- improper selection!")
        exit()
    workfile = (eval(str(options[choice])))


    #load the latest workfile:
    file = workfile.split("/")[-1]
    path = workfile.replace(file,"")

    orig_version = file.split(".hip")[0].split("_")[-1]
    basename = file.split(orig_version)[0]
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
    file = file.replace(orig_version,version)

    fileToLoad = path+file
    print(fileToLoad)
    hou.setUpdateMode(hou.updateMode.Manual)
    hou.hipFile.load(fileToLoad,suppress_save_prompt=True)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()