package herenciaMultiple;

public class Main {

	public static void main(String[] args) {
		A a = new A(3, 5);
		B b = new B(1, 4);
		D d = new D(2, 6, 5);
		
		System.out.println("Valores iniciales:");
		System.out.println("A: x=" + a.x + ", z=" + a.z);
		System.out.println("B: y=" + b.y + ", z=" + b.z);
		d.mostrarValores();
		
		a.incrementaXZ();
		b.incrementaYZ();
		d.incrementaXYZ();
		
		System.out.println("Valores incrementados:");
		System.out.println("A: x=" + a.x + ", z=" + a.z);
		System.out.println("B: y=" + b.y + ", z=" + b.z);
		d.mostrarValores();
		
		System.out.println("Conflicto con Z:");
		System.out.println("Z en A:" + d.z);
		System.out.println("Z en B:" + d.obtenerZdeB());
	}

}
