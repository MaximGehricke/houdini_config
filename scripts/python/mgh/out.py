#OUT
#creates an output node, sets name, shape, color. toggles to null if it already exists
#icon = SOP_output

import hou

def nullForOut():
    for node in hou.selectedNodes():
        outs = node.outputLabels()
        parent_network = node.parent()
        node_pos = node.position()
        num_outputs = len(node.outputConnectors())

        # This 'with' block groups all actions into a single undo step
        with hou.undos.group("Create Output Nulls"):
            
            for i in range(num_outputs):
                null_node = parent_network.createNode("null")

                # Set its input to the i-th output of our source node
                null_node.setInput(0, node, i)
                name = f"OUT_{i+1}"
                if "utpu" not in outs[i]:
                    name = f"OUT_{outs[i]}".replace(" ","_")
                print(name)
                null_node.setName(name, unique_name=True)
                null_node.setColor(hou.Color((0.8, 0.4, 0.2))) # A nice orange color

                # Place it below the source node, staggering horizontally for multiple outputs
                null_node.setPosition(node_pos + hou.Vector2(i * 2, -1.5))


def createOut():
    network = hou.ui.curDesktop().paneTabUnderCursor()
    networkpath = network.pwd().path()
    pos = network.cursorPosition()
    name = "OUT_"+networkpath.split("/")[-1]

    #find lowest selected node:
    selectedNodes = hou.selectedNodes()
    lastNode = "noNodeSelected29834787320~###"

    lowestPos = 10000000000;
    for node in selectedNodes:
        #check if OUT already exists, if so toggle to Null
        if "OUT_" in node.name():
            if node.type().name()=="output":
                node.changeNodeType("null")
                exit()
            if node.type().name()=="null":
                node.changeNodeType("output")
                exit()
                
        position = node.position()[1]
        if position<lowestPos:
            lowestPos = position
            lastNode = node
            

    out = hou.node(networkpath).createNode('output')
    out.setPosition(pos)
    out.setUserData("nodeshape", "null")
    out.setColor(hou.Color((0.29,0.565,0.886)))
    out.setName(name,1)
    out.setSelected(1,1)

    if lastNode!="noNodeSelected29834787320~###":
        out.setInput(0,lastNode)
        out.moveToGoodPosition()


def main(**kwargs):
    #creates output node "OUT_name" or replaces output node with a Null
    if kwargs['ctrlclick']:
        nullForOut()
        return
    if kwargs['shiftclick']:
        nullForOut()
        return
    else:
        createOut()


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()