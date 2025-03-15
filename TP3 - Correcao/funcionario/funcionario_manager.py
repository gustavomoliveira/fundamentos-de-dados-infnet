import mysql.connector

class Funcionario:

    def conectar_banco_dados(self):
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="infnet_tp3"
        )
        return conexao
    
    #função para listar funcionarios
    def listar_funcionario(self): 
        conexao = self.conectar_banco_dados()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, cargo, departamento, salario_base from funcionarios")
        funcionarios = cursor.fetchall()

        print("\nFuncionários cadastrados:")
        print("-" * 120)
        relatorio = []

        for func in funcionarios:
            id_func, nome, cargo, departamento, salario_base = func
            inss = self.calcular_inss(salario_base)
            ir = self.calcular_ir(salario_base, inss)
            salario_liquido = salario_base - inss - ir
            relatorio.append((id_func, nome, cargo, departamento, salario_base, inss, ir, salario_liquido))
        
        # Ordernar pelo salario liquido (maior para o menor)
        relatorio.sort(key=lambda x: x[7], reverse=True)

        print("\nFuncionários cadastrados:")
        print("-" * 120)
        print("{:<5} {:<20} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
            "ID", "Nome", "Cargo", "Departamento", "Bruto", "INSS", "IR", "Líquido"
        ))
        print("-" * 120)

        for id_func, nome, cargo, departamento, salario_base, inss, ir, salario_liquido in relatorio:
            print("{:<5} {:<20} {:<15} {:<15} R${:<8.2f} R${:<8.2f} R${:<8.2f} R${:<8.2f}".format(
                id_func, nome, cargo, departamento, salario_base, inss, ir, salario_liquido
            ))
    
        cursor.close()
        conexao.close()
        return funcionarios
    
    #função para adicionar funcionarios
    def adicionar_funcionario(self):
        conexao = self.conectar_banco_dados()
        cursor = conexao.cursor()
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        departamento = input("Departamento: ")
        salario = float(input("Salário Base: "))
        data_admissao = input("Data de Admissão: ")

        query = "INSERT INTO funcionarios (nome, cargo, departamento, salario_base, data_admissao) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, cargo, departamento, salario, data_admissao)

        cursor.execute(query, valores)
        conexao.commit()

        print(f"Funcionário {nome} cadastrado com sucesso!")
        
        cursor.close()
        conexao.close()
    
    # função para atualizar um funcionario
    def atualizar_funcionario(self):
        id_func = int(input("\nDigite o ID do funcionário que deseja atualizar: "))
        
        novo_cargo = input("Novo Cargo (ou pressione Enter para manter): ")
        novo_departamento = input("Novo Departamento (ou pressione Enter para manter): ")
        novo_salario = input("Novo Salário (ou pressione Enter para manter): ")

        query = "UPDATE funcionarios SET "
        valores = []
        atualizacao = False

        if (novo_cargo):
            query += "cargo = %s, "
            valores.append(novo_cargo)
            atualizacao = True
        if (novo_departamento):
            query += "departamento = %s, "
            valores.append(novo_departamento)
            atualizacao = True
        if (novo_salario):
            query += "salario_base = %s, "
            valores.append(novo_salario)
            atualizacao = True
        # Remover a última vírgula
        query = query.rstrip(", ")
        
        # Sempre colocar o id para atualização e exclusão
        query += " WHERE id = %s"

        # colocar O id a ser atualizado
        valores.append(id_func)

        if (atualizacao):
            conexao = self.conectar_banco_dados()
            cursor = conexao.cursor()
            cursor.execute(query, tuple(valores))
            conexao.commit()
            cursor.close()
            conexao.close()
    
    # função para excluir um funcionario
    def excluir_funcionario(self):
        id_func = int(input("\nDigite o ID do funcionário que deseja excluir: "))
        query = "DELETE FROM funcionarios WHERE id = %s"
        conexao = self.conectar_banco_dados()
        cursor = conexao.cursor()
        cursor.execute(query, (id_func, ))
        conexao.commit()
        cursor.close()
        conexao.close()

    # funcão para calcular INSS
    def calcular_inss(self, salario):
        faixas = [(1412.00, 0.075), (2666.68, 0.09), (4000.03, 0.12)]
        teto = 4000.03
        aliquota_final = 0.14
        inss = 0
        restante = salario

        for faixa, aliquota in faixas:
            if (restante > faixa):
                inss += faixa * aliquota
                restante -= faixa
            else:
                inss += restante * aliquota
                restante = 0
                break
        
        if restante > 0:
            inss += restante * aliquota_final
        
        return round(inss, 2)
    
    def calcular_ir(self, salario_base, inss):
        salario_ir = salario_base - inss
        faixas = [(2112.00, 0, 0), (2826.65, 0.075, 158.40), (3751.05, 0.15, 370.40), 
                  (4664.68, 0.225, 651.73), (float('inf'), 0.275, 884.96)]
        
        for limite, aliquota, deducao in faixas:
            if salario_ir <= limite:
                ir = (salario_ir * aliquota) - deducao
                return max(0, round(ir, 2))

        return 0
    










        
        



    

