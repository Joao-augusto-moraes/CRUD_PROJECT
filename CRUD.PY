#MODULARIZAÇÃO DO CÓDIGO (FUNÇÕES)
#IMPORTANDO O JSON
import json
#FUNÇÃO PARA ESCREVER E SALVAR OS ARQUIVOS EM JSON
def salvar(lista_qualquer, nome_arquivo):
        with open(nome_arquivo,'w', encoding='utf-8') as arquivo_aberto:
                json.dump(lista_qualquer,arquivo_aberto, ensure_ascii=False)

#FUNÇÃO PARA LER OS ARQUIVOS EM JSON
def ler_arquivo(nome_arquivo):
        try:
            with open(nome_arquivo,'r', encoding='utf-8') as arquivo_aberto:
              lista_qualquer = json.load(arquivo_aberto)
              return lista_qualquer
        except:
                return[]
#FUNÇÃO PARA MOSTRAR O MENU PRINCIPAL
def mostrar_menu_principal():
        print('######-BEM-VINDO AO MENU PRINCIPAL DE GERENCIAMENTO-######\n'
            '[1]Gerenciar Estudantes.\n'
            '[2]Gerenciar Professores.\n'
            '[3]Gerenciar Turmas.\n' 
            '[4]Gerenciar Matrículas.\n'
            '[5]Gerenciar Disciplinas.\n'
            '[6]Gerenciar Encerrar.\n')
        return int(input('Digite o número da opção válida que você escolheu:'))

#FUNÇÃO PARA MOSTRAR O MENU DE OPERAÇÕES
def menu_operacoes():
        print('######-BEM-VINDO AO MENU DE OPERAÇÕES-######\n'
                '[1] Listar\n'
                '[2] Incluir\n'
                '[3] Excluir\n'
                '[4] Editar\n'
                '[5] Menu Principal\n')
        return int(input('Digite o número da opção válida que você escolheu:'))
               
#FUNÇÕES PARA LISTAR, INCLUIR, EXCLUIR E EDITAR OS ESTUDANTES, PROFESSORES, TURMAS, MATRICULAS E DISCIPLINAS 
def listar_estudantes(lista_qualquer):
        print('----[LISTAR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('estudantes.json')
        for dados in lista_qualquer:
                print(dados)
        if len(lista_qualquer) == 0:
                print('---NÃO HÁ DADOS CADASTRADOS---')
                
def listar_professores(lista_qualquer):
        print('----[LISTAR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('professores.json')
        for dados in lista_qualquer:
                print(dados)
        if len(lista_qualquer) == 0:
                print('---NÃO HÁ DADOS CADASTRADOS---')
                
def listar_turmas(lista_qualquer):
        print('----[LISTAR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('turmas.json')
        for dados in lista_qualquer:
                print(dados)
        if len(lista_qualquer) == 0:
                print('---NÃO HÁ DADOS CADASTRADOS---')
                
def listar_matriculas(lista_qualquer):
        print('----[LISTAR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('matriculas.json')
        for dados in lista_qualquer:
                print(dados)
        if len(lista_qualquer) == 0:
                print('---NÃO HÁ DADOS CADASTRADOS---')
                
def listar_disciplina(lista_qualquer):
        print('----[LISTAR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('disciplina.json')
        for dados in lista_qualquer:
                print(dados)
        if len(lista_qualquer) == 0:
                print('---NÃO HÁ DADOS CADASTRADOS---')                                     
                
def incluir_estudantes(lista_qualquer):
        print('----[INCLUIR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('estudantes.json')
        while True:
            try:
                codigo = int(input('DIGITE O CÓDIGO DO ESTUDANTE:'))
            except:
                    print('APENAS NÚMEROS SÃO VÁLIDOS')
                    continue
            for i in lista_qualquer:
                if i["---CODIGO_ESTUDANTE---"] == codigo:
                        print('ESTE CÓDIGO JÁ EXISTE')
                        return incluir_estudantes(lista_qualquer)
            nome = input('DIGITE O NOME DO ESTUDANTE:')   
            cpf = input('DIGITE O CPF DO ESTUDANTE:')
            dados_cadastro = {
                       "---NOME_ESTUDANTE---": nome,
                       "---CPF_ESTUDANTE---": cpf,
                       "---CODIGO_ESTUDANTE---":codigo
                }
            break
        lista_qualquer.append(dados_cadastro)
        salvar(lista_qualquer,'estudantes.json')
        
def incluir_professores(lista_qualquer):
        print('----[INCLUIR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('professores.json')
        while True:
            try:
                codigo = int(input('DIGITE O CÓDIGO DO(A) PROFESSOR(A):'))
            except:
                    print('APENAS NÚMEROS SÃO VÁLIDOS')
                    continue
            for i in lista_qualquer:
                if i["---CODIGO_PROFESSOR---"] == codigo:
                        print('ESTE CÓDIGO JÁ EXISTE')
                        return incluir_professores(lista_qualquer)
            nome = input('DIGITE O NOME DO(A) PROFESSOR(A):')   
            cpf = input('DIGITE O CPF DO(A) PROFESSOR(A):')
            dados_cadastro = {
                       "---NOME_PROFESSOR---": nome,
                       "---CPF_PROFESSOR---": cpf,
                       "---CODIGO_PROFESSOR---":codigo
                }
            break
        lista_qualquer.append(dados_cadastro)
        salvar(lista_qualquer,'professores.json')

def incluir_turmas(lista_qualquer):
        print('----[INCLUIR] MENU DE OPERAÇÕES----\n')
        lista_qualquer = ler_arquivo('turmas.json')
        while True:
            try:
                codigo_turma = int(input('DIGITE O CÓDIGO DA TURMA:'))
                for i in lista_qualquer:
                    if i['---CODIGO_TURMA---'] == codigo_turma:
                        print('ESTE CÓDIGO JÁ EXISTE')
                        return incluir_turmas(lista_qualquer)
                codigo_professor = int(input('DIGITE O CÓDIGO DO PROFESSOR:'))
                codigo_da_disciplina = int(input('DIGITE O CÓDIGO DA DISCIPLINA:'))
            except:
                    print('APENAS NÚMEROS SÃO VÁLIDOS')
                    continue
            dados_cadastro = {
              '---CODIGO_TURMA---': codigo_turma,
              '---CODIGO_PROFESSOR_TURMAS---':  codigo_professor,
              '---CODIGO_DISCIPLINAS_TURMAS---': codigo_da_disciplina
                }
            break
        lista_qualquer.append(dados_cadastro)
        salvar(lista_qualquer,'turmas.json')

def incluir_disciplinas(lista_qualquer):
        lista_qualquer = ler_arquivo('disciplina.json')
        while True:
             try:     
                codigo = int(input('DIGITE O CÓDIGO DA DISCIPLINA:'))
             except:
                print('APENAS NÚMEROS SÃO POSSÍVEIS')
                continue
             for i in lista_qualquer:
                if i['---CODIGO_DISCIPLINAS---'] == codigo:
                        print('ESTE CÓDIGO JÁ EXISTE')
                        return incluir_disciplinas(lista_qualquer)
             nome_da_disciplinas = input('DIGITE O NOME DA DISCIPLINA:')
             dados_disciplinas = {
                '---CODIGO_DISCIPLINAS---': codigo,
                '---NOME_DISCIPLINAS---': nome_da_disciplinas
            }
             break
        lista_qualquer.append(dados_disciplinas)
        salvar(lista_qualquer, 'disciplina.json')     
            
def incluir_matriculas(lista_qualquer):
        lista_qualquer = ler_arquivo('matriculas.json')
        while True:
            try:
               codigo_matricula = int(input('DIGITE O CÓDIGO DA TURMA:'))
               for i in lista_qualquer:
                   if i['---CODIGO_MATRICULA---'] == codigo_matricula:
                        print('ESTE CÓDIGO JÁ EXISTE')
                        return incluir_matriculas(lista_qualquer)
               codigo_estudante = int(input('DIGITE O CÓDIGO DO ESTUDANTE:'))
            except:
               print('APENAS NÚMEROS SÃO POSSÍVEIS')
               continue  
            dados_matriculas = {
                    '---CODIGO_MATRICULA---': codigo_matricula,
                    '---CODIGO_ESTUDANTE_MATRICULA---': codigo_estudante
            }
            break
        lista_qualquer.append(dados_matriculas)
        salvar(lista_qualquer, 'matriculas.json')   

def excluir_estudantes(lista_qualquer):
        print('----[EXCLUIR] MENU DE OPERAÇÕES----\n')
        codigo_excluir = int(input('DIGITE O CÓDIGO DO CADASTRO QUE DESEJA EXCLUIR:'))
        dado_excluido = None
        lista_qualquer = ler_arquivo('estudantes.json')
        for dicionario in lista_qualquer:
            if dicionario["---CODIGO_ESTUDANTE---"] == codigo_excluir:
                dado_excluido = dicionario
                break
        if dado_excluido is None:
                print('DADO NÃO ENCONTRADO PARA EXCLUIR')
        else:
                lista_qualquer.remove(dado_excluido)
        salvar(lista_qualquer,'estudantes.json')
        
def excluir_professores(lista_qualquer):
        print('----[EXCLUIR] MENU DE OPERAÇÕES----\n')
        codigo_excluir = int(input('DIGITE O CÓDIGO DO CADASTRO QUE DESEJA EXCLUIR:'))
        dado_excluido = None
        lista_qualquer = ler_arquivo('professores.json')
        for dicionario in lista_qualquer:
            if dicionario["---CODIGO_PROFESSOR---"] == codigo_excluir:
                dado_excluido = dicionario
                break
        if dado_excluido is None:
                print('DADO NÃO ENCONTRADO PARA EXCLUIR')
        else:
                lista_qualquer.remove(dado_excluido)
        salvar(lista_qualquer,'professores.json')  
        
def excluir_turmas(lista_qualquer):
        print('----[EXCLUIR] MENU DE OPERAÇÕES----\n')
        codigo_excluir = int(input('DIGITE O CÓDIGO DO CADASTRO QUE DESEJA EXCLUIR:'))
        dado_excluido = None
        lista_qualquer = ler_arquivo('turmas.json')
        for dicionario in lista_qualquer:
            if dicionario["---CODIGO_TURMA---"] == codigo_excluir:
                dado_excluido = dicionario
                break
        if dado_excluido is None:
                print('DADO NÃO ENCONTRADO PARA EXCLUIR')
        else:
                lista_qualquer.remove(dado_excluido)
        salvar(lista_qualquer,'turmas.json')          
        
def excluir_disciplinas(lista_qualquer):
        print('----[EXCLUIR] MENU DE OPERAÇÕES----\n')
        codigo_excluir = int(input('DIGITE O CÓDIGO DO CADASTRO QUE DESEJA EXCLUIR:'))
        dado_excluido = None
        lista_qualquer = ler_arquivo('disciplina.json')
        for dicionario in lista_qualquer:
            if dicionario["---CODIGO_DISCIPLINAS---"] == codigo_excluir:
                dado_excluido = dicionario
                break
        if dado_excluido is None:
                print('DADO NÃO ENCONTRADO PARA EXCLUIR')
        else:
                lista_qualquer.remove(dado_excluido)
        salvar(lista_qualquer,'disciplina.json')
        
def excluir_matriculas(lista_qualquer):
        print('----[EXCLUIR] MENU DE OPERAÇÕES----\n')
        codigo_excluir = int(input('DIGITE O CÓDIGO DO CADASTRO QUE DESEJA EXCLUIR:'))
        dado_excluido = None
        lista_qualquer = ler_arquivo('matriculas.json')
        for dicionario in lista_qualquer:
            if dicionario["---CODIGO_MATRICULA---"] == codigo_excluir:
                dado_excluido = dicionario
                break
        if dado_excluido is None:
                print('DADO NÃO ENCONTRADO PARA EXCLUIR')
        else:
                lista_qualquer.remove(dado_excluido)
        salvar(lista_qualquer,'matriculas.json')                                 

def editar_estudantes(lista_qualquer):
        print('----[EDITAR] MENU DE OPERAÇÕES----\n')
        codigo_edicao = int(input('DIGITE O CÓDIGO QUE DESEJA EDITAR:'))
        dado_edicao = None
        lista_qualquer = ler_arquivo('estudantes.json')
        for dicionario in lista_qualquer:
                if dicionario["---CODIGO_ESTUDANTE---"] == codigo_edicao:
                        dado_edicao = dicionario
                        break
        if dado_edicao is None:
                print('DADO NÃO ENCONTRADO PARA EDITAR')
        else:
                dado_edicao["---NOME_ESTUDANTE---"] = input('DIGITE O NOVO NOME:')
                dado_edicao["---CPF_ESTUDANTE---"] = input('DIGITE O NOVO CPF:')
                dado_edicao["---CODIGO_ESTUDANTE---"] = int(input('DIGITE O NOVO CÓDIGO:'))
        salvar(lista_qualquer,'estudantes.json')
        
def editar_professores(lista_qualquer):
        print('----[EDITAR] MENU DE OPERAÇÕES----\n')
        codigo_edicao = int(input('DIGITE O CÓDIGO QUE DESEJA EDITAR:'))
        dado_edicao = None
        lista_qualquer = ler_arquivo('professores.json')
        for dicionario in lista_qualquer:
                if dicionario["---CODIGO_PROFESSOR---"] == codigo_edicao:
                        dado_edicao = dicionario
                        break
        if dado_edicao is None:
                print('DADO NÃO ENCONTRADO PARA EDITAR')
        else:
                dado_edicao["---NOME_ESTUDANTE---"] = input('DIGITE O NOVO NOME:')
                dado_edicao["---CPF_ESTUDANTE---"] = input('DIGITE O NOVO CPF:')
                dado_edicao["---CODIGO_ESTUDANTE---"] = int(input('DIGITE O NOVO CÓDIGO:'))
        salvar(lista_qualquer,'professores.json')        
        
def editar_turmas(lista_qualquer):
        print('----[EDITAR] MENU DE OPERAÇÕES----\n')
        codigo_edicao = int(input('DIGITE O CÓDIGO QUE DESEJA EDITAR:'))
        dado_edicao = None
        lista_qualquer = ler_arquivo('turmas.json')
        for dicionario in lista_qualquer:
                if dicionario["---CODIGO_TURMA---"] == codigo_edicao:
                        dado_edicao = dicionario
                        break
        if dado_edicao is None:
                print('DADO NÃO ENCONTRADO PARA EDITAR')
        else:
                dado_edicao["---CODIGO_DISCIPLINAS---"] = int(input('DIGITE O NOVO CÓDIGO DISCIPLINAS:'))
                dado_edicao["---CODIGO_PROFESSOR---"] = int(input('DIGITE O NOVO CÓDIGO PROFESSOR:'))
                dado_edicao["---CODIGO_TURMA---"] = int(input('DIGITE O NOVO CÓDIGO TURMA:'))
        salvar(lista_qualquer,'turmas.json')
        
def editar_disciplinas(lista_qualquer):
        print('----[EDITAR] MENU DE OPERAÇÕES----\n')
        codigo_edicao = int(input('DIGITE O CÓDIGO QUE DESEJA EDITAR:'))
        dado_edicao = None
        lista_qualquer = ler_arquivo('disciplina.json')
        for dicionario in lista_qualquer:
                if dicionario["---CODIGO_DISCIPLINAS---"] == codigo_edicao:
                        dado_edicao = dicionario
                        break
        if dado_edicao is None:
                print('DADO NÃO ENCONTRADO PARA EDITAR')
        else:
                dado_edicao["---CODIGO_DISCIPLINAS---"] = int(input('DIGITE O NOVO CÓDIGO:'))
                dado_edicao["---NOME_DISCIPLINAS---"] = input('DIGITE O NOVO NOME:')
        salvar(lista_qualquer,('disciplina.json'))
        
def editar_matriculas(lista_qualquer):
        print('----[EDITAR] MENU DE OPERAÇÕES----\n')
        codigo_edicao = int(input('DIGITE O CÓDIGO QUE DESEJA EDITAR:'))
        dado_edicao = None
        lista_qualquer = ler_arquivo('matriculas.json')
        for dicionario in lista_qualquer:
                if dicionario["---CODIGO_MATRICULA---"] == codigo_edicao:
                        dado_edicao = dicionario
                        break
        if dado_edicao is None:
                print('DADO NÃO ENCONTRADO PARA EDITAR')
        else:
                dado_edicao["---CODIGO_MATRICULA---"] = int(input('DIGITE O NOVO CÓDIGO MATRICULA:'))
                dado_edicao["---CODIGO_ESTUDANTE_MATRICULA---"] = int(input('DIGITE O NOVO CÓDIGO ESTUDANTES:'))
        salvar(lista_qualquer,'matriculas.json')

estudantes = []
professores = []
turmas = []
matriculas = []
disciplinas = []

#LOOPS PARA REALIZAR AS OPERAÇÕES PARA CADA MÓDULO (ESTUDANTES,PROFESSORES,TURMAS,MATRICULAS E DISCIPLINAS)
while True:
    escolha_do_usuario = mostrar_menu_principal()

### MENU DE OPERAÇÕES
    if escolha_do_usuario == 1:
            
        while True:
            opcao_de_operacao = menu_operacoes()
            
            if opcao_de_operacao == 1:
                    listar_estudantes(estudantes)
                    
            elif opcao_de_operacao == 2:
                    incluir_estudantes(estudantes)
                    
            elif opcao_de_operacao == 3:
                    excluir_estudantes(estudantes)
                    
            elif opcao_de_operacao == 4:
                    editar_estudantes(estudantes)
                    
            elif opcao_de_operacao == 5:
                    print('----VOLTAR AO MENU PRINCIPAL----\n')
                    break
            else:
                    print('ESSA OPÇÃO É INVÁLIDA! ----DIGITE UMA OPÇÃO VÁLIDA----')
      
    if escolha_do_usuario == 2:
            
        while True:
            opcao_de_operacao = menu_operacoes()
            
            if opcao_de_operacao == 1:
                    listar_professores(professores)
                    
            elif opcao_de_operacao == 2:
                    incluir_professores(professores)
                    
            elif opcao_de_operacao == 3:
                    excluir_professores(professores)
                    
            elif opcao_de_operacao == 4:
                    editar_professores(professores)
                    
            elif opcao_de_operacao == 5:
                    print('----VOLTAR AO MENU PRINCIPAL----\n')
                    break
            else:
                    print('ESSA OPÇÃO É INVÁLIDA! ----DIGITE UMA OPÇÃO VÁLIDA----')
    
    if escolha_do_usuario == 3:
            
        while True:
            opcao_de_operacao = menu_operacoes()
            
            if opcao_de_operacao == 1:
                    listar_turmas(turmas)
                    
            elif opcao_de_operacao == 2:
                    incluir_turmas(turmas)
                    
            elif opcao_de_operacao == 3:
                    excluir_turmas(turmas)
                    
            elif opcao_de_operacao == 4:
                    editar_turmas(turmas)
                    
            elif opcao_de_operacao == 5:
                    print('----VOLTAR AO MENU PRINCIPAL----\n')
                    break
            else:
                    print('ESSA OPÇÃO É INVÁLIDA! ----DIGITE UMA OPÇÃO VÁLIDA----')
    
    if escolha_do_usuario == 4:
            
        while True:
            opcao_de_operacao = menu_operacoes()
            
            if opcao_de_operacao == 1:
                    listar_matriculas(matriculas)
                    
            elif opcao_de_operacao == 2:
                    incluir_matriculas(matriculas)
                    
            elif opcao_de_operacao == 3:
                    excluir_matriculas(matriculas)
                    
            elif opcao_de_operacao == 4:
                    editar_matriculas(matriculas)
                    
            elif opcao_de_operacao == 5:
                    print('----VOLTAR AO MENU PRINCIPAL----\n')
                    break
            else:
                    print('ESSA OPÇÃO É INVÁLIDA! ----DIGITE UMA OPÇÃO VÁLIDA----')
    
    if escolha_do_usuario == 5:
            
        while True:
            opcao_de_operacao = menu_operacoes()
            
            if opcao_de_operacao == 1:
                    listar_disciplina(disciplinas)
                    
            elif opcao_de_operacao == 2:
                    incluir_disciplinas(disciplinas)
                    
            elif opcao_de_operacao == 3:
                    excluir_disciplinas(disciplinas)
                    
            elif opcao_de_operacao == 4:
                    editar_disciplinas(disciplinas)
                    
            elif opcao_de_operacao == 5:
                    print('----VOLTAR AO MENU PRINCIPAL----\n')
                    break
            else:
                    print('ESSA OPÇÃO É INVÁLIDA! ----DIGITE UMA OPÇÃO VÁLIDA----')            
    elif escolha_do_usuario == 6:
        break
    else: print('ESSA OPÇÃO É INVÁLIDA')