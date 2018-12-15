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

    def __init__(self, sequencia, degenerado=False):
        super().__init__(sequencia)
        self.seq = sequencia
        self.deg = degenerado
        print("Ácido nucleico criado com sucesso")

    def _is_valid(self):
        if not self.deg:
            for elemento in self.seq.upper():
                if elemento not in self._lexico[0]:
                    raise ValueError('Sequência inválida')
                else:
                    pass
            return True
        else:
            for elemento in self.seq.upper():
                if elemento not in self._lexico[0] and elemento not in self._lexico[1]:
                    raise ValueError('Sequência inválida')
                else:
                    pass
            return True

    def _reverso_complementar(self):
        rev_comp = ''
        index = 1
        try:
            for nucleotideo in self.seq:
                if nucleotideo == self._lexico[0][1]:
                    rev_comp += self._lexico[0][0]
                elif nucleotideo == self._lexico[0][0]:
                    rev_comp += self._lexico[0][1]
                elif nucleotideo == self._lexico[0][3]:
                    rev_comp += self._lexico[0][2]
                elif nucleotideo == self._lexico[0][2]:
                    rev_comp += self._lexico[0][3]
                elif nucleotideo == self._lexico[0][4]:
                    rev_comp += '*'
                elif nucleotideo == self._lexico[1][1]:
                    rev_comp += self._lexico[1][0]
                elif nucleotideo == self._lexico[1][0]:
                    rev_comp += self._lexico[1][1]
                elif nucleotideo == self._lexico[1][3]:
                    rev_comp += self._lexico[1][2]
                elif nucleotideo == self._lexico[1][2]:
                    rev_comp += self._lexico[1][3]
                elif nucleotideo == self._lexico[1][5]:
                    rev_comp += self._lexico[1][4]
                elif nucleotideo == self._lexico[1][4]:
                    rev_comp += self._lexico[1][5]
                elif nucleotideo == self._lexico[1][7]:
                    rev_comp += self._lexico[1][6]
                elif nucleotideo == self._lexico[1][6]:
                    rev_comp += self._lexico[1][7]
                elif nucleotideo == self._lexico[1][9]:
                    rev_comp += self._lexico[1][8]
                elif nucleotideo == self._lexico[1][8]:
                    rev_comp += self._lexico[1][9]
                else:
                    rev_comp += self._lexico[1][10]
                index += 1
        except IndexError:
            print('O nucleotídeo %s da posição %i não tem par'%(nucleotideo, index,))
        finally:
            return rev_comp


class DNA(AcidoNucleico):
    _lexico = [('A', 'T', 'G', 'C'), ('W', 'S', 'M', 'K',
                                      'R', 'Y', 'B', 'V', 'H', 'D', 'N'), ]

    def __init__(self, sequencia, degenerado=False):
        self.deg = degenerado
        super().__init__(sequencia, self.deg)
        self.seq = sequencia
        print("DNA criado com sucesso")
        self.reverso_complementar = self._reverso_complementar()


class RNA(AcidoNucleico):
    _lexico = [('A', 'U', 'G', 'C', 'I'), ('W', 'S', 'M', 'K',
                                           'R', 'Y', 'B', 'V', 'H', 'D', 'N'), ]

    def __init__(self, sequencia, degenerado=False):
        self.deg = degenerado
        super().__init__(sequencia, self.deg)
        self.seq = sequencia
        print("RNA criado com sucesso")
        self.reverso_complementar = self._reverso_complementar()
