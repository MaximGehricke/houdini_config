#viz
#visualize parts of your scene using template flags
#icon = SOP_visualize
#hotkey = M

import hou

def clean_label(name):
# Words we know are just 'tags' and don't want on buttons
    garbage = {'VIZ', 'OUT', 'IN', 'RENDER', 'GRP', 'PREVIEW', 'GEO'}
    
    # 1. Split name into pieces: "VIZ_hans_OUT" -> ["VIZ", "hans", "OUT"]
    parts = name.split('_')
    
    # 2. Keep the piece only if its uppercase version isn't in our garbage list
    # and if the piece actually has content
    clean_parts = [p for p in parts if p.upper().rstrip('0123456789') not in garbage and p]
    
    # 3. Join them back together
    # If we filtered everything out (unlikely), just return the original name
    return "_".join(clean_parts) if clean_parts else name
    
    
def curContext():
    network = hou.ui.curDesktop().paneTabUnderCursor()
    if not network:
        return None
    return network.pwd() # Return the node object, not just the path string


def solidTemplate():
    pane = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.SceneViewer)
    if not pane: return
    settings = pane.curViewport().settings()
    tmplset = settings.displaySet(hou.displaySetType.TemplateModel)
    tmplset.setShadedMode(hou.glShadingType.Smooth)
    tmplset.useGhostedLook(0)


def getViz():
    parent = curContext()
    if not parent: return []
    # Use children() to get actual node objects to check names
    return [n for n in parent.children() if "VIZ_" in n.name()]


def viz_on():
    solidTemplate()
    for node in getViz():
        node.setTemplateFlag(True)


def viz_off():
    for node in getViz():
        node.setTemplateFlag(False)


def createViz():
    network = hou.ui.curDesktop().paneTabUnderCursor()
    if not network: return
    
    parent = network.pwd()
    pos = network.cursorPosition()

    selectedNodes = hou.selectedNodes()
    lastNode = None

    # Find lowest selected node
    lowestPos = 1000000000
    for node in selectedNodes:        
        position = node.position()[1]
        if position < lowestPos:
            lowestPos = position
            lastNode = node
            
    vizzer = parent.createNode('null')
    vizzer.setPosition(pos)
    vizzer.setUserData("nodeshape", "oval")
    vizzer.setColor(hou.Color((0.18, 0.18, 0.18)))
    vizzer.setName("VIZ_01", unique_name=True)
    
    if lastNode:
        vizzer.setInput(0, lastNode)
        vizzer.moveToGoodPosition()
        lastName = clean_label(lastNode.name())
        print(lastName)
        vizzer.setName(f"VIZ_{lastName}", unique_name=True)
    
    vizzer.setSelected(True, clear_all_selected=True)


def toggle_specific(node):
    state = node.isTemplateFlagSet()
    node.setTemplateFlag(not state)
    

def main(**kwargs):   
    try:
        import mghui.radialMenu as radial_menu
    except ModuleNotFoundError:
        import os
        parent_dir = os.path.dirname(os.path.dirname(__file__))
        path_hint = os.path.join(parent_dir, "mghui", "radialMenu.py")
        hou.ui.displayMessage(f"Radial menu is not available. Make sure it's installed under: {path_hint}")
        exit()

    import re

    # --- Build the Menu ---
    vizzers = getViz()
    actions = {
        "ADD VIZ": createViz,
        "ALL ON": viz_on,
        "ALL OFF": viz_off
    }

    # Dynamically add the specific toggles
    for node in vizzers:
        label = node.name().replace("VIZ_", "")
        # Note: n=node is required to lock the variable inside the loop
        actions[label] = lambda n=node: toggle_specific(n)

    radial_menu.run(actions)
