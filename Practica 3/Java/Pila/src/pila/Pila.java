package pila;

public class Pila {
    private int[] elementos;
    private int tope;

    public Pila(int capacidad) {
        elementos = new int[capacidad];
        tope = -1;
    }

    public void apilar(int elemento) {
        if (tope == elementos.length - 1) {
            throw new IllegalStateException("La pila está llena");
        }
        elementos[++tope] = elemento;
    }

    public int desapilar() {
        if (estaVacia()) {
            throw new IllegalStateException("La pila está vacía");
        }
        return elementos[tope--];
    }

    public boolean estaVacia() {
        return tope == -1;
    }

    public int verTope() {
        if (estaVacia()) {
            throw new IllegalStateException("La pila está vacía");
        }
        return elementos[tope];
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i <= tope; i++) {
            sb.append(elementos[i]);
            if (i < tope) sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.apilar(10);
        pila.apilar(20);
        pila.apilar(30);
        System.out.println("Pila: " + pila);
        System.out.println("Tope: " + pila.verTope());
        System.out.println("Desapilar: " + pila.desapilar());
        System.out.println("Pila después de desapilar: " + pila);
    }
}
