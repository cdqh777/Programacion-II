package estPOO;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class EstadisticaPOO {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("");
        String input = reader.readLine();

        double[] datos = Arrays.stream(input.split(" "))
                              .mapToDouble(Double::parseDouble)
                              .toArray();

        Estadisticas estadisticas = new Estadisticas(datos);
        System.out.printf("El promedio es %.2f%n", estadisticas.getPromedio());
        System.out.printf("La desviación estándar es %.5f%n", estadisticas.getDesviacion());
    }
}

class Estadisticas {
    private double[] datos;
    private double promedio;
    private double desviacion;

    public Estadisticas(double[] datos) {
        this.datos = datos;
        this.promedio = calcularPromedio();
        this.desviacion = calcularDesviacion();
    }

    private double calcularPromedio() {
        double suma = 0;
        for (double dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }

    private double calcularDesviacion() {
        double varianza = 0;
        for (double dato : datos) {
            varianza += Math.pow(dato - promedio, 2);
        }
        varianza /= (datos.length - 1);
        return Math.sqrt(varianza);
    }

    public double getPromedio() {
        return promedio;
    }

    public double getDesviacion() {
        return desviacion;
    }
}