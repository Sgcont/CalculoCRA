from math import sqrt


def linear_regression(points):
    n = len(points)
    x_mean = sum(x for x, _ in points) / n
    y_mean = sum(y for _, y in points) / n
    sxx = sum((x - x_mean) ** 2 for x, _ in points)
    if sxx == 0:
        return y_mean, 0.0, x_mean, sxx
    sxy = sum((x - x_mean) * (y - y_mean) for x, y in points)
    slope = sxy / sxx
    intercept = y_mean - slope * x_mean
    return intercept, slope, x_mean, sxx


def residual_std(points, intercept, slope):
    n = len(points)
    if n <= 2:
        return 0.15
    squared_error = sum((y - (intercept + slope * x)) ** 2 for x, y in points)
    value = squared_error / (n - 2)
    return max(sqrt(value), 0.05)


def margin_error_95(x0, n, x_mean, sxx, sigma):
    if sxx == 0:
        return 1.96 * sigma
    adjustment = sqrt(1 + (1 / n) + ((x0 - x_mean) ** 2 / sxx))
    return 1.96 * sigma * adjustment


def clamp_grade(value):
    return max(0.0, min(10.0, value))


def next_cra(cra_atual, creditos_atuais, nota_periodo, creditos_periodo):
    return (
        cra_atual * creditos_atuais + nota_periodo * creditos_periodo
    ) / (creditos_atuais + creditos_periodo)


print("=== Previsão de CRA com modelo simples (regressão linear) ===")
cra_atual = float(input("Digite seu CRA atual: "))
creditos_atuais = int(input("Digite seus créditos já contabilizados: "))

qtd_historico = int(
    input("Quantos CRAs históricos você quer informar? (mínimo 3 recomendado): ")
)
cra_historico = []
for i in range(qtd_historico):
    valor = float(input(f"CRA do período {i + 1}: "))
    cra_historico.append(clamp_grade(valor))

nota_planejada = float(input("Média de nota esperada no próximo período: "))
creditos_planejados = int(input("Créditos esperados por período futuro: "))
horizonte = int(input("Quantos períodos futuros deseja prever? "))

if qtd_historico < 2:
    raise ValueError("Informe pelo menos 2 valores históricos para previsão.")
if creditos_planejados <= 0:
    raise ValueError("Os créditos planejados devem ser maiores que zero.")
if horizonte <= 0:
    raise ValueError("O horizonte de previsão deve ser maior que zero.")

series = [(i + 1, cra) for i, cra in enumerate(cra_historico)]
intercept, slope, x_mean, sxx = linear_regression(series)
sigma = residual_std(series, intercept, slope)

cra_det = cra_atual
cred_det = creditos_atuais
alpha = min(0.8, max(0.4, qtd_historico / (qtd_historico + 4)))

print("\n=== Resultado ===")
print(f"CRA atual: {cra_atual:.2f}")
print(f"Tendência aprendida (inclinação): {slope:+.4f} por período")
print(f"Margem base de erro (desvio residual): ±{sigma:.3f}")

for periodo in range(1, horizonte + 1):
    x0 = qtd_historico + periodo
    cra_ml = clamp_grade(intercept + slope * x0)

    cra_det = next_cra(cra_det, cred_det, nota_planejada, creditos_planejados)
    cred_det += creditos_planejados

    cra_comb = clamp_grade(alpha * cra_ml + (1 - alpha) * cra_det)
    erro = margin_error_95(x0, qtd_historico, x_mean, sxx, sigma)
    limite_inf = clamp_grade(cra_comb - erro)
    limite_sup = clamp_grade(cra_comb + erro)

    print(f"\nPeríodo +{periodo}:")
    print(f"  Previsão ML: {cra_ml:.2f}")
    print(f"  Projeção por créditos/notas: {cra_det:.2f}")
    print(f"  CRA previsto (combinado): {cra_comb:.2f}")
    print(f"  Faixa provável (95%): {limite_inf:.2f} a {limite_sup:.2f}")
