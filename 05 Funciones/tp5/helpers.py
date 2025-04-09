def valida_numero(numero, operacion):
  if not isinstance(numero, (int, float)):
    print(f"Ingresó un dato incorrecto para {operacion}")
  return False