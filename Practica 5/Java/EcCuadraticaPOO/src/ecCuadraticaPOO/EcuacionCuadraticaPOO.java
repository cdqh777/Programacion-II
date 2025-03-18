package ecCuadraticaPOO;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EcuacionCuadraticaPOO {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Ingrese a, b, c: ");
        String input = reader.readLine();
        String[] valores = input.split(" ");

        double a = Double.parseDouble(valores[0]);
        double b = Double.parseDouble(valores[1]);
        double c = Double.parseDouble(valores[2]);
        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);

        double discriminante = ecuacion.getDiscriminante();
        if (discriminante > 0) {
            System.out.printf("La ecuacion tiene dos raíces %.6f y %.5f%n", 
                ecuacion.getRaiz1(), ecuacion.getRaiz2());
        } else if (discriminante == 0) {
            System.out.printf("La ecuacion tiene una raíz %.0f%n", ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuacion no tiene raíces reales");
        }
    }
}

class EcuacionCuadratica {
    private double a;
    private double b;
    private double c;

    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return b * b - 4 * a * c;
    }

    public double getRaiz1() {
        double discriminante = getDiscriminante();
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public double getRaiz2() {
        double discriminante = getDiscriminante();
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
}