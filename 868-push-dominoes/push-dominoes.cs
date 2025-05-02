public class Solution {
    public string PushDominoes(string dominoes) {
        string result = "";

        while (!result.Equals(dominoes)) {
            result = dominoes;
            dominoes = dominoes.Replace("R.L", "-").Replace(".L", "LL").Replace("R.", "RR");
        }

        return result.Replace("-", "R.L");
    }
}