package estME;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class EstadisticaModular {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("");
        String input = reader.readLine();

        double[] datos = Arrays.stream(input.split(" "))
                              .mapToDouble(Double::parseDouble)
                              .toArray();

        double prom = promedio(datos);
        double desv = desviacion(datos, prom);

        System.out.printf("El promedio es %.2f%n", prom);
        System.out.printf("La desviación estándar es %.5f%n", desv);
    }

    public static double promedio(double[] datos) {
        double suma = 0;
        for (double dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }

    public static double desviacion(double[] datos, double promedio) {
        double varianza = 0;
        for (double dato : datos) {
            varianza += Math.pow(dato - promedio, 2);
        }
        varianza /= (datos.length - 1);
        return Math.sqrt(varianza);
    }
}