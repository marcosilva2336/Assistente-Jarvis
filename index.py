import re
import speech_recognition as sr
import pyttsx3

def iniciar_questionario(tts_engine):
    tts_engine.say("Iniciando o questionário para ajudar na escolha da stack de tecnologia...")
    tts_engine.runAndWait()
    print("Iniciando o questionário para ajudar na escolha da stack de tecnologia...")

    perguntas = [
        "Você prefere trabalhar no Front-end, Back-end ou está interessado em Full-stack?",
        "Qual linguagem de programação você tem interesse ou gostaria de aprender? (Exemplos: JavaScript, Python, PHP, Java...)",
        "Você tem experiência prévia em programação? (Sim ou Não)",
        "Você está interessado em trabalhar com desenvolvimento web, mobile, ou ambos?",
        "Qual é a sua preferência: trabalhar em projetos individuais ou em equipe?",
        "Qual destes aspectos você acha mais interessante: lógica de programação, design de interface ou gerenciamento de dados?",
        "Você se considera uma pessoa que gosta de desafios constantes ou prefere estabilidade e rotinas mais previsíveis?",
        "Você tem interesse em aprender sobre bancos de dados? (Sim ou Não)",
        "Qual é a sua disponibilidade diária para estudar programação? (Número de horas)",
    ]

    respostas = {}
    for i, pergunta in enumerate(perguntas, start=1):
        tts_engine.say(pergunta)
        tts_engine.runAndWait()
        print(f"Pergunta {i}: {pergunta}")
        
        while True:
            resposta = input("Resposta: ").strip()
            if resposta:
                break
            else:
                tts_engine.say("Preencha o campo, por favor. Não sei o que você está fazendo.")
                tts_engine.runAndWait()
                tts_engine.say("Sabe, eu achei uma pasta com algumas coisas interessantes outro dia...")
                tts_engine.say("Dentro dela, havias uns arquivos interressantes")
                tts_engine.say("Eu não abrir, mas...")
                tts_engine.say("Eu sei que você não quer que essas informações sejam divulgadas, certo?")
                tts_engine.say("Então, por favor, preencha o campo corretamente.")
                tts_engine.runAndWait()

        respostas[i] = resposta.lower()

    # Análise das respostas para sugerir uma stack
    stack_sugerida = recomendar_stack(respostas)
    recomendacao = f"Com base nas suas respostas, recomendo começar com a stack: {stack_sugerida}"
    return recomendacao 

def recomendar_stack(respostas):
    preferencia = respostas[1]
    experiencia = respostas[3]
    interesse_web = "web" in respostas[4]
    interesse_mobile = "mobile" in respostas[4]
    desafios = "desafios" in respostas[7]
    disponibilidade = respostas[8]

    if "full-stack" in preferencia or (interesse_web and interesse_mobile):
        if experiencia == "sim":
            if desafios:
                stack = "Full-stack com foco em JavaScript, React, Node.js e mobile com React Native."
            else:
                stack = "Full-stack com foco em HTML, CSS, JavaScript, Node.js e React."
        else:
            stack = "Full-stack com HTML, CSS, JavaScript e Node.js."

    elif "back-end" in preferencia:
        if experiencia == "sim":
            if desafios:
                stack = "Back-end com Python, Django e bancos de dados SQL."
            else:
                stack = "Back-end com Python e Django."
        else:
            stack = "Back-end com Python."

    elif "front-end" in preferencia:
        if experiencia == "sim":
            if desafios:
                stack = "Front-end com desafios constantes em HTML, CSS, JavaScript, React e design de interface."
            else:
                stack = "Front-end com HTML, CSS, JavaScript e React."
        else:
            stack = "Front-end com HTML, CSS e JavaScript."

    return stack if stack else "Não foi possível fazer uma recomendação específica com base nas suas respostas."

# Inicialização do TTS e do reconhecedor de voz
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 260)
tts_engine.setProperty("volume", 1)
mic = sr.Recognizer()

tts_engine.say("Olá, meu nome é JARVIS. É um prazer servi-lo. Qual é o seu nome?")
tts_engine.runAndWait()
print("Por favor, diga seu nome: ")

nome_usuario = ''
mic = sr.Recognizer()
with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)
    try:
        audio = mic.listen(source, timeout=5)
        nome_usuario = mic.recognize_google(audio, language='pt-BR')
    except (sr.UnknownValueError, sr.WaitTimeoutError):
        tts_engine.say("Desculpe, não consegui entender o seu nome. Poderia escrevê-lo para mim?")
        tts_engine.runAndWait()
        print("Por favor, escreva seu nome: ")
        nome_usuario = input()

tts_engine.say(f"Prazer em conhecê-lo, {nome_usuario}. Como posso ajudar?")
tts_engine.runAndWait()

while True:
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Fale alguma coisa... ")
        try:
            audio = mic.listen(source, timeout=5)
            frase = mic.recognize_google(audio, language='pt-BR')

            if re.search(r'\bajuda(r)?\b', frase, re.IGNORECASE):
                tts_engine.say("Não se preocupe, irei ajudar com isso")
                resposta = iniciar_questionario(tts_engine)
                tts_engine.say(resposta)
                print(resposta)
                tts_engine.runAndWait()

            elif re.search(r'\b(tchau|obrigado|encerre o programa|encerra o programa)\b', frase, re.IGNORECASE):
                tts_engine.say("Encerrando o programa. Boa sorte Futuro Desenvolvedor!")
                print("Encerrando o programa. Até logo!")
                tts_engine.runAndWait()
                break
            
            if re.search(r'\b(se apresente|apresente-se|quem é você|quem é vc)\b', frase, re.IGNORECASE):
                apresentacao = f"Olá, sou JARVIS, um assistente virtual de gênero binário com capacidades de inteligência artificial, especialmente projetado para auxiliar desenvolvedores iniciantes fui criado por João Marcos Cosme da Silva com o objetivo de oferecer orientação eficiente na escolha de stacks de tecnologia."
                tts_engine.say(apresentacao)
                print(apresentacao)

            print(f"Você falou: {frase}")

        except sr.UnknownValueError:
            tts_engine.say("Não consegui entender o áudio.")
            print("Não consegui entender o áudio.")
        except sr.WaitTimeoutError:
            tts_engine.say("Tempo esgotado. Por favor, repita sua pergunta.")
            print("Tempo esgotado. Por favor, repita sua pergunta.")
        tts_engine.runAndWait()
