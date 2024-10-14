import banco

mensagens = [
    {"assunto": "Atualização de contrato", "destinatario": "cliente1@empresa.com", "remetente": "suporte@empresa.com", "conteudo": "Contrato atualizado com sucesso."},
    {"assunto": "Promoção exclusiva", "destinatario": "cliente2@empresa.com", "remetente": "marketing@empresa.com", "conteudo": "Confira nossa promoção especial para você!"},
    {"assunto": "Boletim informativo", "destinatario": "cliente3@empresa.com", "remetente": "news@empresa.com", "conteudo": "Aqui estão as novidades deste mês."},
    {"assunto": "Confirmação de agendamento", "destinatario": "cliente4@empresa.com", "remetente": "agendamento@empresa.com", "conteudo": "Seu agendamento foi confirmado."},
    {"assunto": "Atualização do sistema", "destinatario": "cliente5@empresa.com", "remetente": "tecnologia@empresa.com", "conteudo": "A atualização do sistema foi concluída."},
    {"assunto": "Aviso de manutenção", "destinatario": "cliente6@empresa.com", "remetente": "infra@empresa.com", "conteudo": "Haverá manutenção no próximo final de semana."},
    {"assunto": "Boas-vindas", "destinatario": "cliente7@empresa.com", "remetente": "suporte@empresa.com", "conteudo": "Bem-vindo(a) ao nosso sistema!"},
    {"assunto": "Pedido concluído", "destinatario": "cliente8@empresa.com", "remetente": "vendas@empresa.com", "conteudo": "Seu pedido foi concluído com sucesso."},
    {"assunto": "Alerta de segurança", "destinatario": "cliente9@empresa.com", "remetente": "seguranca@empresa.com", "conteudo": "Detectamos uma tentativa de acesso não autorizado."},
    {"assunto": "Pesquisa de satisfação", "destinatario": "cliente10@empresa.com", "remetente": "pesquisa@empresa.com", "conteudo": "Nos conte como foi sua experiência conosco."},
    {"assunto": "Parceria estratégica", "destinatario": "cliente11@empresa.com", "remetente": "parcerias@empresa.com", "conteudo": "Temos uma nova proposta de parceria para você."},
    {"assunto": "Confirmação de pagamento", "destinatario": "cliente12@empresa.com", "remetente": "financeiro@empresa.com", "conteudo": "Seu pagamento foi confirmado."},
    {"assunto": "Nota de agradecimento", "destinatario": "cliente13@empresa.com", "remetente": "suporte@empresa.com", "conteudo": "Agradecemos por ser nosso cliente."},
    {"assunto": "Oferta especial", "destinatario": "cliente14@empresa.com", "remetente": "marketing@empresa.com", "conteudo": "Confira nossa oferta especial de fim de ano."},
    {"assunto": "Relatório mensal", "destinatario": "cliente15@empresa.com", "remetente": "financeiro@empresa.com", "conteudo": "Aqui está o relatório financeiro do último mês."},
    {"assunto": "Pedido em andamento", "destinatario": "cliente16@empresa.com", "remetente": "vendas@empresa.com", "conteudo": "Seu pedido está sendo processado."},
    {"assunto": "Aviso de renovação", "destinatario": "cliente17@empresa.com", "remetente": "suporte@empresa.com", "conteudo": "Seu plano está próximo de ser renovado."},
    {"assunto": "Convite para evento", "destinatario": "cliente18@empresa.com", "remetente": "eventos@empresa.com", "conteudo": "Você está convidado(a) para nosso evento anual."},
    {"assunto": "Atualização de políticas", "destinatario": "cliente19@empresa.com", "remetente": "juridico@empresa.com", "conteudo": "As políticas de uso foram atualizadas."},
    {"assunto": "Seu feedback é importante", "destinatario": "cliente20@empresa.com", "remetente": "pesquisa@empresa.com", "conteudo": "Por favor, nos conte sua opinião sobre nossos serviços."}
]

for mensagem in mensagens:
    banco.inclui(mensagem)

print("20 mensagens foram inseridas com sucesso!")