package problemaDiamante;

public class D extends B{
	private C c = new C();
	
	public void metodo() {
		System.out.println("Metodo de D");
		super.metodo();
		c.metodo();
	}

}
