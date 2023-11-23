import java.util.Scanner;

public class AdditiveCipher {

    public static String encrypt(String plainText, int key) {
        StringBuilder encryptedText = new StringBuilder();
        for (int i = 0; i < plainText.length(); i++) {
            if (Character.isUpperCase(plainText.charAt(i))) {
                char ch = (char) (((int) plainText.charAt(i) + key - 65) % 26 + 65);
                encryptedText.append(ch);
            } else {
                char ch = (char) (((int) plainText.charAt(i) + key - 97) % 26 + 97);
                encryptedText.append(ch);
            }
        }
        return encryptedText.toString();
    }

    public static String decrypt(String encryptedText, int key) {
        StringBuilder decryptedText = new StringBuilder();
        for (int i = 0; i < encryptedText.length(); i++) {
            if (Character.isUpperCase(encryptedText.charAt(i))) {
                char ch = (char) (((int) encryptedText.charAt(i) - key - 65 + 26) % 26 + 65);
                decryptedText.append(ch);
            } else {
                char ch = (char) (((int) encryptedText.charAt(i) - key- 97 + 26) % 26 + 97);
                decryptedText.append(ch);
            }
        }
        return decryptedText.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the plaintext: ");
        String plainText = scanner.nextLine();

        System.out.print("Enter the key  positive number");
        int key = scanner.nextInt();

        String encryptedText = encrypt(plainText, key);
        System.out.println("Encrypted Text: " + encryptedText);

        String decryptedText = decrypt(encryptedText, key);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }
}
