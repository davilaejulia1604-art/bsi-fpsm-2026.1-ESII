# acaiteria.py — sistema de pedidos de uma açaiteria de delivery (Aula 9)
#
# Este arquivo reúne os QUATRO padrões de projeto da aula, aplicados a UM
# sistema só, que foi crescendo passo a passo na apostila:
#
#   • Strategy  -> o cálculo da ENTREGA (moto, bicicleta, retirada)
#   • Factory   -> criar_entrega(nome): traduz um texto na estratégia certa
#   • Observer  -> os AVISOS quando o pedido é confirmado (cliente, cozinha, vendas)
#   • Facade    -> a classe Acaiteria: uma porta única que monta e usa tudo
#
# Tudo é texto no terminal (print) — sem banco, sem internet — para focar no
# desenho do código, não na tecnologia.
class Entrega:
    """Strategy (a abstrata). Toda forma de entrega promete um método preco()."""
    def preco(self, distancia_km):
        raise NotImplementedError("cada entrega concreta calcula o seu preço")


class EntregaMoto(Entrega):
    def preco(self, distancia_km):
        return 5.0 + 2.0 * distancia_km


class EntregaBicicleta(Entrega):
    def preco(self, distancia_km):
        return 3.0 + 1.0 * distancia_km


class Retirada(Entrega):
    def preco(self, distancia_km):
        return 0.0


class EntregaDrone(Entrega):
    def preco(self, distancia_km):
        return 8.0 + 3.0 * distancia_km


# ----------------------------------------------------------------------
# FACTORY
# ----------------------------------------------------------------------
def criar_entrega(nome):
    """Simple Factory: recebe um texto e devolve a estratégia de Entrega certa."""
    opcoes = {
        "moto": EntregaMoto,
        "bici": EntregaBicicleta,
        "retirada": Retirada,
        "drone": EntregaDrone,   # <-- LINHA ADICIONADA
    }

    if nome not in opcoes:
        raise ValueError(f"forma de entrega desconhecida: {nome!r}")

    return opcoes[nome]()


# ----------------------------------------------------------------------
# OBSERVER
# ----------------------------------------------------------------------
class Observador:
    """Observer (o abstrato)."""
    def atualizar(self, evento):
        raise NotImplementedError("cada observador reage do seu jeito")


class AvisaCliente(Observador):
    def atualizar(self, evento):
        print(f"[SMS] Oi {evento['cliente']}, seu açaí saiu! "
              f"Total R$ {evento['total']:.2f}")


class PainelCozinha(Observador):
    def atualizar(self, evento):
        print(f"[COZINHA] Preparar pedido de {evento['cliente']}")


class RegistroVendas(Observador):
    def atualizar(self, evento):
        print(f"[VENDAS] +R$ {evento['total']:.2f} registrado")


# ----------------------------------------------------------------------
# FACADE
# ----------------------------------------------------------------------
class Acaiteria:
    def __init__(self):
        self._observadores = [
            AvisaCliente(),
            PainelCozinha(),
            RegistroVendas()
        ]

    def inscrever(self, observador):
        self._observadores.append(observador)

    def _notificar(self, evento):
        for obs in self._observadores:
            obs.atualizar(evento)

    def finalizar(self, cliente, itens, metodo_entrega, distancia_km):
        subtotal = sum(itens)
        entrega = criar_entrega(metodo_entrega)
        total = subtotal + entrega.preco(distancia_km)

        evento = {
            "cliente": cliente,
            "total": total
        }

        self._notificar(evento)
        return total


# ----------------------------------------------------------------------
# TESTE
# ----------------------------------------------------------------------
if __name__ == "__main__":
    loja = Acaiteria()

    print("Pedido da Ana (Moto):")
    total = loja.finalizar("Ana", [12.0, 4.0], "moto", 3)
    print(f"Total: R$ {total:.2f}\n")

    print("Pedido do João (Bicicleta):")
    total = loja.finalizar("João", [20.0], "bici", 5)
    print(f"Total: R$ {total:.2f}\n")

    print("Pedido da Maria (Retirada):")
    total = loja.finalizar("Maria", [15.0, 10.0], "retirada", 0)
    print(f"Total: R$ {total:.2f}\n")

    print("Pedido do Pedro (Drone):")
    total = loja.finalizar("Pedro", [25.0, 8.0], "drone", 4)
    print(f"Total: R$ {total:.2f}")

# ----------------------------------------------------------------------
# STRATEGY — cada forma de entrega é uma classe que sabe calcular o seu preço
# ----------------------------------------------------------------------
