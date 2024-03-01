import time
import json
import subprocess
import urllib.request
import webbrowser


def show_menssage(mensagem):
    # Usando o zenity para exibir uma caixa de diálogo de mensagem
    comando = ['zenity', '--info', '--text', mensagem]
    subprocess.Popen(comando)


def check_new_version(current_version):
    code_url = "https://raw.githubusercontent.com/JuanBindez/Chernobyl/main/code.json"

    try:
        with urllib.request.urlopen(code_url) as response:
            version_info = response.read().decode().strip()

        code_data = json.loads(version_info)
        latest_version = code_data.get("code", "")
        mensagem = code_data.get("message", "")

        
        while True:
            time.sleep(4)
            if latest_version == current_version:
                time.sleep(4)
            elif latest_version != current_version:
                show_menssage(mensagem)
            else:
                break

    except urllib.error.URLError:
        pass


if __name__ == "__main__":
    check_new_version("0")
