class AerDisplay:
    def get_elements_dic_instance(self):
        art = []
        for key in sorted(self.__dict__):
            art.append(f'{key} = {self.__dict__[key]}\n')
        return ''.join(art)

    def __str__(self):
        return f'Class :{self.__class__.__name__}\n{self.get_elements_dic_instance()}'

