def valida_numero(numero, operacion):
  if not isinstance(numero, (int, float)):
   return print(f"Ingresó un dato incorrecto para {operacion}.")