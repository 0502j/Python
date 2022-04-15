from datetime import date

class Aluno:
    def __init__(self, nome, sobrenome, curso):
            self._nome = nome
            self._sobrenome = sobrenome
            self._curso = curso

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    #Desenvolver property e property.setter para nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    #Sobrescrever o método str e retornar o atributo nome
    def __str__(self):
        return self._nome

    #def __str__(self):
        #pass


    #Sobrescrever o método repr e retornar o atributo nome acrescido de um espaço e
    # o atributo sobrenome
    def __repr__(self):
        return self._nome + " " + self._sobrenome

    #def __repr__(self):
     #   pass


class Professor:
    def __init__(self, nome, sobrenome):
            self._nome = nome
            self._sobrenome = sobrenome
            self._disciplinas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor


    #Desenvolver property para o atributo disciplina

    # @property
    # def disciplina(self):
        #pass

    @property
    def disciplina(self):
        return self._disciplinas


    #Esse método adiciona a lista disciplina o nome da disciplina passada como parâmetro
    def adicionar_disciplina(self, disciplina):
        return self._disciplinas.append(disciplina)


    #Sobreescrever os métodos __str__ e __repr__. 
    #Estes métodos retornam o atributo nome do professor
    
    def __str__(self):
        return self._nome
    def __repr__(self):
        return self._nome

    #def __str__(self):
        #pass

    #def __repr__(self):
        #pass



class SalaAula:
    def __init__(self, professor):
        if isinstance(professor, Professor):
            self._professor = professor
        else:
            raise TypeError('Tipo do professor precisa instância de Professor')
        self._alunos = []

    @property
    def professor(self):
        return str(self._professor)

    @property
    def alunos(self):
        return self._alunos

    #def adicionar_aluno(self, nome, sobrenome, curso):
        #pass

    #def busca_aluno(self, nome_procurado):
        #pass
    
    def __str__(self):
        return 'Sala com prof. ' + self.professor

    def __repr__(self):
        return str(self)


    # Desenvolver o método adicionar_aluno. 
    # Este método recebe os parâmetros nome, sobrenome e curso do aluno, 
    # instancia um objeto do tipo Aluno e adiciona a lista interna de alunos.

    def adicionar_aluno(self, nome, sobrenome, curso):
        return self._alunos.append(Aluno(nome, sobrenome, curso))

    #Desenvolver o método busca_aluno. Este método recebe como parâmetro o nome de um aluno 
    # procurado e pesquisa na lista interna de alunos. Caso encontre retorna o objeto aluno. 
    # Se não encontra retorna none.

    def busca_aluno(self, nome_procurado):

        for aluno in self._alunos:
            if aluno.nome == nome_procurado:
                return aluno
        
        return None