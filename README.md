

# Pterodactyl Auto Start


## Description

This bash script auto start (at boot for example) the servers in Pterodactyl that have `alwaysStart` in their description.
Modified by NoxShadow YT to migrate to Replit, All credit goes to https://github.com/Alteiria/ for her amazing pterodactylAutoStart.

## Requirements

* You need to set two Secrets in your Replit.:
  * `baseURL` : The URL of your Pterodactyl panel + `/api`. Example: `https://your.pterodactyl.panel/api`
  * `apiToken` : The token generated from the Account API page.
* And having jq >1.6 installed: https://github.com/stedolan/jq/releases

## Installation
1. Generate an account API token: https://your.pterodactyl.panel/account/api
2. Download the git repository to the `/opt/pterodactylAutoStart` directory using:
````
sudo git clone https://github.com/Alteiria/pterodactylAutoStart.git /opt/pterodactylAutoStart
````
3. Install JQ from [the release page](https://github.com/stedolan/jq/releases):
````
sudo wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -O /usr/bin/jq
sudo chmod +x /usr/bin/jq
````
4. Move the service file from the installation directory to the systemd service files:
````
sudo mv /opt/pterodactylAutoStart/pterodactylAutoStart.service /etc/systemd/system/pterodactylAutoStart.service
````
5. Edit the service file and modify the two environment variables `baseURL` and `apiToken`:

````
sudo nano /etc/systemd/system/pterodactylAutoStart.service
````

**Note**: Make sure to follow the [Requirements](requirements.txt) section for the two environment variables!

6. Enable the service file to make the script starting at boot:
````
sudo systemctl enable pterodactylAutoStart
````
7. On your Pterodactyl panel, edit the description of every server that you wish to auto start by simply adding `alwaysStart` in their description. **Watchout for the capitalized in the second `s`**!

    Screenshot of one of Alteiria server that auto start:
![](https://i.imgur.com/7Cg4J9k.png)

## How to test if the script works as intended.

1. Manually shutdown a server that you configured to auto start.
2. Run the systemd start command to start the script:
````
~~sudo systemctl start pterodactylAutoStart~~ Click the run button on Replit.
````
3. Check if your server start after that, it will take up to 80 seconds because there is a delay of 60
seconds to abid with Replit's TOS to controll data traffic.
([more details available here](https://github.com/NoxShadow-YT/pterodactylAutoStart/issues/2)).
4. If your server didn't start after that period of 80 seconds check the logs using journalctl:
````
journalctl -u pterodactylAutoStart
````
By the way run journalctl in Replit Shell at least once so it will prompt you to install journalctl 
to replit.nix.
