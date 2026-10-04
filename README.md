# CalculoCRA
Simples e direto, calcular o futuro de seu CRA a partir das notas que chegarão

## Nova versão com previsão (ML simples)

O script agora inclui:
- previsão de CRA com regressão linear sobre seu histórico de CRA;
- projeção com base no CRA atual + média de notas + créditos futuros;
- previsão combinada entre tendência histórica e projeção por créditos;
- margem de erro (faixa provável de 95%) para períodos futuros.

### Como usar
1. Execute:
   - `python /home/runner/work/CalculoCRA/CalculoCRA/CalculoCRA.py`
2. Informe:
   - CRA atual e créditos atuais;
   - histórico de CRAs por período (quanto maior, melhor);
   - média de nota esperada e créditos planejados;
   - quantidade de períodos futuros para previsão.

### Observação
É um modelo introdutório para apoio de planejamento acadêmico. A precisão depende da qualidade/quantidade do histórico informado.
