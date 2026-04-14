#houEnv
#sets up the Houdini Environment
import time, os, sys, re

locations = ["C:/Users/Maxim/Documents/","/net/homes/mgehrick/"]
thisPath = os.path.abspath(__file__).replace("\\","/").replace("/setup/houEnv.py","")

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


def readBoilerplate():
    # Get the dir of current script and return boilerplate.txt in same dir
    bpfile = os.path.dirname(os.path.abspath(__file__))+"/boilerplate.txt"
    try:
        with open(bpfile, 'r') as f:
            print("reading boilerplate.txt ...")
            return str(f.read())
    except IOError as e:
        print(f"Error: Could not read boilerplate file: '{bpfile}'. Reason: {e}")






def updateEnv(folders, bp):
    for folder in folders:
        folder.replace("houdini.env","")
        env = folder + "/houdini.env"
        env.replace("//","/").replace("\\","/")
        print("appending to ", env)
        try:
            with open(env, 'r') as f:
                if bp in str(f.read()):
                    print(f"already installed in '{env}'")
                    continue
                with open(env, 'a') as f:
                    f.write(bp)
            
            print(f"Successfully appended to '{env}'")

        except IOError as e:
            print(f"Error: Could not write to file '{env}'. Reason: {e}")


def main():
    system = winOrLinux()
    print("os is ", system)
    time.sleep(1)
    print("\n")
    time.sleep(0.5)    
    envPaths =  findHoudiniEnv(locations)
    # print("folder: ", envPaths)
    time.sleep(2)
    print("\n")
    time.sleep(0.5)
    print("\n")
    time.sleep(0.5)
    print("\n")
    bp = readBoilerplate().replace("addPathToConfigFolderHere",thisPath)
    time.sleep(0.5)
    print("\n")
    time.sleep(0.5)
    print("\n")
    print("\n")
    time.sleep(0.5)
    print("\n")
    updateEnv(envPaths,bp)
    
    time.sleep(0.2)
    print("\n")
    time.sleep(0.2)
    print("\n")
    time.sleep(10)



if __name__ == "__main__":
    main()