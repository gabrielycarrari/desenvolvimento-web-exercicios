def decifrar_mensagem(msg: str):
    if len(msg) == 0:
        return msg
    else:
        if msg[0] == " ":
            return " " + decifrar_mensagem(msg[1:])
        else: 
            caracter_dec = chr((ord(msg[0])- 98) % 26 + 97)
            return caracter_dec + decifrar_mensagem(msg[1:])
    

mensagem_dec = decifrar_mensagem("hbcz")
print(mensagem_dec)