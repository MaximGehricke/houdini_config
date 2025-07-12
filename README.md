This Repo stores my personal Houdini preferences, scripts and toolbars.


Windows:
/setup/install.bat

Linux:
/setup/install.sh
chmod +x install.sh

this will append boilerplate.txt content to the houdini.env - you might need to help it find the installation


boot Houdini, then add this into a shelftool: 
import mgh.addScripts
mgh.addScripts.main()