# LightweightSyslog

A lightweight Python script that logs basic system metrics on Linux at regular intervals and optionally runs as a user-level systemd service.

Features
Logs system uptime, CPU usage, and memory usage.
Writes logs to ~/myscript.log.
Can run continuously as a user-level systemd service.
Self-contained and easy to set up.
Requirements
Python 3.x
Linux system with systemd

--

## Usage

Run the script:

./ syslogger

## Features
The script will:

Create a systemd user service at ~/.config/systemd/user/loggerpy.service.
Enable and start the service, which ensures the logger runs automatically on login.
Log system uptime, CPU, and memory usage to ~/myscript.log.
Running Manually
python3 logger.py

Logs will appear in the console and in ~/myscript.log.

Running as a systemd Service

The script automatically sets up a user-level systemd service:

~/.config/systemd/user/loggerpy.service

Security and Privacy

This script only collects system metrics and does not transmit data externally.

--

## Contributing

Contributions are welcome! Please submit issues or pull requests for bug fixes and feature enhancements.

--

## License

This project is licensed under the MIT License.
