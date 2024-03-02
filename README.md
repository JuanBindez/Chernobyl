# Chernobyl


## auto run:

    crontab -e

## add line:

    @reboot python3 /caminho/para/seu/programa.py

## Create file name_service.service:

    [Unit]
    Description=Descrição do seu serviço
    
    [Service]
    ExecStart=/usr/bin/python3 /caminho/para/seu/programa.py
    Restart=always
    
    [Install]
    WantedBy=multi-user.target

## move file:

    sudo mv name_service.service /etc/systemd/system/

## command:
    sudo systemctl daemon-reload

## command 2:

    sudo systemctl enable name_service

## all commands:

    sudo systemctl start name_service
    sudo systemctl stop name_service
    sudo systemctl restart name_service




