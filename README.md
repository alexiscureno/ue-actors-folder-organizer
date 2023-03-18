![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Unreal Engine](https://img.shields.io/badge/unrealengine-%23313131.svg?style=for-the-badge&logo=unrealengine&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

# Unreal Engine Actor Organizer
# ue-actors-folder-organizer

# Requirements
* Unreal Engine 4.26
* Python 3.7

# Installation
* Clone this repository or download the ZIP archive and extract its contents.
* Copy and paste it into your Unreal Engine projects script file.

# Usage 
1. Open the level you want to organize in Unreal Editor.
2. Go to ```File > Execute Python Script```.
3. Locate your script in your project's files and run it.

# Notes

* The script currently supports organizing actors by class for StaticMeshActor, ReflectionCapture, and Blueprint classes. To add support for more classes, update the folder_names dictionary with the appropriate class name and list of actors.
* The script does not delete any actors or modify the level in any other way.
The script logs its progress to the Unreal Editor's Output Log, which can be 
* The script logs its progress to the Unreal Editor's Output Log, which can be accessed by opening the "Output Log" window from the Window menu.
