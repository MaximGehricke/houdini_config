#SL
#opens parameters of the FS SL manager
#icon = NODEFLAGS_render
#hotkey = L

import hou

def main():
  node = hou.node('/obj/sl_sequence_manager1')
  desktop = hou.ui.curDesktop()
  if node is not None:
      desktop = hou.ui.curDesktop()
      fp = desktop.createFloatingPane(hou.paneTabType.Parm)
      fp.setCurrentNode(node)
  else:
      node = hou.node('/obj/sl_sequence_manager')
      desktop = hou.ui.curDesktop()
      if node is not None:
          desktop = hou.ui.curDesktop()
          fp = desktop.createFloatingPane(hou.paneTabType.Parm)
          fp.setCurrentNode(node)

