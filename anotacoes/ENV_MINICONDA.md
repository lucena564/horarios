# Criando um Ambiente Virtual com Miniconda

## 1️⃣ Criar um Ambiente Virtual com Conda

Depois de instalar o Miniconda, você pode criar um ambiente virtual para organizar pacotes e dependências.

1. Abra o terminal (ou **Prompt de Comando** no Windows) e crie um novo ambiente:
   ```sh
   conda create --name meu_env python=3.9
   ```
   *Substitua `meu_env` pelo nome desejado e `3.9` pela versão do Python que deseja usar.*

2. Ative o ambiente virtual:
   - **Windows**:
     ```sh
     conda activate meu_env
     ```
   - **Linux/macOS**:
     ```sh
     source activate meu_env
     ```

3. Para listar todos os ambientes disponíveis:
   ```sh
   conda env list
   ```

4. Para instalar pacotes dentro do ambiente:
   ```sh
   conda install numpy pandas
   ```

5. Para sair do ambiente virtual:
   ```sh
   conda deactivate
   ```

---

## 3️⃣ Remover um Ambiente Virtual
Se você não precisar mais de um ambiente, pode removê-lo com:
```sh
conda remove --name meu_env --all
```

---

Agora você pode usar ambientes isolados para gerenciar diferentes versões do Python e pacotes sem conflitos! 🚀
