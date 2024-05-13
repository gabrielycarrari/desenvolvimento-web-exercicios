import datetime 
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

agora = datetime.datetime.now()

data_formatada = agora.strftime("%d/%m/%Y")

print(f"Data formatada: {data_formatada}")