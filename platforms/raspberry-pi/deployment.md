# Raspberry Pi Deployment Checklist

1. Document target Pi model, OS, Python version, and required system packages.
2. Install dependencies in a virtual environment; keep secrets outside version control.
3. Validate the standalone command first.
4. Configure and review the `systemd` unit; install/enable it only with permission.
5. Test `systemctl start`, `stop`, `restart`, and `status`; inspect `journalctl -u <service>`.
6. Confirm clean SIGTERM shutdown, hardware release, permissions, and startup after reboot.
7. Document rollback and recovery. Do not restart live services without explicit authorization.
