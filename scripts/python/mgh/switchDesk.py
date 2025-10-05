#switchDesk
#switches between desktops on click
#icon = NETWORKS_lop

import hou

def main(**kwargs):
    # Define the names of your two desktops
    desk_primary = "mgh"
    desk_secondary = "solaris_mgh"
    
    # Get the name of the currently active desktop
    current_desk_name = hou.ui.curDesktop().name()
    
    # Determine which desktop to switch to
    if current_desk_name == desk_primary:
        target_name = desk_secondary
    else:
        # If we are on the secondary OR any other desktop,
        # switch back to the primary one.
        target_name = desk_primary
    
    # Find the target desktop by its name
    target_desktop = hou.ui.desktop(target_name)
    
    # Check if the desktop file actually exists before trying to switch
    if target_desktop:
        target_desktop.setAsCurrent()
    else:
        # This is crucial error feedback for the user
        hou.ui.displayMessage(
            f"Error: Desktop '{target_name}' not found.",
            severity=hou.severityType.Error)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
