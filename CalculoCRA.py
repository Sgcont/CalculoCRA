cra_atual = float(input("Digite seu CRA atual: "))
creditos_atuais = int(input("Digite seus créditos já contabilizados: "))

nota_futura = float(input("Digite a nota da nova disciplina: "))
creditos_futuros = int(input("Digite os créditos da nova disciplina: "))

cra_novo = (
    cra_atual * creditos_atuais
    + nota_futura * creditos_futuros
) / (creditos_atuais + creditos_futuros)

print(f"\nCRA atual: {cra_atual:.2f}")
print(f"Nota futura: {nota_futura:.2f}")
print(f"Novo CRA: {cra_novo:.2f}")
print(f"Variação: {cra_novo - cra_atual:+.2f}")
