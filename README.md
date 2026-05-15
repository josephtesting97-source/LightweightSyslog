# LightweightSyslog

A lightweight tool that logs basic system metrics on Linux at regular intervals and optionally runs as a user-level systemd service.

Features
Logs system uptime, CPU usage, and memory usage.
Writes logs to ~/myscript.log.
Can run continuously as a user-level systemd service.
Self-contained and easy to set up.

## Requirements

Linux system with systemd



## Usage

Usage Examples

Run locally and log to file only:


```./syslog```


Send logs to a server while running:


```./syslog --server http://example.com/log-receiver```


Setup systemd service for automatic logging:


```./syslog --setup-service```

You can also combine server logging with systemd setup:

```./syslog --setup-service --server http://example.com/log-receiver```

## Features
The tool will:

Create a systemd user service at ~/.config/systemd/user/loggerpy.service.
Enable and start the service, which ensures the logger runs automatically on login.
Log system uptime, CPU, and memory usage to ~/myscript.log.


Logs in ~/myscript.log.

Running as a systemd Service

The script automatically sets up a user-level systemd service:

~/.config/systemd/user/loggerpy.service

## Security and Privacy

This script only collects system metrics and only transmits data externally when the user requests it to a user selected location.


## Contributing

Contributions are welcome! Please submit issues or pull requests for bug fixes and feature enhancements.


## License

This project is licensed under the MIT License.
