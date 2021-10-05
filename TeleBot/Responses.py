from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("oi", "olá", "e ai",):
        return "Como posso lhe auxiliar?" 
    
    if user_message in ("Quem é você?", "O que você é?"):
        return "Eu sou um BOT!"
    
    if user_message in ("tempo", "horas?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)



    return "Eu não estou te entendendo."