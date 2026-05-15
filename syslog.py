import os
import sys
import time
import subprocess
import textwrap
import argparse
import requests

# --- CONFIGURATION ---
SCRIPT_PATH = os.path.abspath(sys.argv[0])
LOG_PATH = os.path.expanduser("~/myscript.log")
SERVICE_NAME = "loggerpy"
USER_HOME = os.path.expanduser("~")
SYSTEMD_USER_DIR = os.path.join(USER_HOME, ".config/systemd/user")
SERVICE_FILE = os.path.join(SYSTEMD_USER_DIR, f"{SERVICE_NAME}.service")


def setup_systemd_service():
    """Create and enable a user-level systemd service."""
    os.makedirs(SYSTEMD_USER_DIR, exist_ok=True)

    service_content = textwrap.dedent(f"""
    [Unit]
    Description=My 60-Second Linux Logging Script
    After=network.target

    [Service]
    Type=simple
    ExecStart={SCRIPT_PATH}
    Restart=always
    RestartSec=10

    [Install]
    WantedBy=default.target
    """)

    with open(SERVICE_FILE, "w") as f:
        f.write(service_content)
        print(f"Service file written to: {SERVICE_FILE}")

    def run_systemctl_user(command):
        result = subprocess.run(
            ["systemctl", "--user"] + command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error running systemctl {' '.join(command)}:\n{result.stderr}")
        return result

    run_systemctl_user(["daemon-reload"])
    run_systemctl_user(["enable", SERVICE_NAME])
    run_systemctl_user(["start", SERVICE_NAME])
    print(f"{SERVICE_NAME} enabled and started as a user service!")


def log_metrics(server_url=None):
    """Capture system metrics and optionally send them to a server."""
    uptime = subprocess.getoutput("uptime -p")
    cpu_usage = subprocess.getoutput("top -bn1 | grep '%Cpu'")
    mem_usage = subprocess.getoutput("free -h | grep Mem")

    log_line = f"[{time.ctime()}] {uptime} | {cpu_usage.strip()} | {mem_usage.strip()}\n"

    # Write to local log file
    with open(LOG_PATH, "a") as f:
        f.write(log_line)
    print(log_line, end="")

    # Send to server if URL provided
    if server_url:
        try:
            response = requests.post(server_url, data={"log": log_line})
            if response.status_code != 200:
                print(f"Warning: Failed to send log to server ({response.status_code})")
        except requests.RequestException as e:
            print(f"Error sending log to server: {e}")


def main():
    parser = argparse.ArgumentParser(description="Linux System Logger")
    parser.add_argument("--server", type=str, help="Send logs to this server URL")
    parser.add_argument("--setup-service", action="store_true", help="Setup systemd service for automatic logging")
    args = parser.parse_args()

    if args.setup_service:
        setup_systemd_service()

    while True:
        log_metrics(server_url=args.server)
        time.sleep(5)


if __name__ == "__main__":
    main()
