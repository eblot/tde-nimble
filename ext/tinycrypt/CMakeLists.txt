#-----------------------------------------------------------------------------
# TinyCrypt
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

build_component_from (
  src/aes_decrypt.c
  src/aes_encrypt.c
  src/cbc_mode.c
  src/ccm_mode.c
  src/cmac_mode.c
  src/ctr_mode.c
  src/ctr_prng.c
  src/ecc.c
  src/ecc_dh.c
  src/ecc_dsa.c
  src/ecc_platform_specific.c
  src/hmac.c
  src/hmac_prng.c
  src/sha256.c
  src/utils.c
)
