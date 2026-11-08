# Lab: Red Hat Enterprise Linux no WSL2

Laboratório de administração Linux: Red Hat Enterprise Linux rodando no WSL2 com configuração de systemd, rede, provisionamento idempotente e registro na Red Hat Subscription Manager.

Este é o **Lab 1 (base)** do portfólio de Alex Rabelo — Cloud, DevOps & SRE. Documenta a instalação completa do RHEL 10.2 no Windows Subsystem for Linux 2 (WSL2), utilizando a assinatura gratuita para desenvolvedores individuais da Red Hat.

## Stack

- Red Hat Enterprise Linux 10.2 (WSL2)
- Bash / Shell Script
- GitHub Actions (ShellCheck + Bats)
- Red Hat Developer Subscription (gratuita para indivíduos)
- Red Hat Lightspeed Image Builder (opcional, para imagens customizadas)
- systemd, dnf, subscription-manager

## Como este projeto foi construído (transparência de IA)

| Etapa | Ferramenta / IA usada | O que eu fiz |
|-------|----------------------|--------------|
| Pesquisa de documentação RHEL + WSL2 | Leitura de docs oficiais da Red Hat e Microsoft | Validei cada passo manualmente |
| Rascunho do tutorial de instalação | OpenCode como sugestão | Reescrevi com comandos exatos, validei sintaxe |
| Estrutura do tutorial (markdown) | Escrito manualmente | Organizei em passos numerados com comandos copy-paste |
| Criação do template de imagens | Escrito manualmente | Defini 15 placeholders com nomes descritivos e checklist de segurança |
| Análise crítica da solução | Escrito manualmente | Avaliei pontos fortes, limitações e veredito do projeto |

## Decisões que a IA não tomou

- Escolha do WSL2 em vez de VirtualBox (performance e integração com Windows).
- Escolha do RHEL 10.2 como versão alvo (mais recente estável no momento).
- Estrutura de pastas do repositório.
- Quais métricas de sucesso definir.
- Responsabilidade pelo que roda em produção.

## Conteúdo do repositório

| Arquivo | Conteúdo |
|---------|----------|
| [lab-rhel-wsl2-tutorial.md](lab-rhel-wsl2-tutorial.md) | Tutorial completo com diagrama Mermaid da arquitetura, passos detalhados e análise crítica |
| [TEMPLATE_IMAGES_RHEL_WSL2.md](TEMPLATE_IMAGES_RHEL_WSL2.md) | Template com 15 placeholders de imagem, exemplos de inserção e checklist de segurança |

## Como usar este lab

1. Clone este repositório
2. Leia `lab-rhel-wsl2-tutorial.md` seguindo os passos sequenciais
3. Capture as imagens conforme o `TEMPLATE_IMAGES_RHEL_WSL2.md`
4. Substitua os placeholders por suas próprias capturas de tela
5. Publique no GitHub Pages ou como documentação do repositório

## Link para o portfólio

[alexrabelo.github.io](https://alexrabelo.github.io/) — hub com todos os labs e a síntese de pesquisa de mercado.

---

🤖 **Construído com auxílio de IA — revisado, testado e operado por mim.**

Regra de ouro: nunca publicar algo que não consigo explicar linha por linha, rodar sozinho e defender em entrevista técnica.