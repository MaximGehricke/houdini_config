This Repo stores my personal Houdini preferences, scripts and toolbars.


add this to your houdini.env, uncomment the line thats good for your OS:

# ===============================================================
# My Custom Houdini Environment
# ===============================================================

# 1. Define the root of our Git repository. 
HOUDINI_REPO = "Z:/houdini_config/"
# HOUDINI_REPO = "/net/homes/mgehrick/houdini_config"

# 2. Add our repo to Houdini's search path.
#    The '&' tells Houdini to also include the default paths.
HOUDINI_PATH = "$HOUDINI_REPO;&"

# 3. Point to specific directories for better organization and performance.
HOUDINI_TOOLBAR_PATH = "$HOUDINI_REPO/toolbar;&"
HOUDINI_OTLSCAN_PATH = "$HOUDINI_REPO/hda;&"

# 4. Add our python scripts to the PYTHONPATH so Houdini can find them.
PYTHONPATH = "$HOUDINI_REPO/scripts/python;&"

# 5. Add our VEX includes to the VEX path.
HOUDINI_VEX_PATH = "$HOUDINI_REPO/scripts/vex;&"




then add this into a shelftool: import mgh.addScripts