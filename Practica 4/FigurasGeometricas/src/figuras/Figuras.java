package figuras;

import java.text.DecimalFormat;

abstract class Figura {
    public abstract double area();
}

class Rectangulo extends Figura {
    private double base;
    private double altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    public double area() {
        return base * altura;
    }
}

class Circulo extends Figura {
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }

    public double area() {
        return Math.PI * radio * radio;
    }
}

class TrianguloRec extends Figura {
    private double base;
    private double altura;

    public TrianguloRec(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    public double area() {
        return (base * altura) / 2;
    }
}

class Trapecio extends Figura {
    private double baseMayor;
    private double baseMenor;
    private double altura;

    public Trapecio(double baseMayor, double baseMenor, double altura) {
        this.baseMayor = baseMayor;
        this.baseMenor = baseMenor;
        this.altura = altura;
    }

    public double area() {
        return ((baseMayor + baseMenor) * altura) / 2;
    }
}

class Pentagono extends Figura {
    private double lado;

    public Pentagono(double lado) {
        this.lado = lado;
    }

    public double area() {
        return (5 * lado * lado) / (4 * Math.tan(Math.PI / 5));
    }
}

public class Figuras {
    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.##");

        Figura rectangulo = new Rectangulo(5, 10);
        Figura circulo = new Circulo(7);
        Figura triangulo = new TrianguloRec(6, 8);
        Figura trapecio = new Trapecio(10, 6, 4);
        Figura pentagono = new Pentagono(5);

        System.out.println("Rectangulo: " + df.format(rectangulo.area()));
        System.out.println("Circulo: " + df.format(circulo.area()));
        System.out.println("Triangulo: " + df.format(triangulo.area()));
        System.out.println("Trapecio: " + df.format(trapecio.area()));
        System.out.println("Pentagono: " + df.format(pentagono.area()));
    }
}