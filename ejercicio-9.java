public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setCredito(250.00);
        Trabajador trabajador = new Trabajador();
        trabajador.setSalario(1500.00);

        System.out.println("Los datos del cliente son");
        System.out.println("Nombre "+ cliente.nombre);
        System.out.println("Edad "+ cliente.edad);
        System.out.println("Telefono "+ cliente.telefono);
        System.out.println("Credito  "+ cliente.getCredito());
        System.out.println("");
        System.out.println("Los datos del Trabajador son");
        System.out.println("Nombre "+ trabajador.nombre);
        System.out.println("Edad "+ trabajador.edad);
        System.out.println("Telefono "+ trabajador.telefono);
        System.out.println("Salario  "+ trabajador.getSalario());






    }
}
class Persona {
    int edad;
    String nombre;
    String telefono;

}


class Cliente extends Persona{
    private double credito;
    String nombre = "Juan";
    String telefono = "666 555 444";
    int edad = 25;

    public void setCredito(double credito) {
        this.credito = credito;
    }

    public double getCredito() {
        return credito;
    }
}
class Trabajador extends Persona{
    String nombre = "Alberto";
    String telefono = "564 654 456";
    private double salario ;
    int edad = 25;
    public  void setSalario(double salario){
        this.salario = salario;
    }
    public double getSalario(){
        return salario;
    }
}


