def definir_prioridade(idade, sexo, gestante, sintoma):
    sintomas_criticos = ["dor no peito", "falta de ar", "desmaio", "convulsão", "sangramento"]

    if sexo.lower() == "feminino" and gestante:
        return "Alta (Gestante)"

    if idade >= 60:
        return "Média (Idoso)"
    
    if idade < 10:
        return "Média (Criança)"

    if sintoma.lower() in sintomas_criticos:
        return "Alta (Sintoma Crítico)"
    
    return "Baixa"

def atendimento():
    print("=== TRIAGEM HOSPITALAR ===")
    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (Masculino/Feminino): ")

    gestante = False
    if sexo.lower() == "feminino" and idade >= 10:
        resposta = input("Está gestante? (s/n): ").strip().lower()
        gestante = resposta == 's'

    sintoma = input("Sintoma principal: ")

    prioridade = definir_prioridade(idade, sexo, gestante, sintoma)

    print("\n=== FICHA DE TRIAGEM ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")
    if sexo.lower() == "feminino" and idade >= 10:
        print(f"Gestante: {'Sim' if gestante else 'Não'}")
    print(f"Sintoma principal: {sintoma}")
    print(f"PRIORIDADE: {prioridade}")

if __name__ == "__main__":
    atendimento()