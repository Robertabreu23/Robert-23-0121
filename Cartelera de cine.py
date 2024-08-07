def mostrar_cartelera():
  def obtener_detalles_pelicula(genero, pelicula_opcion):
      if genero == "Acción":
          if pelicula_opcion == 1:
              return "Deadpool & Wolverine", "La existencia pacífica de Deadpool se derrumba cuando la Autoridad de la Variación Temporal lo recluta para ayudar a proteger el multiverso. Pronto se une a su posible amigo, Wolverine, para completar la misión y salvar a su mundo de una amenaza existencial.", "R/18", "2h 7min"

          elif pelicula_opcion == 2:
              return "Bad Boys:Ride or Die", "Este verano, los Bad Boys favoritos del mundo están de regreso con su icónica mezcla de acción al borde del asiento y comedia escandalosa, pero esta vez con un giro: los mejores de Miami ahora están prófugos.", "R/14", "1h 50min"
      elif genero == "Comedia":
          if pelicula_opcion == 1:
              return "Harold and the Purple Crayon", "En su libro, el aventurero Harold puede hacer que cualquier cosa cobre vida con solo dibujarla. Cuando crece y se dibuja a sí mismo fuera de las páginas del libro y entra en el mundo físico, Harold descubre que tiene mucho que aprender sobre la vida real.", "S/R", "1h 32min"
          elif pelicula_opcion == 2:
              return "Fly Me to the Moon", "Ambientada en el histórico alunizaje del Apolo 11, en 1969. Llamados para mejorar la imagen pública de la NASA, las chispas vuelan en todas las direcciones cuando la prodigio del marketing Kelly Jones (Johansson) causa estragos en la ya difícil tarea del director del lanzamiento Cole Davis (Tatum). Cuando la Casa Blanca considera que la misión es demasiado importante para fracasar, Jones recibe la orden de simular un alunizaje falso como respaldo, comenzando la verdadera cuenta atrás...", "S/R", "2h 12min"
      elif genero == "Terror/Horror":
          if pelicula_opcion == 1:
              return "The exorcism", "El ganador del Oscar Russell Crowe interpreta a Anthony Miller, un actor con problemas que comienza a desmoronarse mientras filma una película de terror sobrenatural. Su hija distanciada, Lee (Ryan Simpkins), se pregunta si está volviendo a sus adicciones pasadas o si hay algo más siniestro en juego.", "R/18", "1h 35min"
          elif pelicula_opcion == 2:
              return "Maxxxine", "En el Hollywood de los años 80, Maxine Minx, estrella de cine para adultos y aspirante a actriz, finalmente consigue su gran oportunidad. Pero mientras un misterioso asesino acecha a las estrellas de Hollywood, un rastro de sangre amenaza con revelar su siniestro pasado.", "R/18", "1h 43min"
      return None, None, None, None

  while True:
      # Preguntar al usuario el género de la película
    print("Seleccione un género de película:")
    print("1. Acción")
    print("2. Comedia")
    print("3. Terror/Horror")

    genero_opcion = int(input("Ingrese el número de la opción deseada: "))

    if genero_opcion == 1:
      genero = "Acción"
      peliculas = ["Deadpool & Wolverine", "Bad Boys:Ride or Die"]
    elif genero_opcion == 2:
      genero = "Comedia"
      peliculas = ["Harold and the Purple Crayon", "Fly Me to the Moon"]
    elif genero_opcion == 3:
      genero = "Terror/Horror"
      peliculas = ["The exorcism", "Maxxxine"]
    else:
      print("Opción no válida.")
      continue

    print(f"\nSeleccione una película de {genero}:")
    for i, pelicula in enumerate(peliculas, 1):
      print(f"{i}. {pelicula}")

    pelicula_opcion = int(input("Ingrese el número de la opción deseada: "))

    titulo, sinopsis, clasificacion, duracion = obtener_detalles_pelicula(genero, pelicula_opcion)
    if titulo:
        # Mostrar detalles de la película seleccionada
        print(f"\nDetalles de la película '{titulo}':")
        print(f"Sinopsis: {sinopsis}")
        print(f"Clasificación: {clasificacion}")
        print(f"Duración: {duracion}")
    else:
        print("Opción no válida.")
        continue

      # Preguntar si desea ver otra película
    Continuar=input("¿Repetir? (Si/No): ")
    if Continuar.lower() != "si":
        print("Gracias por usar la cartelera de cine.")
        break


mostrar_cartelera()
