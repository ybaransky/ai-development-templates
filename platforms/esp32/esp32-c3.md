# ESP32-C3 Addendum

- ESP32-C3 is a single-core RISC-V device; do not assume dual-core task placement.
- Check native USB Serial/JTAG behavior and board-specific boot/download wiring.
- Verify wake-capable GPIOs and strapping pins for the exact module/board.
- Validate pin assignments and sleep power against the selected board schematic.
