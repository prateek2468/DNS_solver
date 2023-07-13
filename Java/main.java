package Java;

/**
 * main
 */
public class DNSheader{
    private int id ; 
    private int flags ; 
    private int num_questions =0; 
    private int num_answers =  0 ; 
    private int num_authorities =  0 ; 
    private int num_additions = 0 ; 

    public DNSheader(int id , int flags , int num_questions , int num_answers , int num_authorities  , int num_additions ){
        this.id = id ; 
        this.flags = flags ; 
        this.num_questions = num_questions ; 
        this.num_answers = num_answers ; 
        this.num_authorities = num_authorities ; 
        this.num_questions = num_questions ; 
    }

}

public class main {


    public static void main(String[] args) {
        
    }
}