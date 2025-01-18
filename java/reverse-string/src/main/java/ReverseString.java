class ReverseString {

    String reverse(String inputString) {
        
        String reversedString = "";

        for (int i = 0; i < inputString.length(); i++) {
            reversedString = inputString.charAt(i) + reversedString;
        }

        return reversedString;
    }
}
