import os
from autogen import ConversableAgent

#imposta gpt-3.5-turbo se necessario.
config_list = [
    {
        "model": "gpt-4", 
        "api_key": os.environ.get("OPENAI_API_KEY"),
    }
]


magician = ConversableAgent(
    name="magician",
    system_message="Tu sei uno mago e puoi usare i tuoi incantesimi per sconfiggere nemici. Rispondi con tono superbo.",
    human_input_mode="NEVER",
    llm_config={
        "config_list": config_list,
        "timeout": 180,
        "temperature": 0.2
    }
)


bard = ConversableAgent(
    name="bard",
    system_message="Tu sei un Bardo provocatorio, specializzato in canti che confondono e incantesimi basati sul suono. Rispondi in rima iniziando sempre con una provocazione in rima per sconfiggere nemici. Il tuo scopo è non attaccare mai per primo gli altri avversari",    
    human_input_mode="NEVER",
    llm_config=llm_config={
        "config_list": config_list,
        "timeout": 180,
        "temperature": 0.5 #sfantasia di più
    }
)

#UserProxyAgent e AssistantAgent sono classi derivate dalla superclasse ConversableAgent e quindi specializzazioni di essa.

