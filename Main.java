public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.setEdad(20);
        persona1.setNombre("Luis");
        persona1.setNumeroMovil("666 555 444");

        System.out.println("Tiene " + persona1.getEdad() + " años");
        System.out.println("Se llama " +persona1.getNombre());
        System.out.println("Su numero de movil es " + persona1.getNumeroMovil());
    }
}
class Persona{
    private int edad;
    private String nombre;
    private String  numeroMovil;

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public  String getNombre(){
        return this.nombre;
    }
    public void setNumeroMovil(String numeroMovil){
        this.numeroMovil = numeroMovil;
    }
    public  String getNumeroMovil(){
        return this.numeroMovil;
    }
}