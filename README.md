# raspberry-pi-webserver
Flask Webserver running on Raspberry Pi 3B as my central hub.  
See https://github.com/ArcaneBow7258/pico-w-led-api for what I use this webserver for.   
My RPi is simply plugged in so IP is fairly static and thus not really a consideration of mine.  
Development environment is VS Code Remote SSH.

# Network Set-up
_References_  
https://stackoverflow.com/questions/61443935/ssh-service-running-on-multiple-ports-with-custom-rules-in-linux  
- Install Gunicorn and Ngnix
- NOTE: Tutorial says set Gunicorn as a service, I did not
- Using another device on same network, log into routerlogin.net
- _OPTIONAL:_ Port forward port you wish to ssh into your Pi. Names below are optional
  - `cp ssh/sshd_config_custom /etc/ssh/sshd_config_custom`
  - `cp ssh/ssh.service /lib/systemd/system/sshd-custom.service`
```
systemctl enable sshd-custom.service   
systemctl start sshd-custom.service
```
- _OPTION:_ To open to internet (danger!!!!), Port forward HTTP/HTTPS port (I used HTTP, not tested on HTTPS), for example 80.
  
Ngnix Set up for safety (HTTP)
-
_References_  
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04  
https://flask.palletsprojects.com/en/3.0.x/deploying/nginx/  
- `sudo vi sudo nano /etc/nginx/sites-available/myproject`
```
# Per the Flask link, basically route port 80 (HTTP) to 8000 internally (Externally, you're accessing port 80)
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
}
```
- `sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled`
- `sudo nginx -t` to test if it breaks and if it does go google it
- `sudo systemctl restart nginx`
- `sudo ufw allow 'Nginx Full'`


# Environment
- `pip install venv`
- `venv` and create your environment
- `source bin/activate`
- `pip install -r requirements.txt` but really all you need is Flask

# Other Files
- `ip.sh` is for finding ip if you exposed yourself to the public
- `run.sh` is just to run Gunicorn on the Webserver
