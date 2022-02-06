import java.util.ArrayList;

/*
   * home
   * documents
   * gamer.xml
   * test.xml
   * test
   * etc
*/

class Node{
    public String val;
    public ArrayList<Node> children;
    public Node(String val){
        this.val = val;
        this.children = new ArrayList<>();
    }


    public int hashCode(){
        return this.val.hashCode();
    }
}

class Solution {
    public void parseFilePaths(String[] paths) {
        Node root = new Node("/");
        for (String p : paths){
            String[] tokens = p.split("/");
            Node currentNode = root;
            for (String t : tokens){
                boolean found = false;
                for(Node n : currentNode.children){
                    if(n.val.equals(t) ){
                        currentNode  = n;
                        found = true;
                        break;
                    }
                }
                if (!found){
                    Node next = new Node(t);
                    currentNode.children.add(next);
                    currentNode = next;
                }
            }
        }
        dfsPrint(root, 0);

    }

    public void dfsPrint(Node root, int depth){
        for(int i =0; i < depth; i++){
            System.out.print("\t");
        }
        
        System.out.println(root.val);
        for(Node n : root.children){
            dfsPrint(n, depth + 1);
        }
    }

    public static void main(String[] args) {
        String[] inputs = {
                "/home/documents/gamer.xml",
                "/home/documents/epic.xml",
                "/etc/test/wowsers.xml,",
                "/home/test/gamer.xml",
                "/etc/documents/again/testing.xml",
                "/etc/file.xml", };

        Solution driver = new Solution();
        driver.parseFilePaths(inputs);

    }

}
