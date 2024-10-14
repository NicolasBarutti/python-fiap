import banco

# Simulação da função altera
mensagem_para_alterar = {
    "id": 1,  # Assumindo que existe uma mensagem com ID 1 no banco
    "assunto": "Novo Assunto Alterado",
    "destinatario": "cliente1@empresa.com",
    "remetente": "suporte@empresa.com",
    "conteudo": "Conteúdo da mensagem alterado com sucesso."
}

# Alterando a mensagem com id 1
banco.altera(mensagem_para_alterar)
print(f"Mensagem com ID {mensagem_para_alterar['id']} foi alterada com sucesso!")

# Simulação da função recupera (recuperar uma mensagem específica por ID)
id_para_recuperar = 1
mensagem_recuperada = banco.recupera(id_para_recuperar)
if mensagem_recuperada:
    print(f"Mensagem recuperada (ID: {id_para_recuperar}): {mensagem_recuperada}")
else:
    print(f"Mensagem com ID {id_para_recuperar} não encontrada.")

# Simulação da função recupera_assunto (busca por fragmento de assunto)
assunto_fragmento = "Promoção"
mensagens_assunto = banco.recupera_assunto(assunto_fragmento)
print(f"Mensagens com assunto contendo '{assunto_fragmento}':")
for mensagem in mensagens_assunto:
    print(mensagem)

# Simulação da função recupera_destinatario (busca por destinatário)
destinatario_para_busca = "cliente2@empresa.com"
mensagens_destinatario = banco.recupera_destinatario(destinatario_para_busca)
print(f"Mensagens enviadas para o destinatário {destinatario_para_busca}:")
for mensagem in mensagens_destinatario:
    print(mensagem)

# Simulação da função apaga (excluir uma mensagem por ID)
id_para_apagar = 2  # Assumindo que existe uma mensagem com ID 2 no banco
banco.apaga(id_para_apagar)
print(f"Mensagem com ID {id_para_apagar} foi excluída com sucesso.")
