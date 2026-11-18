# ESP32 Family Guidelines

- Identify the exact chip and board (original ESP32, S2, S3, C3, C6, etc.) before choosing pins or APIs.
- Verify strapping pins, input-only pins, ADC behavior, peripheral routing, USB/JTAG support, PSRAM, and wake sources per variant.
- Use task synchronization appropriate to FreeRTOS and multicore/single-core behavior; `volatile` alone is insufficient.
- Keep interrupt handlers minimal and compatible with IRAM restrictions where applicable.
- For low power, measure sleep current on the assembled board, not only chip datasheet figures.
- Do not assume all ESP32 variants share peripheral availability or Arduino APIs.
