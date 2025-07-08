from src.domain.reloj import Reloj

reloj1 = Reloj(10, 30, 0)
reloj2 = Reloj(15, 45, 50)
reloj3 = Reloj(23, 59, 59)

print("Reloj 1:", reloj1)
print("Reloj 2:", reloj2)
print("Reloj 3:", reloj3)

reloj1.adelantar_minutos(1)
print("\nReloj 1 después de adelantar 1 minuto:", reloj1)

reloj2.update_hora(10, 31, 0)
print("Reloj 2 después de update_hora:", reloj2)

if reloj1.es_igual(reloj2):
    print("Reloj 1 y Reloj 2 tienen la misma hora.")
else:
    print("Reloj 1 y Reloj 2 tienen distinta hora.")

reloj_sistema = Reloj.obtener_instancia(12, 0, 0)
print("\nSingleton (Reloj del sistema):", reloj_sistema)

reloj_sistema.update_hora(14, 30, 0)
print("Reloj del sistema actualizado:", reloj_sistema)

otro_reloj = Reloj.obtener_instancia(5, 5, 5)
print("¿Singleton sigue siendo el mismo?:", otro_reloj)
