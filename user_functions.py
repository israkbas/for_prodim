import math


def kok_bul(f, low, high, epsilon=1e-6):

    if f(low) >= 0 or f(high) <= 0:
        raise ValueError(
            "Geçersiz aralık! f(alt sınır) < 0 ve f(üst sınır) > 0 olmalıdır."
        )

    while (high - low) > epsilon:
        mid = (low + high) / 2

        if f(mid) < 0:
            low = mid
        else:
            high = mid

    return (low + high) / 2


def main():

    print("Fonksiyon giriniz (Python formatında).")
    print("Örnekler:")
    print("x**2 - 9")
    print("3*x + 2")
    print("math.exp(x) - 5\n")

    expression = input("f(x) = ")

    # Girilen fonksiyonun geçerli olup olmadığını kontrol etmek için
    try:
        eval(expression, {"x": 1, "math": math})
    except Exception:
        print("Hata: Geçersiz fonksiyon ifadesi girdiniz.")
        return

    # Alt ve üst sınır kontrol
    try:
        low = float(input("Alt sınır: "))
        high = float(input("Üst sınır: "))
    except ValueError:
        print("Hata: Lütfen sayısal bir değer giriniz.")
        return

    if low >= high:
        print("Hata: Alt sınır üst sınırdan küçük olmalıdır.")
        return

    def f(x):
        return eval(expression, {"x": x, "math": math})

    try:
        root = kok_bul(f, low, high)

        print("\nBulunan kök =", root)
        print("Kontrol f(kök) =", f(root))

    except ValueError as e:
        print("Hata:", e)
    except Exception:
        print("Beklenmeyen bir hata oluştu.")


if __name__ == "__main__":
    main()