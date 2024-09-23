Es problema se nos ocurre una euristica gredy que cosite basicamente en construir la cadena de optima poniendo las letras de mayor peso lexico grafico al final de la cadena y manteniendo una idea de balance sobre las letras que pasaremos a explicar si nos percatamos si al poner las letras se cumple algo como maximo inicialmente se pueden colocar k+1 letras para mantener el balance puesto que si no se rombe el balance al poner 1 letra cualquiera a su derecha por ejemplo supongamos que k = 1  si tenemos abbb o _bbb donde _ es cualquier posible letra sera un caso invalido deforma general se cumple que el numero de letras que se pueden colocar a la derecha es el maximo debes se k+1


Este problemas inicialmente conocemos que podiamos hacer una dinamica que calcule calcuale el camino de costo minimo entre todos los vertices y llevar una matriz como subestructura optima que lleva la mejor distancia hasta el momento y el mejor camino si hay mas de un camino con distancia optima llevarlos por lo que llevariamos todo los caminos que ente i,j que son mejores hasta el momento si aparce uno mejor entonces este es el nuevo mejor para ello el primer via de solucion fue modificar el algoritmo floid warschal este algoritmo es V^3 pero podemos mejorar esto con una dinamica que explicaremos proximamente que es O(EV) en el peor de los caso este algoritmo es V^3 pero en el resto es mejora el rendimiento 





