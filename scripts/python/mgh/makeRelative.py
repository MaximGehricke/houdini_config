#makeRelative
#replaces absolute paths with relative ones
#icon = SOP_name
# hotkey = alt + r


import hou

def main(**kwargs):
    nodes = hou.selectedNodes()
    parmsToAffect = ["target","cache_path","cachepath","campath","cmp_camera","source","shop_materialpath","shop_materialpath1","shop_materialpath2","shop_materialpath3","shop_materialpath4","objpath1","objpath2","objpath3","objpath4","objpath5","objpath6","objpath7","objpath8","objpath9","objpath10","soppath","sop_path","soppath","bindgeoinput1","bindgeoinput2","bindgeoinput3","bindgeoinput4"]

    for node in nodes:
        for parm in node.parms():
            for name in parmsToAffect:
                if parm.name()==name:
                    parm.set(node.relativePathTo(hou.node(parm.eval())))
                   


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
