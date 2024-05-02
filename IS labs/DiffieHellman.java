public class DiffieHellman {
    public static long power(long a, long b , long P){
        if(b==1){
            return a;
        }else{
            return ((long)Math.pow(a,b))%P;
        }
    }
    
    public static void main(String[] args) {
        int P = 7;
        System.out.println("P : "+P);
        int G = 3;
        System.out.println("G : "+G);

        int a = 4;
        int b=3;

        long x = power(G , a , P);
        System.out.println("Public key of A : "+x);
        long y = power(G , b , P);
        System.out.println("Public key of B : "+y);

        long ka = power(y , a , P);
        System.out.println("Secret key of A: "+ka);
        long kb = power(x , b , P);
        System.out.println("Secret key of B: "+kb);
    }
}
