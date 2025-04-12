package herenciaMultiple;

public class D extends A {
	private B b;
	
	public D(int x, int y, int z) {
		super(x, z);
		this.b = new B(y, z);
	}
	
	public void incrementaXYZ() {
		x++;
		b.y++;
		z++;
		b.z++;
	}
	
	public int obtenerY() {
		return b.y;
	}
	
	public int obtenerZdeB() {
		return b.z;
	}
	
	public void mostrarValores() {
		System.out.println("D - x: " + x + ", y: " + b.y + ", z (A): " + z + ", z (B): " + b.z);
	}
	
	public void incrementarZ() {
		super.incrementaZ();
		b.incrementaZ();
	}
	
	public void establecerValores(int x, int y, int z) {
		this.x = x;
		this.b.y = y;
		this.z = z;
		this.b.z = z;
	}
}
