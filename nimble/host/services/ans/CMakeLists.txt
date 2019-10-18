#-----------------------------------------------------------------------------
# NimBLE Alert Notification Service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS (-DBLE_SVC_ANS_NEW_ALERT_CAT=0)
ADD_DEFINITIONS (-DBLE_SVC_ANS_UNR_ALERT_CAT=0)
ADD_DEFINITIONS (-DBLE_SVC_ANS_SYSINIT_STAGE=303)

build_component_from (
  src/ble_svc_ans.c
)
