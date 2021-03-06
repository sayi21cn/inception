from .submaker import Submaker
import os
class AdbKeysSubmaker(Submaker):
    PATH_DEVICE_ADBKEYS = "data/misc/adb/adb_keys"
    def make(self, workDir):
        adbKeys = self.getConfigValue("keys", [])
        outData = ""
        outPath = os.path.join(workDir, self.__class__.PATH_DEVICE_ADBKEYS)
        for key in adbKeys:
            outData += key + "\n"

        os.makedirs(os.path.dirname(outPath))
        with open(outPath, "w") as f:
            f.write(outData)

        self.setConfigValue("update.files.add.data/misc/adb", {
                "destination": "/data/misc/adb",
                "uid": "1000",
                "gid": "2000",
                "mode": "0640",
                "mode_dirs": "02750"
            })
