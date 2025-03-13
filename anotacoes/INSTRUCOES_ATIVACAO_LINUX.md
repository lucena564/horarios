# Como Ativar o Subsistema Windows para Linux (WSL)

## 1️⃣ Ativar o WSL

Abra o **Prompt de Comando (cmd) como Administrador** e execute:

```sh
wsl --install
```

Isso instala o WSL junto com a distribuição padrão do Ubuntu. Se for a primeira vez que usa o WSL, pode ser necessário reiniciar o PC após a instalação.

---

## 2️⃣ Instalar uma distribuição Linux específica (opcional)

Caso queira instalar outra distribuição, liste as disponíveis com:

```sh
wsl --list --online
```

E instale, por exemplo, o Debian com:

```sh
wsl --install -d Debian
```

---

## 3️⃣ Acessar o WSL pelo CMD

Depois de instalado, basta digitar no **cmd**:

```sh
wsl
```

Isso abrirá o shell da distribuição Linux instalada.

Se você tiver mais de uma distribuição instalada, pode abrir uma específica assim:

```sh
wsl -d Ubuntu
```

---

## 4️⃣ Definir a distribuição padrão (caso tenha mais de uma)

Para definir uma distribuição específica como padrão ao executar `wsl`, use:

```sh
wsl --set-default Ubuntu
```

---

## 5️⃣ Verificar e atualizar a versão do WSL

Para ver a versão atual:

```sh
wsl --version
```

Se estiver na versão 1 e quiser atualizar para a 2 (recomendado), use:

```sh
wsl --set-version Ubuntu 2
```

Agora, você pode rodar comandos do Linux no Windows diretamente pelo **cmd** ou pelo **PowerShell**! 🚀


