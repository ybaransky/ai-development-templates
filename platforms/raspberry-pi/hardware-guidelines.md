# Raspberry Pi Hardware Guidelines

- Verify Raspberry Pi model, GPIO numbering convention, voltage levels (3.3V GPIO), and attached devices.
- Never connect 5V signals directly to GPIO without suitable level shifting.
- Keep hardware access behind narrow adapters; provide fakes for host tests.
- Establish ownership of GPIO, I2C, SPI, serial ports, and cleanup on errors/shutdown.
- Handle permission, missing-device, and transient I/O failures explicitly.
- Avoid assuming all Pi models and Linux images have the same interfaces or GPIO libraries.
