# Design — Padrão Visual: Lab RHEL + WSL2

**Data:** 08/Nov/2026  
**Autor:** Alex Luiz Rabelo — Cloud, DevOps & SRE  
**Repositório:** `AlexRabelo/lab-redhat-wsl2`  
**Escopo:** Apenas o lab RHEL + WSL2 (Opção C — começar só aqui, depois avaliar expansão)

---

## Intent e porquê

Definir uma ficha de design (guia de estilo visual) para as 15 capturas de tela e o diagrama Mermaid do lab RHEL + WSL2, aplicável primeiro a este repositório, com potencial de expansão futura para os outros labs.

O lab já tem imagens capturadas em `assets/imgs/lab-rhel-wsl2/`, mas sem padrão visual definido: dimensões variadas, sem tratamento de borrado de dados pessoais padronizado, e o diagrama Mermaid usa cores padrão. O site do portfólio (`alexrabelo.github.io`) já usa uma paleta dark tecnológica que pode servir de base para este padrão, criando coerência entre o site e os labs.

## Goals

- Padrão visual consistente para as 15 imagens PNG e o diagrama Mermaid
- Dimensões e tratamento padronizados (bordas, sombras, cores)
- Regras claras de borrado de dados pessoais (PII) integradas ao padrão
- Compatível com Markdown do GitHub (imagens locais + Mermaid nativo)
- Base para expansão futura para os outros repositórios

## Non-goals

- Padronizar os outros repositórios agora (`ShellScript`, `iac-terraform-ai-review`, `mlops-k8s-recomendacao`, `llmops-rag-infra`)
- Criar ferramentas automatizadas de edição de imagem
- Hospedar imagens fora do repositório

## Anti-goals

- Imagens com aparências aleatórias ou inconsistentes entre si
- Dados pessoais (nome de usuário Windows, e-mail Red Hat, IPs, chaves de ativação) visíveis em capturas publicadas

## Constraints

- Ferramentas disponíveis localmente (GIMP, ImageMagick, navegador, editores de texto)
- Imagens devem ser exibíveis em Markdown do GitHub
- Diagrama Mermaid deve renderizar nativamente no GitHub
- O padrão deve ser aplicável retroativamente às 15 imagens existentes

## Approaches considerados

| Abordagem | Descrição | Trade-off |
|-----------|-----------|-----------|
| **A** — Padrão baseado no site (`alexrabelo.github.io`) | Reusa a paleta dark do site: `#08090c`, `#22d3ee`, `#3b82f6`, fontes Outfit/Source Sans 3 | Coerente com o portfólio; exige definição exata de cores/bordas |
| **B** — Padrão neutro | Branco/cinza, sem cores fortes, bordas suaves | Menos identidade visual; não aproveita o investimento já feito no site |
| **C** — Sem padrão | Cada imagem fica como está | Descartado: gera inconsistência |

## Decisões tomadas (como builder)

- **Escopo:** apenas `lab-redhat-wsl2` (Opção C, conforme solicitado pelo usuário)
- **Abordagem:** A (baseado no site), por coerência com o portfólio existente
- **Paleta de cores:**
  - Fundo escuro: `#08090c`
  - Acento ciano: `#22d3ee`
  - Azul secundário: `#3b82f6`
  - Bordas: `#1e293b`
  - Texto: `#f8fafc`, texto secundário: `#94a3b8`
- **Tipografia:** Outfit para títulos, Source Sans 3 para corpo (mesmas do site)
- **Bordas:** raio 8px, borda 1px `#1e293b`, sombra suave (`0 8px 24px -4px rgba(0, 0, 0, 0.45)`)
- **Dimensões alvo:** 16:9 (ex: 1200×675) quando possível
- **Borrado de PII:** retângulo opaco sobre dados sensíveis antes de publicar
- **Mermaid:** tema escuro (`dark`), cores consistentes com a paleta

## Arquitetura da solução (diagrama Mermaid)

O diagrama existente no tutorial será atualizado para usar o tema escuro (`%%{init: {'theme': 'dark', ...}%%}`) com a paleta definida acima.

## Entregáveis do builder

1. Criar `docs/design-padrao-visual.md` com a ficha completa de design visual
2. Aplicar o padrão às 15 imagens existentes (redimensionar para 16:9, adicionar bordas/sombra, borrar PII)
3. Atualizar o diagrama Mermaid no `lab-rhel-wsl2-tutorial.md` para o tema escuro da paleta
4. Documentar o passo a passo de captura de novas imagens seguindo o padrão

---

## Notas do builder

Este documento foi revisado por mim (builder) antes de ser apresentado ao usuário. Não há questões pendentes que exijam decisão do usuário além da aprovação deste design.

Aprovação: o usuário sinalizou que quer seguir a sequência sugerida. Este design está pronto para aprovação final e, em seguida, para geração do plano de execução via `writing-plans`.
