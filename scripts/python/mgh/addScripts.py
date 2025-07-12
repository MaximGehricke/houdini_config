#addScripts
#automatically adds all mgh scripts to the shelf
#icon = NETWORKS_top

import hou
import os

def main(legacy = 0):
    #set to 1 for legacy mode - copying full script into Houdini preferences
    
    # Get the location of this script
    scripts_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\","/").replace("\\","/").replace("//","/")

    #get module name
    module = scripts_dir.split("/")[-1]

    shelf_name = hou.ui.readInput("name the shelf or leave empty for module name:")[1]
    if not shelf_name:
        shelf_name = module

    # Ensure the shelf exists, or create it
    shelf = hou.shelves.shelves().get(shelf_name)
    if not shelf:
        shelf = hou.shelves.newShelf(
            name=shelf_name,
            label=shelf_name)

    # Get the current tools in the shelf (if any)
    existing_tools = list(shelf.tools())

    # Iterate over all Python scripts in the module
    for script_file in os.listdir(scripts_dir):
        if script_file.endswith(".py"):  # Only consider Python files
            script_path = os.path.join(scripts_dir, script_file)

            # Read the Python script content
            with open(script_path, "r") as file:
                script_content = file.read()

            # Extract tool name from the file
            tool_name = script_content.splitlines()[0]
            descr = script_content.splitlines()[1]
            icon =  script_content.splitlines()[2]
            code = tool_name+"\n"+descr+"\n"+icon+"\n\n"
            code += "import importlib\n"
            code += "import "+module+"."+script_file.replace(".py","")+"\n"
            code += "importlib.reload("+module+"."+script_file.replace(".py","")+")\n"
            code += module+"."+script_file.replace(".py","")+".main()"
            

            if legacy==1:
                    code=script_content

            # Create a new tool
            tool = hou.shelves.newTool(
                name=tool_name.replace(" ","").replace("#","").replace("\n",""),
                label=tool_name,
                script=code,
                icon= icon.replace(" ","").replace("#","").replace("\n","").replace("icon","").replace("=","")
            )

            # Add the tool to the list of existing tools
            existing_tools.append(tool)

    # Update the shelf with the new list of tools
    shelf.setTools(existing_tools)

    hou.ui.displayMessage(f"Shelf tools added to {shelf_name}!")


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
