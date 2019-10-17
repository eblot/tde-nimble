#-----------------------------------------------------------------------------
# NimBLE nRF52 driver
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(BLE_PHY_SYSVIEW=0)
ADD_DEFINITIONS(BLE_PHY_CODED_RX_IFS_EXTRA_MARGIN=0)
ADD_DEFINITIONS(BLE_PHY_DBG_TIME_TXRXEN_READY_PIN=-1)
ADD_DEFINITIONS(BLE_PHY_DBG_TIME_ADDRESS_END_PIN=-1)
ADD_DEFINITIONS(BLE_PHY_DBG_TIME_WFR_PIN=-1)
ADD_DEFINITIONS(BLE_PHY_NRF52840_ERRATA_164=0)
ADD_DEFINITIONS(BLE_PHY_NRF52840_ERRATA_191=1)

build_component_from (
  src/ble_hw.c
  src/ble_phy.c
  src/ble_phy_trace.c
)
