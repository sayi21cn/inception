from .maker import Maker
from inception.generators.bootimg import BootImgGenerator
import os
class ImageMaker(Maker):

    def __init__(self, config, key, imageName):
        super(ImageMaker, self).__init__(config, key)
        self.imageName = imageName

    def make(self, workDir, outDir):
        gen = BootImgGenerator(self.getCommonConfigValue("tools.mkbootimg.bin"))
        gen.setWorkDir(workDir)
        gen.setOutDir(outDir)

        bootConfig = self.getMakeConfigValue("img")
        ramdisk = bootConfig["ramdisk_dir"] if "ramdisk_dir" in bootConfig else None
        if ramdisk is None:
            ramdisk = self.getMakeConfigValue("img.ramdisk")

        kernel = self.getMakeConfigValue("img.kernel")

        second = bootConfig["second"] if "second" in bootConfig else None
        cmdline = bootConfig["cmdline"] if "cmdline" in bootConfig else None
        base = bootConfig["base"] if "base" in bootConfig else None
        pagesize = bootConfig["pagesize"] if "pagesize" in bootConfig else None
        ramdisk_offset = bootConfig["ramdisk_offset"] if "ramdisk_offset" in bootConfig\
            else None
        ramdiskaddr = bootConfig["ramdiskaddr"] if "ramdiskaddr" in bootConfig else None
        devicetree = bootConfig["dt"] if "dt" in bootConfig else None
        signature = bootConfig["signature"] if "signature" in bootConfig else None

        gen.setKernel(kernel)
        gen.setRamdisk(ramdisk)
        gen.setKernelCmdLine(cmdline)
        gen.setSecondBootLoader(second)
        gen.setPageSize(pagesize)
        gen.setBaseAddr(base)
        gen.setRamdiskOffset(ramdisk_offset)
        gen.setDeviceTree(devicetree)
        gen.setSignature(signature)
        gen.setRamdiskAddr(ramdiskaddr)

        gen.generate(os.path.join(outDir, self.imageName + ".img"))