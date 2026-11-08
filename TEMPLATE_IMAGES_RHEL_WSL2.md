# Template de Imagens — Lab RHEL no WSL2

Este arquivo lista todos os placeholders de imagem do tutorial `lab-rhel-wsl2-tutorial.md`, organizados por seção, para facilitar o preenchimento posterior com capturas de tela reais.

---

## Pasta de destino

Todas as imagens devem ser salvas em:

```
assets/imgs/lab-rhel-wsl2/
```

---

## Lista de imagens (em ordem de aparição)

| # | Arquivo | Seção do tutorial | O que capturar |
|---|---------|-------------------|----------------|
| 01 | `wsl-enable-features.png` | Pré-requisitos | Tela do PowerShell com comandos `dism.exe` para habilitar WSL e Virtual Machine Platform |
| 02 | `wsl-version-2.png` | Pré-requisitos | Saída do comando `wsl --set-default-version 2` |
| 03 | `wsl-list-verbose.png` | Pré-requisitos | Saída de `wsl --list --verbose` ANTES de importar o RHEL |
| 04 | `redhat-developer-login.png` | Passo 2 | Tela de cadastro/login no [developers.redhat.com/register](https://developers.redhat.com/register) — **borre dados pessoais** |
| 05 | `redhat-download-page.png` | Passo 3 | Página de downloads da Red Hat com a linha **WSL2 image RHEL 10.2** destacada |
| 06 | `wsl-import-command.png` | Passo 4 | Terminal PowerShell com o comando `wsl --import` digitado |
| 07 | `wsl-list-after-import.png` | Passo 4 | Saída de `wsl --list --verbose` mostrando `RHEL-10.2` na lista |
| 08 | `wsl-rhel-prompt.png` | Passo 4 | Terminal RHEL aberto no WSL2 (prompt `alex@workstation:~$` ou similar) |
| 09 | `cat-redhat-release.png` | Passo 4 | Saída do comando `cat /etc/redhat-release` mostrando `Red Hat Enterprise Linux release 10.2` |
| 10 | `subscription-manager-register.png` | Passo 5 | Terminal com o comando `subscription-manager register` sendo executado |
| 11 | `subscription-manager-status.png` | Passo 5 | Saída de `subscription-manager status` mostrando **Overall Status: Registered** |
| 12 | `dnf-repolist.png` | Passo 6 | Saída de `dnf repolist` mostrando repositórios AppStream e BaseOS |
| 13 | `dnf-update.png` | Passo 6 | Saída do comando `dnf update` em execução |
| 14 | `wsl-default-user.png` | Passo 7 | PowerShell com comando `wsl --manage ... --set-default-user demo` |
| 15 | `final-wsl-terminal.png` | Passo 8 (final) | Tela final do RHEL 10.2 pronto para uso no WSL2 |

---

## Exemplo de inserção no Markdown

```markdown
### Verificar a versão

Dentro do terminal RHEL:

```bash
cat /etc/redhat-release
```

Saída esperada:

```output
Red Hat Enterprise Linux release 10.2
```

![Verificação da versão RHEL 10.2 no WSL2](./assets/imgs/lab-rhel-wsl2/09-cat-redhat-release.png)
```

---

## ⚠️ Cuidados de segurança (obrigatório)

Antes de publicar qualquer imagem, **borre ou remova**:

- [ ] Nome de usuário real do Windows (use `demo` ou borre)
- [ ] E-mail da conta Red Hat
- [ ] Senha ou Activation Key
- [ ] Endereços IP internos ou nomes de máquina reais
- [ ] Chaves de assinatura ou números de entitlement
- [ ] Qualquer informação identificável pessoal (PII)

---

## Checklist de conclusão

- [ ] Todas as 15 imagens capturadas e salvas em `assets/imgs/lab-rhel-wsl2/`
- [ ] Todas as tags `![...](./assets/imgs/lab-rhel-wsl2/XX-nome.png)` presentes no tutorial
- [ ] Dados pessoais borrados ou removidos de todas as imagens
- [ ] Imagens testadas em visualizador Markdown (caminhos corretos)

---

*Última atualização: 08/Nov/2026*  
*Autor: Alex Luiz Rabelo — Cloud, DevOps & SRE*  
*Transparência de IA: Este arquivo foi compilado com auxílio de ferramentas de IA com base em fontes oficiais da Red Hat e Microsoft, e revisado/testado manualmente pelo autor.*