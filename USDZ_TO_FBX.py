import aspose
import aspose.threed
from pathlib import Path
from pathlib import PurePath


myFilePath =  Path(r"MyPathToFile")

# load the USDZ in an object of Scene 
scene = aspose.threed.Scene.from_file(str(myFilePath))

newFBXFileName = PurePath(myFilePath.parent, "namYourNewFile.fbx")

# save USDZ as a FBX 
scene.save(str(newFBXFileName), aspose.threed.FileFormat.FBX7700ASCII)

print("New File Created : " + newFBXFileName)