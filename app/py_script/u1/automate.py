import numpy as np


class Automate:
    def __init__(self):
        self.id_unite = 1
        self.num_auto = 1
        self.type_auto = 0x0000BA20
        self.temp_cuve = np.random.randint(25, 41) / 10
        self.temp_ex = np.random.randint(80, 141) / 10
        self.poids_cuve = np.random.randint(3512, 4608)
        self.poids_pro = 0
        self.m_ph = np.random.randint(68, 73) / 10
        self.m_k = np.random.randint(35, 48)
        self.c_nacl = np.random.randint(10, 18) / 10
        self.bact_sal = np.random.randint(17, 37)
        self.bact_e_coli = np.random.randint(35, 49)
        self.bact_list = np.random.randint(28, 55)