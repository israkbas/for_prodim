def kok_bul(f, low, high, epsilon=1e-6):
    """
    Artan bir fonksiyonun f(x)=0 kökünü bisection(ikiye bölme) yöntemi ile bulur.
    """

    # Aralık kontrol
    if low >= high:
        raise ValueError("Alt sınır üst sınırdan küçük olmalıdır.")

    # Kökün verilen aralıkta olduğunun kontrolü
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


# Herhangi bir örnek fonksiyon 
def f(x):
    return x**2 - 9

try:
    root = kok_bul(f, 0, 10)

    print("Bulunan kök:", root)
    print("Kontrol f(kök):", f(root))

except ValueError as e:
    print("Hata:", e)

except Exception:
    print("Beklenmeyen bir hata oluştu.")