import hou

# Initialize session keys if they don't exist
if not hasattr(hou.session, "sr_search"):
    hou.session.sr_search = ""
if not hasattr(hou.session, "sr_replace"):
    hou.session.sr_replace = ""

labels = ["Search for:", "Replace with:"]
defaults = [hou.session.sr_search, hou.session.sr_replace]

status, values = hou.ui.readMultiInput(
    "Search and Replace (Session Memory)", 
    labels, 
    initial_contents=defaults,
    title="Global Search/Replace"
)

if status == 0 and values:
    search, replace = values[0], values[1]
    
    # Update session memory
    hou.session.sr_search = search
    hou.session.sr_replace = replace
    
    sel = hou.selectedNodes()
    if not sel:
        hou.ui.displayMessage("No nodes selected.")
    else:
        with hou.undos.group("Batch Search and Replace"):
            count = 0
            for node in sel:
                for parm in node.parms():
                    if isinstance(parm.parmTemplate(), hou.StringParmTemplate):
                        raw_val = parm.rawValue()
                        if search in raw_val:
                            parm.set(raw_val.replace(search, replace))
                            count += 1
            hou.ui.displayMessage(f"Updated {count} parameters.")