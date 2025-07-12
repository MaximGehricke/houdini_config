#PREP
#creates alembic import prep nodes
#icon = SOP_alembic

import hou

def main(**kwargs):
    #find lowest selected node:
    selectedNodes = hou.selectedNodes()

    if not selectedNodes:
        hou.ui.displayMessage("no node selected")
        exit()

    pos = 10000000000;
    for node in selectedNodes:            
        position = node.position()[1]
        if position<pos:
            pos = position
            lastNode = node

    pos = lastNode.position()
    offset = hou.Vector2(0.0,1.0)
    pathSplit = lastNode.path().split("/")
    pathSplit.pop(-1)
    path = ""
    for i in pathSplit:
        path = path + "/" + i
    color = hou.Color((0.475,0.812,0.204))


    #create nodes and set position and color
    unpack = hou.node(path).createNode('unpack')
    unpack.setPosition(pos-offset)
    unpack.setColor(color)
    conv = hou.node(path).createNode('convert')
    conv.setPosition(pos-offset-offset)
    conv.setColor(color)

    #connect nodes
    unpack.setInput(0,lastNode)
    conv.setInput(0,unpack)

    unpack.parm("transfer_attributes").set("path")

    #dont scale x0.1 if ctrl clicked 
    if not kwargs['ctrlclick']:
        scale = hou.node(path).createNode('xform')
        scale.setPosition(pos-offset-offset-offset)
        scale.setColor(color)
        scale.setName("hou_scale",1)
        scale.setInput(0,conv)    
        scale.parm("scale").set("0.1")




if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()