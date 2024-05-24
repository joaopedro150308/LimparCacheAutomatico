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
    sleep(0.5)
    pyautogui.hotkey('left', 'enter')
    sleep(0.5)
    pyautogui.hotkey('right', 'right', 'enter')


def limpar_cache(pasta):
    abrir_cmd()
    pyautogui.typewrite(str(pasta))
    enviar_codigo()
    sleep(2)
    limpar_pasta()
    sleep(2)
    iginorar_janela()


def fechar_janela():
    pyautogui.hotkey('alt', 'f4')


# PROGRAMA PRINCIPAL

# Limpar %temp%
limpar_cache('%temp%')
sleep(10)
fechar_janela()
sleep(2)

# Limpar temp
limpar_cache('temp')
sleep(10)
fechar_janela()

sleep(2)

# Limpar prefetch
limpar_cache('prefetch')
sleep(10)
fechar_janela()
