import pyautogui
from time import sleep

def enviar_codigo():
    pyautogui.hotkey('enter')


def limpar_pasta():
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('delete')

def abrir_cmd():
    pyautogui.hotkey('win', 'r')


def iginorar_janela():
    pyautogui.moveTo(673,581, duration=2)
    pyautogui.click()
    pyautogui.moveTo(1033,632, duration=2)
    pyautogui.click()


def iginorar_janela_adm():
    pyautogui.moveTo(888,518, duration=2)
    pyautogui.click()


def limpar_cache(pasta):
    abrir_cmd()
    pyautogui.typewrite(str(pasta))
    enviar_codigo()
    sleep(2)
    limpar_pasta()
    sleep(2)
    iginorar_janela()
    iginorar_janela_adm()
    iginorar_janela()


# PROGRAMA PRINCIPAL

# Limpar %temp%
limpar_cache('%temp%')
sleep(10)

# Limpar temp
limpar_cache('temp')
sleep(10)

# Limpar prefetch
limpar_cache('prefetch')
