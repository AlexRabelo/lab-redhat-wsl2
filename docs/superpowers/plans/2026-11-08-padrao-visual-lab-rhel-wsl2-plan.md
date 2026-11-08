# Padrão Visual — Lab RHEL + WSL2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Aplicar um padrão visual consistente às 15 capturas de tela e ao diagrama Mermaid do lab RHEL + WSL2, com ficha de design escrita e regras de borrado de PII, tudo no repositório `AlexRabelo/lab-redhat-wsl2`.

**Architecture:** Uma ficha de design escrita em Markdown (`docs/design-padrao-visual.md`) define paleta, tipografia, bordas, dimensões e regras de borrado. As 15 imagens existentes são tratadas (redimensionadas, bordadas, PII borrado) conforme a ficha. O diagrama Mermaid no tutorial é atualizado para tema escuro com a mesma paleta.

**Tech Stack:** Markdown, Mermaid, GIMP/ImageMagick (edição de imagem local), Git

**Spec:** `docs/superpowers/specs/2026-11-08-padrao-visual-lab-rhel-wsl2-design.md`

## Global Constraints

- Escopo restrito ao repositório `lab-redhat-wsl2` (não tocar outros repositórios agora)
- Paleta: fundo `#08090c`, acento `#22d3ee`, azul `#3b82f6`, borda `#1e293b`
- Tipografia: Outfit (títulos), Source Sans 3 (corpo)
- Borda: raio 8px, 1px `#1e293b`, sombra suave
- Dimensões alvo: 16:9 (ex: 1200×675)
- Borrado de PII: retângulo opaco sobre nome de usuário Windows, e-mail Red Hat, IPs, chaves
- Mermaid: tema `dark`, cores da paleta
- Imagens exibíveis em Markdown do GitHub (caminhos locais `assets/imgs/lab-rhel-wsl2/`)

## Review Focus

- Imagem com PII não borrado antes do commit — cada imagem tratada deve ter PII verificado como borrado ou removido
- Diagrama Mermaid que não renderiza no GitHub — verificar sintaxe `%%{init: ...}%%` e tema escuro
- Caminho de imagem quebrado no Markdown — verificar que cada `![...](./assets/imgs/lab-rhel-wsl2/...)` aponta para arquivo existente
- Dimensão fora do padrão 16:9 — verificar consistência entre as 15 imagens

---

### Task 1: Escrever ficha de design visual

**Files:**
- Create: `docs/design-padrao-visual.md`

**Interfaces:**
- Consumes: nada (documento base)
- Produces: ficha de design completa referenciada por todas as tarefas seguintes

- [ ] **Step 1: Escrever `docs/design-padrao-visual.md`**

Escrever o documento com: paleta de cores, tipografia, bordas/sombra, dimensões alvo, regras de borrado de PII, instruções para Mermaid tema escuro, e passo a passo para captura de novas imagens. Usar os valores exatos da Global Constraints acima.

- [ ] **Step 2: Commit**

```bash
git add docs/design-padrao-visual.md
git commit -m "docs(design): adiciona ficha de padrao visual do lab RHEL WSL2"
```

---

### Task 2: Aplicar padrão às 15 imagens existentes

**Files:**
- Modify: `assets/imgs/lab-rhel-wsl2/*.png` (15 arquivos)

**Interfaces:**
- Consumes: ficha de design de Task 1 (valores de cor, borda, dimensão, PII)
- Produces: 15 imagens tratadas, consistentes entre si

- [ ] **Step 1: Listar as 15 imagens e verificar PII em cada**

Para cada arquivo em `assets/imgs/lab-rhel-wsl2/`, abrir e verificar se há dados pessoais visíveis (nome de usuário Windows, e-mail Red Hat, IP interno, chave de ativação). Listar quais precisam de borrado.

- [ ] **Step 2: Tratar cada imagem (redimensionar 16:9, borda, sombra, borrar PII)**

Usar GIMP ou ImageMagick para cada uma das 15 imagens:
- Redimensionar para 16:9 (ex: 1200×675) quando possível
- Adicionar borda raio 8px, 1px `#1e293b`, sombra suave
- Borrar com retângulo opaco qualquer dado pessoal identificado no Step 1

- [ ] **Step 3: Verificar que todas as 15 imagens existem e são exibíveis**

Executar um script simples ou comando `ls` para confirmar os 15 arquivos em `assets/imgs/lab-rhel-wsl2/`. Verificar que nenhum caminho no tutorial aponta para arquivo ausente.

- [ ] **Step 4: Commit**

```bash
git add assets/imgs/lab-rhel-wsl2/
git commit -m "feat(images): aplica padrao visual a todas as 15 imagens do lab"
```

---

### Task 3: Atualizar diagrama Mermaid para tema escuro

**Files:**
- Modify: `lab-rhel-wsl2-tutorial.md` (seção do diagrama Mermaid)

**Interfaces:**
- Consumes: ficha de design de Task 1 (cores da paleta, tema dark)
- Produces: diagrama Mermaid renderizado com tema escuro e cores consistentes

- [ ] **Step 1: Localizar o bloco Mermaid no tutorial**

Encontrar o bloco ```mermaid ... ``` em `lab-rhel-wsl2-tutorial.md` (seção Arquitetura da solução).

- [ ] **Step 2: Atualizar para tema escuro com paleta definida**

Adicionar `%%{init: {'theme': 'dark', 'themeVariables': { ... }}}%%` no início do bloco, usando as cores da paleta (`#08090c`, `#22d3ee`, `#3b82f6`, `#1e293b`).

- [ ] **Step 3: Verificar renderização do Mermaid**

Abrir o arquivo no GitHub (ou visualizador local com suporte a Mermaid) e confirmar que o diagrama renderiza com tema escuro.

- [ ] **Step 4: Commit**

```bash
git add lab-rhel-wsl2-tutorial.md
git commit -m "feat(diagram): atualiza Mermaid para tema escuro da paleta de design"
```

---

### Task 4: Documentar passo a passo de captura de novas imagens

**Files:**
- Modify: `docs/design-padrao-visual.md` (adicionar seção de captura)
- Modify: `lab-rhel-wsl2-tutorial.md` (opcional, referenciar a ficha)

**Interfaces:**
- Consumes: ficha de design de Task 1
- Produces: seção na ficha de design com instruções para capturar novas imagens seguindo o padrão

- [ ] **Step 1: Adicionar seção de captura à ficha de design**

Em `docs/design-padrao-visual.md`, adicionar seção "Como capturar novas imagens" com: ferramenta (GIMP/ImageMagick), dimensão alvo, borda, borrado de PII, nomeação de arquivo (minúsculo, descritivo), caminho de destino (`assets/imgs/lab-rhel-wsl2/`).

- [ ] **Step 2: Commit**

```bash
git add docs/design-padrao-visual.md
git commit -m "docs(design): adiciona instrucoes de captura de imagens ao padrao visual"
```

---

### Task 5: Verificação final e revisão de toda a branch

**Files:**
- Modify: nenhum (apenas revisão)

**Interfaces:**
- Consumes: todas as tarefas anteriores
- Produces: confirmação de que o padrão está aplicado e consistente

- [ ] **Step 1: Revisar o diff completo**

Executar `git log` e `git diff` para confirmar que todas as alterações estão coerentes com a ficha de design.

- [ ] **Step 2: Verificar que nenhum PII está exposto**

Revisar cada imagem tratada e o texto do tutorial para confirmar que não há nome de usuário Windows, e-mail Red Hat, IP interno ou chave de ativação visível.

- [ ] **Step 3: Commit final**

```bash
git add -A
git commit -m "chore: finaliza aplicacao do padrao visual no lab RHEL WSL2"
```

- [ ] **Step 4: Push para origin main**

```bash
git push origin main
```

---

## Self-review do plano

1. **Spec coverage:** Todos os requirements da spec (ficha de design, 15 imagens, Mermaid tema escuro, borrado PII, passo a passo de captura) têmTask correspondente. Nenhuma lacuna.
2. **Step scan:** Cada step permite ao implementador escrever exatamente uma coisa razoável. Nenhum step carrega mais do que uma decisão.
3. **Type consistency:** Não há tipos de função aqui (não é código de programa), mas os caminhos de arquivo e nomes de tarefa são consistentes entre si.
4. **Review Focus:** Cada um dos 4 itens de Review Focus tem pelo menos uma Task cuja etapa o cobre (PII → Task 2 Step 1/2; Mermaid → Task 3; caminho quebrado → Task 2 Step 3; dimensão → Task 2 Step 2).
5. **Proportion:** O plano tem 5 tasks com steps granulares, proporcional à spec (que é curta e focada).

---

**Plan complete and saved to `docs/superpowers/plans/2026-11-08-padrao-visual-lab-rhel-wsl2-plan.md`.**

Qual execução você prefere?

- **Subagent-driven** — Uma subagente nova implementa cada task e uma revisora nova checa cada uma antes da próxima começar, depois uma revisão de toda a branch no final. Mais completa; custa um contexto novo por task e por revisão.
- **Native** — Eu implemento todas as tasks nesta sessão do jeito que este harness roda o trabalho, e então um revisor único no modelo mais capaz checa a branch inteira no final. Mais barato e rápido; revisão independente só no final.

Para este plano eu recomendo **Native**, porque as tasks são de edição de imagem e diagrama (pouca dependência entre interfaces de código), são poucas (5 tasks), e o custo de um erro enviado é baixo (imagens/diagrama podem ser refeitas).

O plano captura o que você quer? Qual abordagem de execução devemos usar?
