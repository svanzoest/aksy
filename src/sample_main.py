
""" Python equivalent of akai section sample_main

Sample Main
"""

__author__ =  'Walco van Loon'
__version__=  '0.1'

import sysex

class SampleMain:
     def __init__(self, z48):
          self.z48 = z48
          self.commands = {}
          comm = sysex.Command('\x1C','\x01', 'get_no_items', (), (sysex.BYTE,))
          self.commands[('\x1C', '\x01')] = comm
          comm = sysex.Command('\x1C','\x02\x00', 'get_handles', (sysex.BYTE,), ())
          self.commands[('\x1C', '\x02\x00')] = comm
          comm = sysex.Command('\x1C','\x02\x01', 'get_names', (sysex.BYTE,), ())
          self.commands[('\x1C', '\x02\x01')] = comm
          comm = sysex.Command('\x1C','\x02\x02', 'get_handles_names', (sysex.BYTE,), ())
          self.commands[('\x1C', '\x02\x02')] = comm
          comm = sysex.Command('\x1C','\x02\x03', 'get_handles_modified', (sysex.BYTE,), ())
          self.commands[('\x1C', '\x02\x03')] = comm
          comm = sysex.Command('\x1C','\x03', 'set_current_by_handle', (sysex.DWORD,), ())
          self.commands[('\x1C', '\x03')] = comm
          comm = sysex.Command('\x1C','\x04', 'set_current_by_name', (sysex.STRING,), ())
          self.commands[('\x1C', '\x04')] = comm
          comm = sysex.Command('\x1C','\x05', 'get_current_handle', (), (sysex.DWORD,))
          self.commands[('\x1C', '\x05')] = comm
          comm = sysex.Command('\x1C','\x06', 'get_current_name', (), (sysex.STRING,))
          self.commands[('\x1C', '\x06')] = comm
          comm = sysex.Command('\x1C','\x07', 'get_name_by_handle', (sysex.DWORD,), (sysex.STRING,))
          self.commands[('\x1C', '\x07')] = comm
          comm = sysex.Command('\x1C','\x08', 'get_handle_by_name', (sysex.STRING,), (sysex.DWORD,))
          self.commands[('\x1C', '\x08')] = comm
          comm = sysex.Command('\x1C','\x09', 'delete_all', (), ())
          self.commands[('\x1C', '\x09')] = comm
          comm = sysex.Command('\x1C','\x0A', 'delete_current', (), ())
          self.commands[('\x1C', '\x0A')] = comm
          comm = sysex.Command('\x1C','\x0B', 'delete_by_handle', (sysex.DWORD,), ())
          self.commands[('\x1C', '\x0B')] = comm
          comm = sysex.Command('\x1C','\x0C', 'rename_current', (sysex.STRING,), ())
          self.commands[('\x1C', '\x0C')] = comm
          comm = sysex.Command('\x1C','\x0D', 'rename_by_handle', (sysex.DWORD, sysex.STRING), ())
          self.commands[('\x1C', '\x0D')] = comm
          comm = sysex.Command('\x1C','\x0E', 'set_tag_bit', (sysex.BYTE, sysex.BYTE), ())
          self.commands[('\x1C', '\x0E')] = comm
          comm = sysex.Command('\x1C','\x0F', 'get_tag_bitmap', (), ())
          self.commands[('\x1C', '\x0F')] = comm
          comm = sysex.Command('\x1C','\x10', 'get_curr_modified', (), (sysex.STRING,))
          self.commands[('\x1C', '\x10')] = comm
          comm = sysex.Command('\x1C','\x11 ', 'get_modified', (), (sysex.BYTE,))
          self.commands[('\x1C', '\x11 ')] = comm
          comm = sysex.Command('\x1C','\x18', 'delete_tagged', (sysex.BYTE ,), ())
          self.commands[('\x1C', '\x18')] = comm
          comm = sysex.Command('\x1C','\x40 ', 'play', (), ())
          self.commands[('\x1C', '\x40 ')] = comm
          comm = sysex.Command('\x1C','\x41 ', 'stop', (), ())
          self.commands[('\x1C', '\x41 ')] = comm
          comm = sysex.Command('\x1C','\x42', 'play_until', (sysex.QWORD,), ())
          self.commands[('\x1C', '\x42')] = comm
          comm = sysex.Command('\x1C','\x43 ', 'play_from', (sysex.BYTE, sysex.QWORD), ())
          self.commands[('\x1C', '\x43 ')] = comm

     def get_no_items(self):
          """Get number of items in memory

          Returns:
               sysex.BYTE
          """
          comm =  self.commands.get(('\x1C','\x01'))
          return self.z48.execute(comm, ())

     def get_handles(self, arg0):
          """Get Sample handles
          """
          comm =  self.commands.get(('\x1C','\x02\x00'))
          return self.z48.execute(comm, (arg0, ))

     def get_names(self, arg0):
          """Get sample names
          """
          comm =  self.commands.get(('\x1C','\x02\x01'))
          return self.z48.execute(comm, (arg0, ))

     def get_handles_names(self, arg0):
          """Get list of sample handles and names
          """
          comm =  self.commands.get(('\x1C','\x02\x02'))
          return self.z48.execute(comm, (arg0, ))

     def get_handles_modified(self, arg0):
          """Get a list of modified/tagged samples
          """
          comm =  self.commands.get(('\x1C','\x02\x03'))
          return self.z48.execute(comm, (arg0, ))

     def set_current_by_handle(self, arg0):
          """Select current item by handle
          """
          comm =  self.commands.get(('\x1C','\x03'))
          return self.z48.execute(comm, (arg0, ))

     def set_current_by_name(self, arg0):
          """Select current item by name
          """
          comm =  self.commands.get(('\x1C','\x04'))
          return self.z48.execute(comm, (arg0, ))

     def get_current_handle(self):
          """Get handle of current item

          Returns:
               sysex.DWORD
          """
          comm =  self.commands.get(('\x1C','\x05'))
          return self.z48.execute(comm, ())

     def get_current_name(self):
          """Get name of current item

          Returns:
               sysex.STRING
          """
          comm =  self.commands.get(('\x1C','\x06'))
          return self.z48.execute(comm, ())

     def get_name_by_handle(self, arg0):
          """Get item name from handle

          Returns:
               sysex.STRING
          """
          comm =  self.commands.get(('\x1C','\x07'))
          return self.z48.execute(comm, (arg0, ))

     def get_handle_by_name(self, arg0):
          """Get item handle from name

          Returns:
               sysex.DWORD
          """
          comm =  self.commands.get(('\x1C','\x08'))
          return self.z48.execute(comm, (arg0, ))

     def delete_all(self):
          """Delete ALL items from memory
          """
          comm =  self.commands.get(('\x1C','\x09'))
          return self.z48.execute(comm, ())

     def delete_current(self):
          """Delete current item from memory
          """
          comm =  self.commands.get(('\x1C','\x0A'))
          return self.z48.execute(comm, ())

     def delete_by_handle(self, arg0):
          """Delete item represented by handle <Data1>
          """
          comm =  self.commands.get(('\x1C','\x0B'))
          return self.z48.execute(comm, (arg0, ))

     def rename_current(self, arg0):
          """Rename current item
          """
          comm =  self.commands.get(('\x1C','\x0C'))
          return self.z48.execute(comm, (arg0, ))

     def rename_by_handle(self, arg0, arg1):
          """Rename item represented by handle <Data1>
          """
          comm =  self.commands.get(('\x1C','\x0D'))
          return self.z48.execute(comm, (arg0, arg1, ))

     def set_tag_bit(self, arg0, arg1):
          """Set Tag Bit <Data1> = bit to set, <Data2> = (0=OFF, 1=ON) BYTE(0, 1) <Data3> = (0=CURRENT, 1=ALL)
          """
          comm =  self.commands.get(('\x1C','\x0E'))
          return self.z48.execute(comm, (arg0, arg1, ))

     def get_tag_bitmap(self):
          """Get Tag Bitmap
          """
          comm =  self.commands.get(('\x1C','\x0F'))
          return self.z48.execute(comm, ())

     def get_curr_modified(self):
          """Get name of current item with modified/tagged info

          Returns:
               sysex.STRING
          """
          comm =  self.commands.get(('\x1C','\x10'))
          return self.z48.execute(comm, ())

     def get_modified(self):
          """Get modified state of current item.

          Returns:
               sysex.BYTE
          """
          comm =  self.commands.get(('\x1C','\x11 '))
          return self.z48.execute(comm, ())

     def delete_tagged(self, arg0):
          """Delete tagged items <Data1> = tag bit
          """
          comm =  self.commands.get(('\x1C','\x18'))
          return self.z48.execute(comm, (arg0, ))

     def play(self):
          """Start auditioning the current sample <Data1> = velocity <Data2> =(NO LOOPING, 1=LOOPING) BYTE BYTE
          """
          comm =  self.commands.get(('\x1C','\x40 '))
          return self.z48.execute(comm, ())

     def stop(self):
          """Stop playback of the current sample
          """
          comm =  self.commands.get(('\x1C','\x41 '))
          return self.z48.execute(comm, ())

     def play_until(self, arg0):
          """Play To <Data1> = velocity, <Data2> = sample position BYTE
          """
          comm =  self.commands.get(('\x1C','\x42'))
          return self.z48.execute(comm, (arg0, ))

     def play_from(self, arg0, arg1):
          """Play From <Data1> = velocity, <Data2> = sample position
          """
          comm =  self.commands.get(('\x1C','\x43 '))
          return self.z48.execute(comm, (arg0, arg1, ))

