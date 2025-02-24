import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

class Linea {
    public float[] p1;
    public float[] p2;

    public Linea(float[] p1, float[] p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public String toString() {
        return String.format("Linea de (%.2f, %.2f) a (%.2f, %.2f)", p1[0], p1[1], p2[0], p2[1]);
    }

    public void dibujalinea(Graphics g) {
        g.drawLine((int) p1[0], (int) p1[1], (int) p2[0], (int) p2[1]);
    }
}

class Circulo {
    public float[] centro;
    public float radio;

    public Circulo(float[] centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public String toString() {
        return String.format("Circulo con centro en (%.2f, %.2f) y radio %.2f", centro[0], centro[1], radio);
    }

    public void dibujacirculo(Graphics g) {
        g.drawOval((int) (centro[0] - radio), (int) (centro[1] - radio), (int) (2 * radio), (int) (2 * radio));
    }
}

class Dibujo extends JPanel {
    private Linea linea;
    private Circulo circulo;

    public Dibujo(Linea linea, Circulo circulo) {
        this.linea = linea;
        this.circulo = circulo;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        linea.dibujalinea(g);
        circulo.dibujacirculo(g);
    }
}

public class Main {
    public static void main(String[] args) {
        float[] p1 = {50, 50};
        float[] p2 = {200, 200};
        float[] centro = {150, 150};
        float radio = 100;

        Linea linea = new Linea(p1, p2);
        Circulo circulo = new Circulo(centro, radio);

        JFrame frame = new JFrame("Graficar Línea y Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(new Dibujo(linea, circulo));
        frame.setVisible(true);
    }
}
