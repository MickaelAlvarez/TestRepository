package parser;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ListFileNameParser {

    /*
     * commentaire
     */

    public static List<String> parse(
            File file
    )
    {
        // This is a commentary 
        ArrayList<String> listFile = new ArrayList<>(); // test
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();
            while (line != null) {
                listFile.add(getDataFromLine(line));
            }

            String test = "a";

            switch (test) {
                case "a":
                    break;
                default:
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return listFile;
    }

    /**
     * Javadoc
     * @param line
     * @return
     */
    private static String getDataFromLine(
            String line
    )
    {
        String[] lineSplitted = line.split("\\\t");
        return lineSplitted[1];
    }
}
