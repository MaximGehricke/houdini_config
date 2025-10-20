#mat
#quickly create a grey arnold shader
 
import hou

def isArnoldInstalled():
    if hou.nodeType("Driver/arnold") is not None:
        return True
    return False
        

def findLowestNode(nodesToRunOver = ""):
    #find lowest of the given or selected nodes
    if not nodesToRunOver:
        nodesToRunOver = hou.selectedNodes()
    lastNode = None
    
    lowestPos = 10000000000;
    for node in nodesToRunOver:
        position = node.position()[1]
        if position<lowestPos:
            lowestPos = position
            lastNode = node

    return lastNode,position
    
    
def createArnoldShdr(ctx, var = "grey"):
    #matnet and material builder
    matnet = ctx.createNode("matnet","matnet")
    vop = matnet.createNode("arnold_materialbuilder",var)
    #create material assign
    mat = ctx.createNode("material")
    mat.parm("shop_materialpath1").set("../"+matnet.name()+"/"+vop.name())
    #standardSurface SHR
    std = vop.createNode("arnold::standard_surface", var)
    std.setPosition((std.position()[0]-3, std.position()[1]))
    #connect material output
    matOut = hou.node(str(vop.path())+"/OUT_material")
    matOut.setInput(0, std)
    return mat, matnet, vop, std
    
    
def main(**kwargs):
    ctx = next(tab for tab in hou.ui.currentPaneTabs() if isinstance(tab, hou.NetworkEditor) and tab.isCurrentTab()).pwd()
    orgNode,orgPos = findLowestNode()
    
    if isArnoldInstalled():
        
        mat, matnet, vop, std = createArnoldShdr(ctx, "grey")
        for parm in ["r","g","b"]:
            std.parm("base_color"+parm).set(0.18)
  
        if orgNode:
            mat.setInput(0,orgNode)
            mat.setPosition(orgNode.position() + hou.Vector2(0, -2))
            matnet.setPosition((mat.position()[0]-3, mat.position()[1]))
            mat.setSelected(1)
            mat.setDisplayFlag(1)
            mat.setRenderFlag(1)
        



    
    
        

        
main()
