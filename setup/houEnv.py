#houEnv
#sets up the Houdini Environment
import time, os, sys

locations = ["C:/Users/Maxim/Documents/","/net/homes/mgehrick/"]

boilerplate = '''
# ===============================================================
# My Custom Houdini Environment
# ===============================================================

# 1. Define the root of our Git repository. 
# windows path: HOUDINI_REPO = "Z:/houdini_config/"
# linux path: HOUDINI_REPO = "/net/homes/mgehrick/houdini_config"

# 2. Add our repo to Houdini's search path.
#    The '&' tells Houdini to also include the default paths.
HOUDINI_PATH = "$HOUDINI_REPO;&"

# 3. Point to specific directories for better organization and performance.
HOUDINI_TOOLBAR_PATH = "$HOUDINI_REPO/toolbar;&"
HOUDINI_OTLSCAN_PATH = "$HOUDINI_REPO/hda;&"

# 4. Add our python scripts to the PYTHONPATH so Houdini can find them.
PYTHONPATH = "$HOUDINI_REPO/scripts/python;&"

# 5. Add our VEX includes to the VEX path.
HOUDINI_VEX_PATH = "$HOUDINI_REPO/scripts/vex;&"

'''


def winOrLinux():

    if sys.platform.startswith('win'):
        return "windows"  
    elif sys.platform.startswith('linux'):
        return "linux"
    else:
        return "other"
    
def findHoudiniEnv(loc):
    #finds install location of Houdini
    print("Searching locations: "+str(loc))
    houdini_folders = []
    for path in loc:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                # Convert the directory name to lowercase for case-insensitive matching
                if "houdini" in dir_name.lower():
                    for root, dirs, files in os.walk(os.path.join(root, dir_name)):
                        for file in files:
                            # print(str(file))
                            if "houdini.env" in file.lower():
                                full_path = os.path.join(root, dir_name, file)
                                if not "backup" in full_path.lower():
                                    print(f"[FOUND]   '{dir_name}' (Full path: {full_path})")
                                    houdini_folders.append(full_path)
    if not houdini_folders:
        houdini_folders = input("Pls enter path to houdini.env : ")
    return [item.replace("\\", "/").replace("\\","/") for item in houdini_folders]
        


def main():
    system = winOrLinux()
    print(system)
    
    print("folder: ", findHoudiniEnv(locations))
    print("done")

    # if os == "windows":
    #     output = boilerplate.replace("# windows path: ","")
    # else:
    #     output = boilerplate.replace("# linux path: ","")
    # print(output)
    #time.sleep(10)



if __name__ == "__main__":
    main()