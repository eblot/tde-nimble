#-----------------------------------------------------------------------------
# NimBLE controller
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

# syscfg.vals.BLE_LL_CFG_FEAT_LL_EXT_ADV:
#     BLE_LL_CFG_FEAT_LE_CSA2: 1
#     BLE_HW_WHITELIST_ENABLE: 0
#     BLE_LL_EXT_ADV_AUX_PTR_CNT: 5
# syscfg.vals.!BLE_HOST:
#     BLE_LL_VND_EVENT_ON_ASSERT: 1
# syscfg.restrictions:
#     - OS_CPUTIME_FREQ == 32768

build_component_from (
  src/ble_ll.c
  src/ble_ll_adv.c
  src/ble_ll_conn.c
  src/ble_ll_conn_hci.c
  src/ble_ll_conn_priv.h
  src/ble_ll_ctrl.c
  src/ble_ll_dtm.c
  src/ble_ll_dtm_priv.h
  src/ble_ll_hci.c
  src/ble_ll_hci_ev.c
  src/ble_ll_rand.c
  src/ble_ll_resolv.c
  src/ble_ll_scan.c
  src/ble_ll_sched.c
  src/ble_ll_supp_cmd.c
  src/ble_ll_sync.c
  src/ble_ll_trace.c
  src/ble_ll_utils.c
  src/ble_ll_whitelist.c
  src/ble_ll_xcvr.c
)
