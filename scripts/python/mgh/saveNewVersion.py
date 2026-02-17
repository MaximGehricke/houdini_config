#saveNewVersion
#version up and save the current file
#icon=SOP_file
#hotkey = F12

import hou, os


def main(**kwargs):
    workfile = hou.hipFile.path()
    
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
    version = "v"+str(latest+1).zfill(3)
    file = file.replace(orig_version,version)
    
    fileToSave = path+file
    print(fileToSave)
    hou.hipFile.save(fileToSave)
    


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()