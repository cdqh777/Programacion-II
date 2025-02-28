package cola;

public class Cola {
    private int[] elementos;
    private int frente;
    private int fin;

    public Cola(int capacidad) {
        elementos = new int[capacidad];
        frente = 0;
        fin = -1;
    }

    public void encolar(int elemento) {
        if (fin == elementos.length - 1) {
            throw new IllegalStateException("La cola está llena");
        }
        elementos[++fin] = elemento;
    }

    public int desencolar() {
        if (estaVacia()) {
            throw new IllegalStateException("La cola está vacía");
        }
        return elementos[frente++];
    }

    public boolean estaVacia() {
        return frente > fin;
    }

    public int verFrente() {
        if (estaVacia()) {
            throw new IllegalStateException("La cola está vacía");
        }
        return elementos[frente];
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = frente; i <= fin; i++) {
            sb.append(elementos[i]);
            if (i < fin) sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        Cola cola = new Cola(5);
        cola.encolar(10);
        cola.encolar(20);
        cola.encolar(30);
        System.out.println("Cola: " + cola);
        System.out.println("Frente: " + cola.verFrente());
        System.out.println("Desencolada: " + cola.desencolar());
        System.out.println("Cola sin desencolar: " + cola);
    }
}