package tokenizer;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class tokenizer {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		FileOutputStream output = new FileOutputStream("c:/dataset.txt", true);
		Scanner input = new Scanner(System.in);
		while (true) {
			StringBuffer contents = new StringBuffer();

			while (true) {
				String temp = new String();
				temp = input.nextLine();
				if (temp.equals("000")) {
					break;
				}
				contents.append(temp);

			}

			String token_contents = new String();
			token_contents = contents.toString();
			String Array[] = token_contents.split("¡°|¡±|\"");

			for (int a = 1; a < Array.length; a = a + 2) {
				byte[] by = Array[a].getBytes();
				System.out.println(Array[a]);
				output.write(by);
				by = "\r\n".getBytes();
				output.write(by);
			}
			Array = null;
			token_contents = null;
			contents = null;
			

		}
	}

}
