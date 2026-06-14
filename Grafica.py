import matplotlib.pyplot as plt

def graficar (
        resultados1,
        resultados2,
        nombre1="Texto 1",
        nombre2 = "Texto 2"
):
    temperaturas = list(
        resultados1.keys()
    )
    entropia1 = list(
        resultados1.values()
    )
    entropia2 = list(
        resultados2.values()
    )
    plt.figure(figsize=(8,5))

    plt.plot(
        temperaturas,
        entropia1,
        marker="x",
        label=nombre1
    )

    plt.plot(
        temperaturas,
        entropia2,
        marker="o",
        label=nombre2
    )
    for x, y in zip(temperaturas, entropia1):
        plt.annotate(
            f"{y:.2f}",
            (x,y)
    )
    for x, y in zip(
        temperaturas,
        entropia2
    ):
        plt.annotate(
            f"{y:.2f}",
            (x, y)
        )
    plt.xlabel("Temperatura")
    plt.ylabel("Entropía")
    plt.title(
        "Entropía vs. Temperatura"
    )
    plt.grid(True)
    plt.legend()
    plt.show()