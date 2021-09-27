import time

import QCC_Update

ps_key_18_value = QCC_Update.read_ps_key("18")

time.sleep(5)

QCC_Update.read_mib()

time.sleep(5)

QCC_Update.flash_device_nvs_app()

time.sleep(5)

QCC_Update.write_ps_key("18", ps_key_18_value)

time.sleep(5)

QCC_Update.write_mib()

input("Press to close")
