package ecCuadraticaME;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EcuacionCuadraticaModular {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Ingrese a, b, c: ");
        String input = reader.readLine();
        String[] valores = input.split(" ");

        double a = Double.parseDouble(valores[0]);
        double b = Double.parseDouble(valores[1]);
        double c = Double.parseDouble(valores[2]);
        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            double raiz1 = getRaiz1(a, b, discriminante);
            double raiz2 = getRaiz2(a, b, discriminante);
            System.out.printf("La ecuacion tiene dos raíces %.6f y %.5f%n", raiz1, raiz2);
        }
        
        else if (discriminante == 0) {
            double raiz = getRaiz1(a, b, discriminante);
            System.out.printf("La ecuacion tiene una raíz %.0f%n", raiz);
        }
        
        else {
            System.out.println("La ecuacion no tiene raíces reales");
        }
    }

    public static double getDiscriminante(double a, double b, double c) {
        return b * b - 4 * a * c;
    }

    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
}