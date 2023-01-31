################################################################################
# © Keysight Technologies 2016
#
# You have a royalty-free right to use, modify, reproduce and distribute
# the Sample Application Files (and/or any modified version) in any way
# you find useful, provided that you agree that Keysight Technologies has no
# warranty, obligations or liability for any Sample Application Files.
#
################################################################################

import pyvisa


# Change VISA_ADDRESS to a PXI address, e.g. 'PXI0::23-0.0::INSTR'
VISA_ADDRESS = 'Your instruments VISA address goes here!'

try:
    # Create a connection (session) to the PXI module
    resourceManager = pyvisa.ResourceManager()
    session = resourceManager.open_resource(VISA_ADDRESS)

    print('Manufacturer: %s\nModel: %s\nChassis: %d\nSlot: %d\nBus-Device.Function: %d-%d.%d\n' %
          (session.get_visa_attribute(pyvisa.constants.VI_ATTR_MANF_NAME),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_MODEL_NAME),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_PXI_CHASSIS),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_SLOT),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_PXI_BUS_NUM),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_PXI_DEV_NUM),
           session.get_visa_attribute(pyvisa.constants.VI_ATTR_PXI_FUNC_NUM)))

    # Close the connection to the instrument
    session.close()
    resourceManager.close()

except pyvisa.Error as ex:
    print('An error occurred: %s' % ex)

print('Done.')
