# Verify canonical documentation copies in project templates
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ('common/docs/feature-development.md', 'templates/arduino-platformio/docs/feature-development.md'),
    ('common/docs/refactoring.md', 'templates/arduino-platformio/docs/refactoring.md'),
    ('common/docs/architecture-review.md', 'templates/arduino-platformio/docs/architecture-review.md'),
    ('common/docs/git-workflow.md', 'templates/arduino-platformio/docs/git-workflow.md'),
    ('common/prompts/add-feature.md', 'templates/arduino-platformio/prompts/add-feature.md'),
    ('common/prompts/refactor-code.md', 'templates/arduino-platformio/prompts/refactor-code.md'),
    ('common/prompts/review-architecture.md', 'templates/arduino-platformio/prompts/review-architecture.md'),
    ('common/docs/feature-development.md', 'templates/raspberry-pi-python/docs/feature-development.md'),
    ('common/docs/refactoring.md', 'templates/raspberry-pi-python/docs/refactoring.md'),
    ('common/docs/architecture-review.md', 'templates/raspberry-pi-python/docs/architecture-review.md'),
    ('common/docs/git-workflow.md', 'templates/raspberry-pi-python/docs/git-workflow.md'),
    ('common/prompts/add-feature.md', 'templates/raspberry-pi-python/prompts/add-feature.md'),
    ('common/prompts/refactor-code.md', 'templates/raspberry-pi-python/prompts/refactor-code.md'),
    ('common/prompts/review-architecture.md', 'templates/raspberry-pi-python/prompts/review-architecture.md'),
    ('languages/cpp/coding-standards.md', 'templates/arduino-platformio/docs/coding-standards.md'),
    ('platforms/arduino/framework.md', 'templates/arduino-platformio/docs/arduino-framework.md'),
    ('platforms/platformio/build-and-test.md', 'templates/arduino-platformio/docs/platformio.md'),
    ('languages/python/coding-standards.md', 'templates/raspberry-pi-python/docs/coding-standards.md'),
    ('languages/python/testing.md', 'templates/raspberry-pi-python/docs/testing.md'),
    ('platforms/raspberry-pi/hardware-guidelines.md', 'templates/raspberry-pi-python/docs/platforms/raspberry-pi.md'),
    ('platforms/raspberry-pi/linux-services.md', 'templates/raspberry-pi-python/docs/linux-services.md'),
    ('platforms/raspberry-pi/deployment.md', 'templates/raspberry-pi-python/docs/deployment.md'),
 ]
failures = []
for source, destination in PAIRS:
    if (ROOT / source).read_bytes() != (ROOT / destination).read_bytes():
        failures.append(f"Mismatch: {source} != {destination}")
if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"OK: {len(PAIRS)} copied documents match canonical sources")
