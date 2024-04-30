from typing import List
from Administrativo import Administrativo
from Funcionario import Funcionario
from Professor import Professor

funcionarios: List[Funcionario] = []
funcionarios.append(Professor("Fulano", 100, "123456"))
funcionarios.append(Administrativo("Sicrano", 21, "Compras"))
funcionarios.append(Professor("Beltrano", 23, "654321"))
funcionarios.append(Administrativo("Fortrano", 21, "Compras"))
funcionarios.append(Professor("Pentano", 23, "456545"))
funcionarios.append(Administrativo("Hexano", 21, "Compras"))
funcionarios.append(Professor("Hepnato", 23, "788987"))

for f in funcionarios:
    print(f"{f.nome} recebe {f.calcular_salario()} por mês.")
