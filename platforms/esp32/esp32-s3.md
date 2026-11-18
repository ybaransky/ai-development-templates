# ESP32-S3 Addendum

- Verify board-specific USB-OTG vs USB Serial/JTAG configuration and connector wiring.
- Check PSRAM availability/configuration and whether buffers need internal DMA-capable memory.
- Verify strapping pins, GPIO restrictions, and wake sources on the exact module.
- Do not assume S3 behavior applies to C3/C6.
