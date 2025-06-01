crypto_db={
        "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 9/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  

}

class crypto_budy:
    def __init__(self):
        self.prompts={
            "Which crypto is trending up?":'',
            "What’s the most sustainable coin?":'',
            "which one has low energy power?":'',

        }
    def response(self,message):
        message=message.lower().strip()
        
        for user_query in self.prompts:
            if "sustainable" in user_input:  
                recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])  
                return f"Invest in {recommend}!  It’s eco-friendly and has long-term potential!"
            if 'trending' in user_input:
                trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
                return f"These coins are trending up: {', '.join(trending)} "
            if 'low energy' in user_input:
                low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
                return f"These coins use low energy: {', '.join(low_energy)} "
            
chatbot=crypto_budy()
while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit"]:
        print("Chatbot: See you later!")
        break
    print("Chatbot:",chatbot.response(user_input)) 


