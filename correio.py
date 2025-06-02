pacotes = (
    ("ABC123", "Enviado"),
    ("XYZ789", "Recebido"),
    ("DEF456", "Em transito"),
    ("KL321", "Enviado"),
    ("MNO654", "Recebido"),
    ("PQR987", "Em transito"),
    ("STU741", "Enviado")
)

def contar_status(pacotes):
    contagem = {"Enviado": 0, "Recebido": 0, "Em transito": 0}
    for _, status in pacotes:
        if status in contagem:
            contagem[status] += 1
    return contagem

def listar_em_transito(pacotes):
    return [codigo for codigo, status in pacotes if status.lower() == "em transito"]

def buscar_status(codigo_busca, pacotes):
    for codigo, status in pacotes:
        if codigo == codigo_busca:
            return f"Status do pacote {codigo}: {status}"
    return "Pacote não cadastrado."

def ordenar_pacotes(pacotes):
    return tuple(sorted(pacotes, key=lambda x: x[0]))

print("1. Contagem de pacotes por status:")
contagem = contar_status(pacotes)
for status, qtd in contagem.items():
    print(f"  {status}: {qtd}")

print("\n2. Códigos de pacotes 'Em transito':")
em_transito = listar_em_transito(pacotes)
print(f"  {em_transito}")

print("\n3. Buscar status de um pacote:")
codigo_exemplo = "DEF456"
print(buscar_status(codigo_exemplo, pacotes))

print("\n4. Pacotes ordenados por código de rastreamento:")
ordenados = ordenar_pacotes(pacotes)
for pacote in ordenados:
    print(f"  {pacote}")