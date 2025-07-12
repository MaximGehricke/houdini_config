#bypassDebug
#bypasses nodes with "DEBUG" in the name. You can specify certain path as a str list in main()
# icon = DIALOG_error

import hou

def main(search_paths = [''],**kwargs):
    # search_path : List of specific paths at which to search for "DEBUG" nodes
    curPath = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor).pwd().path()
    search_paths.append(curPath)

    found_paths = []

    
    for path in search_paths:
        parent_node = hou.node(path)
        if parent_node:
            # Iterate through all child nodes of the parent node
            for node in parent_node.children():
                # Check if "DEBUG" is in the node's name
                if "DEBUG" in node.name():
                    node.bypass(1)                       
                    # If found, append the path to the list
                    found_paths.append(node.path())
        
        # Display a message popup with the found paths
    if found_paths:
        message = "Bypassed DEBUG nodes at the following paths:\n" + "\n".join(found_paths)
        hou.ui.displayMessage(message, title="DEBUG Nodes Found", severity=hou.severityType.Message)



if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()