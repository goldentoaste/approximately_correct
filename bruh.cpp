class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        boolean res = false;
        Character last;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '[' ||s.charAt(i) == '{'){
                brackets.push(s.charAt(i));
            }
            else if(brackets.isEmpty()){
                return false;
            }
            if(s.charAt(i) == ')'){
                last = brackets.pop();
                if(last != '(')
                    return false;
            }
            if(s.charAt(i) == '}'){
                last = brackets.pop();
                if(last != '{')
                    return false;
            }
            if(s.charAt(i) == ']'){
                last = brackets.pop();
                if(last != '[')
                    return false;
            }     
    }
        if(brackets.isEmpty())
            return true;
        return false;
}
}