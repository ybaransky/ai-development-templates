# ESP32-C6 Addendum

- Verify the chosen Arduino core/platform version supports the required C6 peripherals and wireless features.
- Do not assume ESP32-S3 USB or GPIO behavior applies to C6.
- Check board-specific native USB Serial/JTAG, bootstrapping, and sleep/wake restrictions.
- Confirm whether Wi-Fi, BLE, and 802.15.4 coexistence matters for the application.
