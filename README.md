# JARVIS - Assistente de Orientação para Desenvolvimento de Software  

O **JARVIS** é um assistente virtual interativo desenvolvido em **Python** com suporte a reconhecimento de voz e síntese de fala. Ele foi criado para ajudar desenvolvedores iniciantes a escolherem a stack de tecnologia mais adequada ao seu perfil e preferências, por meio de um questionário dinâmico.

## 🚀 Funcionalidades  

- **Reconhecimento de Voz:**  
  Utiliza a biblioteca `speech_recognition` para captar e interpretar comandos de voz do usuário.  

- **Síntese de Fala:**  
  Com `pyttsx3`, o JARVIS é capaz de responder em áudio, criando uma experiência interativa.  

- **Questionário Personalizado:**  
  Um conjunto de perguntas ajuda a identificar preferências e objetivos do usuário, sugerindo a stack de tecnologia ideal com base nas respostas.  

- **Comandos Inteligentes:**  
  Responde a comandos como "se apresente", "ajuda", e "encerrar programa".  

- **Recomendações de Stack:**  
  Sugere stacks como Front-end, Back-end ou Full-stack com base nas respostas do usuário.  

## 🛠️ Tecnologias Utilizadas  

- **Python:** Linguagem base para todo o desenvolvimento.  
- **SpeechRecognition:** Para capturar e processar a entrada de voz.  
- **pyttsx3:** Para síntese de voz.  
- **re:** Para processamento e correspondência de padrões em texto.  

## 📋 Pré-requisitos  

- **Python 3.x:** Instale a versão mais recente do Python em sua máquina.  
- **Bibliotecas Necessárias:**  
  Instale as dependências executando:  
  ```bash
  pip install speechrecognition pyttsx3
