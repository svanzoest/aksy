import logging

import sysextools, disktools, programtools, multitools, songtools, multifxtools
import sampletools, systemtools, recordingtools, keygrouptools, zonetools
from aksy.devices.akai.sampler import Sampler
from aksy import model

log = logging.getLogger("aksy")

class Z48(Sampler):
    """Z48
    """
    def __init__(self, debug=1, usb_product_id=Sampler.Z48):
        Sampler.__init__(self, usb_product_id, debug)
        self.setup_tools()

        self.sysextools.enable_msg_notification(False)
        self.sysextools.enable_item_sync(False)
        
        self.setup_model()

    def setup_tools(self):
        self.disktools = disktools.Disktools(self)
        self.programtools = programtools.Programtools(self)
        self.keygrouptools = keygrouptools.Keygrouptools(self)
        self.zonetools = zonetools.Zonetools(self)
        self.sampletools = sampletools.Sampletools(self)
        self.songtools = songtools.Songtools(self)
        self.multitools = multitools.Multitools(self)
        self.multifxtools = multifxtools.Multifxtools(self)
        self.systemtools = systemtools.Systemtools(self)
        self.sysextools = sysextools.Sysextools(self)
        self.recordingtools = recordingtools.Recordingtools(self)

    def setup_model(self):
        model.register_handlers({model.Disk: self.disktools,
                        model.FileRef: self.disktools,
                        model.Program: self.programtools,
                        model.Sample: self.sampletools,
                        model.Multi: self.multitools})

        self.disks = model.RootDisk('disks', self.disktools.get_disklist())
        self.memory = model.Memory('memory')

class MPC4K(Z48):
    def __init__(self, debug=1):
        Z48.__init__(self, debug, usb_product_id=Sampler.MPC4K)
