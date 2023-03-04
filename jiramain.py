"""Este código é um chatbot que responde à entrada do usuário. 
Ele usa o módulo "long_responses" importado para armazenar respostas mais longas e o módulo "re" para dividir a entrada do usuário em palavras individuais. 
A função "message_probability" calcula a porcentagem de palavras em uma mensagem do usuário que correspondem às palavras reconhecidas, e a função "check_all_messages" verifica todas as mensagens predefinidas e retorna aquela com a maior probabilidade. 
A função "get_response" é usada para obter uma resposta do chatbot e chama ambas as funções. Finalmente, há um loop while que permite aos usuários interagir com o chatbot."""


import re
import long_responses as long
import os
import pwd

username = pwd.getpwuid(os.getuid()).pw_name
print("Ola", username, "!", "Seja bem vindo ao JiraBot!")

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Conta quantas palavras estão presentes em cada mensagem predefinida
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calcula a porcentagem de palavras reconhecidas em uma mensagem do usuário
    percentage = float(message_certainty) / float(len(recognised_words))

    # Verifica se as palavras necessárias estão na string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Deve ter as palavras necessárias ou ser uma única resposta
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifica a criação da resposta / adiciona ao dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #respostas -------------------------------------------------------------------------------------------------------
    response('Ola! Bem Vindo ao JiraBot', ['ola', 'Oi', 'Oii', 'oi', 'hey', 'Oie'], single_response=True)
    response('Ate logo!', ['tchau', 'ate'], single_response=True)
    response('Estou bem e voce?', ['como', 'tudo', 'voce', 'esta'], required_words=['tudo', 'bem'])
    response('Por nada!', ['obrigado', 'muito obrigado'], single_response=True)
    response('Otimo! Vamos la! O que posso ajudar?', ['estou', 'bem'], required_words=['estou'])

    # Respostas mais longas
    response(long.R_INTROJIRA1, ['jira', 'que', 'e'], required_words=['que', 'e', 'jira'])
    response(long.R_INTROJIRA2, ['configurar', 'jira', 'Jira', 'como'], required_words=['configurar'])
    response(long.R_INTROJIRA3, ['novo', 'projeto', 'jira'], required_words=['novo', 'projeto'])
    response(long.R_INTROJIRA4, ['quais', 'principais', 'funcionalidades'], required_words=['principais', 'funcionalidades'])
    response(long.R_INTROJIRA5, ['como', 'gerenciar', 'tarefas'], required_words=['gerenciar', 'tarefas'])
    response(long.R_INTROJIRA6, ['recursos', 'relatorio', 'jira'], required_words=['recursos', 'relatorio'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Usado para obter a resposta
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testando o sistema de resposta
while True:
    print('JiraBot: ' + get_response(input('You: ')))