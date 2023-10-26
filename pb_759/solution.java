package Daily.pb_759;

import java.util.ArrayList;

public class solution {
	ArrayList<String> list = new ArrayList<String>();
	String nb="25525502";
	public static void main(String[] args){
		String Ans = "";
		int value = 0;
		int	dot = 0;
	}
	public void gen_ip(String Ans, String nb, int value, int i, int dot){
		if (value > 255)
			return;
		if (Ans.equals("") || Ans.charAt(Ans.length() - 1) != '.'){
			Ans += nb.charAt(i);
			value += (int)(nb.charAt(i) - '0');
			i++;
			gen_ip(Ans, nb, value, i, dot);
		}
		
	}
}
