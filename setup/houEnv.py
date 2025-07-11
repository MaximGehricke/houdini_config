#houEnv
#sets up the Houdini Environment
import time, os, sys, re

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

    # print("Searching locations: "+str(loc))
    houdini_folders = []
    inputPath = input("Pls enter path to houdini install: ")

    if not inputPath:
        try:
            # A robust pattern to match 'houdini' followed by a version number (e.g., 18.0, 19.5, 20)
            # The `$` at the end ensures it doesn't match names like 'houdiniBackup'
            pattern = re.compile(r'houdini\d+(\.\d+)?$', re.IGNORECASE)

            for search_dir in loc:
                # Check if the search directory itself exists
                if not os.path.isdir(search_dir):
                    continue

                # List all items (files and folders) directly inside the search directory
                for item_name in os.listdir(search_dir):
                    full_path = os.path.join(search_dir, item_name)
                    
                    # We only care about directories that match our specific Houdini version pattern
                    if os.path.isdir(full_path) and pattern.match(item_name):
                        # Final check: does this directory contain a 'houdini.env' file?
                        env_file_path = os.path.join(full_path, 'houdini.env')
                        if os.path.isfile(env_file_path):
                            # It's a valid directory. Add its path to our list.
                            # Use replace to ensure consistent forward slashes
                            normalized_path = full_path.replace("\\", "/")
                            print(f"[FOUND] {normalized_path}")
                            houdini_folders.append(normalized_path) # Appends the folder path

        except:
            inputPath = input("Pls enter path to houdini.env : ")
            houdini_folders.append(inputPath)


    else:
        houdini_folders.append(inputPath)
    return houdini_folders


def updateEnv(folders, boilerplate):
    for folder in folders:
        folder.replace("houdini.env","")
        env = folder + "/houdini.env"
        env.replace("//","/").replace("\\","/")
        print("writing to ", env)


def main():
    system = winOrLinux()
    print("os is ", system)
    time.sleep(1)
    print("\n")
    time.sleep(0.5)    
    envPaths =  findHoudiniEnv(locations)
    print("folder: ", envPaths)
    time.sleep(2)
    print("\n")
    time.sleep(0.5)
    print("\n")
    time.sleep(0.5)
    print("\n")
    if system == "windows":
        bp = boilerplate.replace("# windows path: ","")
    else:
        bp = boilerplate.replace("# linux path: ","")
    # print(bp)
    time.sleep(2)
    updateEnv(envPaths,bp)
    
    time.sleep(0.2)
    print("\n")
    time.sleep(0.2)
    print("\n")
    time.sleep(10)



if __name__ == "__main__":
    main()