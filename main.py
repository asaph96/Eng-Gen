class MaterialGenetico:
    _lexico = []

    def __init__(self, sequencia):
        self._seq = sequencia
        print("Material genético criado")

    def _is_valid(self):
        for elemento in self.seq.upper():
            if elemento not in self._lexico:
                raise ValueError('Sequência inválida')
            else:
                pass
        return True

    @property
    def seq(self):
        return self._seq.upper()

    @seq.setter
    def seq(self, sequencia):
        if self._is_valid():
            self._seq = sequencia

    def __len__(self):
        return len(self.seq)

class Proteina(MaterialGenetico):
    _lexico = ['A', 'R', 'N', 'D', 'B', 'C', 'E', 'Q', 'Z',
               'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def __init__(self, sequencia):
        super().__init__(sequencia)
        self.seq = sequencia
        print('Proteína criada')

class AcidoNucleico(MaterialGenetico):

    def __init__(self, sequencia):
        super().__init__(sequencia)
        self.seq = sequencia
        print("Ácido nucleico criado com sucesso")