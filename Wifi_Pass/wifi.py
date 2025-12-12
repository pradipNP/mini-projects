import subprocess

# Get all profiles
data = subprocess.check_output("netsh wlan show profiles").decode(errors="ignore")

profiles = []
for line in data.split("\n"):
    if "All User Profile" in line:
        profiles.append(line.split(":")[1].strip())

# Show passwords for each valid profile
for profile in profiles:
    try:
        result = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear').decode(errors="ignore")

        for line in result.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                print(f"Profile: {profile}, Password: {password}")

    except subprocess.CalledProcessError:
        pass